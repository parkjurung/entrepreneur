#!/usr/bin/env python3
"""Extract Pagecall standard financial statement PDFs into analysis-friendly JSON.

The source PDFs have an embedded text layer, so this script uses PyMuPDF text
extraction rather than OCR. It also writes raw page text for auditability.
"""

from __future__ import annotations

import json
import re
import unicodedata
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import fitz


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "data" / "source-documents" / "financial-statements"
OUTPUT_DIR = ROOT / "data" / "extracted" / "financial-statements"
RAW_TEXT_DIR = OUTPUT_DIR / "raw-text"
JSON_PATH = OUTPUT_DIR / "financial_statements.json"
REPORT_PATH = OUTPUT_DIR / "extraction_report.md"

CODE_RE = re.compile(r"^\d{3}$")
AMOUNT_RE = re.compile(r"^-?[0-9,]+$")
ISSUE_NO_RE = re.compile(r"\d{4}-\d{3}-\d{4}-\d{3}")
BUSINESS_NO_RE = re.compile(r"\d{3}-\d{2}-\d{5}")
CORPORATE_NO_RE = re.compile(r"\d{6}-\*+")
DATE_RE = re.compile(r"\d{4}\.\s*\d{2}\.\s*\d{2}")


@dataclass(frozen=True)
class ParsedRow:
    account_name: str
    code: str
    amount: int
    amount_text: str
    page: int
    row_index: int


def normalize_text(value: str) -> str:
    return unicodedata.normalize("NFC", value).strip()


def parse_amount(value: str) -> int:
    return int(value.replace(",", ""))


def compact_lines(text: str) -> list[str]:
    return [normalize_text(line) for line in text.splitlines() if normalize_text(line)]


def parse_statement_rows(page_text: str, page_number: int) -> list[ParsedRow]:
    lines = compact_lines(page_text)
    rows: list[ParsedRow] = []

    for i in range(len(lines) - 2):
        account_name = lines[i]
        code = lines[i + 1]
        amount_text = lines[i + 2]

        if not CODE_RE.match(code):
            continue
        if not AMOUNT_RE.match(amount_text):
            continue
        if account_name in {"코드", "금", "액"}:
            continue
        if CODE_RE.match(account_name) or AMOUNT_RE.match(account_name):
            continue

        rows.append(
            ParsedRow(
                account_name=account_name,
                code=code,
                amount=parse_amount(amount_text),
                amount_text=amount_text,
                page=page_number,
                row_index=len(rows),
            )
        )

    return rows


def first_match(pattern: re.Pattern[str], text: str) -> str | None:
    match = pattern.search(text)
    return normalize_text(match.group(0)) if match else None


def find_after(lines: list[str], label: str) -> str | None:
    for i, line in enumerate(lines[:-1]):
        if line == label:
            return lines[i + 1]
    return None


def parse_certificate_metadata(page_text: str, filename: str) -> dict[str, Any]:
    lines = compact_lines(page_text)
    joined = "\n".join(lines)
    dates = [normalize_text(match.group(0)).replace(" ", "") for match in DATE_RE.finditer(joined)]
    business_year_start = dates[0] if len(dates) >= 1 else None
    business_year_end = dates[1] if len(dates) >= 2 else None
    filing_date = dates[2] if len(dates) >= 3 else None

    certificate_year_month = None
    certificate_day = None
    for i, line in enumerate(lines[:-1]):
        if re.fullmatch(r"\d{4}년\d{1,2}월", line):
            certificate_year_month = line
            certificate_day = lines[i + 1]
            break

    attachment_start = None
    for i in range(len(lines) - 3):
        if lines[i : i + 4] == ["첨", "부", "서", "류"]:
            attachment_start = i + 4
            break

    attachments: list[str] = []
    if attachment_start is not None:
        for line in lines[attachment_start:]:
            if line == "신":
                break
            attachments.append(line)

    return {
        "source_filename": filename,
        "issue_number": first_match(ISSUE_NO_RE, joined),
        "company_name": find_after(lines, "상호( 법인명)"),
        "business_registration_number": first_match(BUSINESS_NO_RE, joined),
        "representative": find_after(lines, "성명( 대표자)"),
        "corporate_registration_number_masked": first_match(CORPORATE_NO_RE, joined),
        "business_type": find_after(lines, "태"),
        "business_item": find_after(lines, "목"),
        "business_address": find_after(lines, "장"),
        "business_year_start": business_year_start,
        "business_year_end": business_year_end,
        "attachments": attachments,
        "filing_type": "정기 신고" if "정기" in lines and "신고" in lines else None,
        "filing_date": filing_date,
        "certificate_date_text": (
            f"{certificate_year_month} {certificate_day}" if certificate_year_month and certificate_day else None
        ),
        "receipt_number": find_after(lines, "접수번호"),
        "tax_office": next((line.replace("서장", "세무서") for line in lines if line.endswith("세무서장")), None),
        "department": find_after(lines, "담당부서"),
        "contact": next((line for line in lines if re.fullmatch(r"\d{2}-\d{4}-\d{4}", line)), None),
    }


def rows_to_json(rows: list[ParsedRow]) -> list[dict[str, Any]]:
    return [
        {
            "account_name": row.account_name,
            "code": row.code,
            "amount": row.amount,
            "amount_text": row.amount_text,
            "page": row.page,
            "row_index": row.row_index,
        }
        for row in rows
    ]


def amount_by_code(rows: list[ParsedRow]) -> dict[str, int]:
    return {row.code: row.amount for row in rows}


def metric_value(rows: list[ParsedRow], code: str) -> int | None:
    for row in rows:
        if row.code == code:
            return row.amount
    return None


def build_metrics(balance_rows: list[ParsedRow], income_rows: list[ParsedRow]) -> dict[str, Any]:
    return {
        "balance_sheet": {
            "current_assets": metric_value(balance_rows, "001"),
            "cash_and_cash_equivalents": metric_value(balance_rows, "003"),
            "total_assets": metric_value(balance_rows, "228"),
            "current_liabilities": metric_value(balance_rows, "229"),
            "noncurrent_liabilities": metric_value(balance_rows, "284"),
            "total_liabilities": metric_value(balance_rows, "333"),
            "capital_stock": metric_value(balance_rows, "334"),
            "capital_surplus": metric_value(balance_rows, "337"),
            "retained_earnings": metric_value(balance_rows, "372"),
            "total_equity": metric_value(balance_rows, "382"),
            "total_liabilities_and_equity": metric_value(balance_rows, "383"),
        },
        "income_statement": {
            "revenue": metric_value(income_rows, "001"),
            "cost_of_sales": metric_value(income_rows, "035"),
            "gross_profit": metric_value(income_rows, "066"),
            "selling_general_admin_expenses": metric_value(income_rows, "067"),
            "operating_income": metric_value(income_rows, "129"),
            "non_operating_income": metric_value(income_rows, "130"),
            "non_operating_expenses": metric_value(income_rows, "179"),
            "pretax_income": metric_value(income_rows, "217"),
            "income_tax_expense": metric_value(income_rows, "218"),
            "net_income": metric_value(income_rows, "219"),
        },
    }


def validate_document(balance_rows: list[ParsedRow], income_rows: list[ParsedRow]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    balance = amount_by_code(balance_rows)
    income = amount_by_code(income_rows)

    def add_check(name: str, actual: int | None, expected: int | None) -> None:
        checks.append(
            {
                "name": name,
                "actual": actual,
                "expected": expected,
                "passed": actual is not None and expected is not None and actual == expected,
            }
        )

    add_check("assets_equal_liabilities_plus_equity", balance.get("228"), (balance.get("333") or 0) + (balance.get("382") or 0))
    add_check("liabilities_and_equity_equal_assets", balance.get("383"), balance.get("228"))
    add_check("gross_profit_equals_revenue_minus_cogs", income.get("066"), (income.get("001") or 0) - (income.get("035") or 0))
    add_check("operating_income_equals_gross_profit_minus_sga", income.get("129"), (income.get("066") or 0) - (income.get("067") or 0))
    add_check("net_income_equals_pretax_minus_tax", income.get("219"), (income.get("217") or 0) - (income.get("218") or 0))

    return checks


def parse_pdf(pdf_path: Path) -> dict[str, Any]:
    doc = fitz.open(pdf_path)
    page_texts = [page.get_text("text") for page in doc]
    normalized_name = normalize_text(pdf_path.name)
    raw_text_path = RAW_TEXT_DIR / f"{pdf_path.stem}.txt"
    raw_text_path.write_text(
        "\n\n".join(f"===== PAGE {i + 1} =====\n{text}" for i, text in enumerate(page_texts)),
        encoding="utf-8",
    )

    balance_rows = parse_statement_rows(page_texts[1], 2)
    income_rows = parse_statement_rows(page_texts[2], 3)
    metadata = parse_certificate_metadata(page_texts[0], normalized_name)
    fiscal_year = None
    if metadata.get("business_year_end"):
        fiscal_year = int(str(metadata["business_year_end"])[:4])

    return {
        "fiscal_year": fiscal_year,
        "metadata": metadata,
        "extraction": {
            "method": "pymupdf_embedded_text",
            "page_count": doc.page_count,
            "raw_text_path": str(raw_text_path.relative_to(ROOT)),
            "balance_sheet_row_count": len(balance_rows),
            "income_statement_row_count": len(income_rows),
        },
        "balance_sheet": rows_to_json(balance_rows),
        "income_statement": rows_to_json(income_rows),
        "metrics": build_metrics(balance_rows, income_rows),
        "validation_checks": validate_document(balance_rows, income_rows),
    }


def build_report(documents: list[dict[str, Any]]) -> str:
    lines = [
        "# Financial Statement Extraction Report",
        "",
        f"- Generated at: {datetime.now(timezone.utc).isoformat()}",
        "- Source: `data/source-documents/financial-statements/`",
        "- Method: PyMuPDF embedded text extraction. OCR was not used because the PDFs contain extractable text.",
        "- Output JSON: `data/extracted/financial-statements/financial_statements.json`",
        "- Raw text: `data/extracted/financial-statements/raw-text/`",
        "",
        "## Documents",
        "",
        "| Fiscal year | Source file | Balance rows | Income rows | Validation |",
        "| --- | --- | ---: | ---: | --- |",
    ]

    for doc in documents:
        checks = doc["validation_checks"]
        passed = sum(1 for check in checks if check["passed"])
        status = f"{passed}/{len(checks)} passed"
        lines.append(
            "| {year} | {file} | {balance} | {income} | {status} |".format(
                year=doc["fiscal_year"],
                file=doc["metadata"]["source_filename"],
                balance=doc["extraction"]["balance_sheet_row_count"],
                income=doc["extraction"]["income_statement_row_count"],
                status=status,
            )
        )

    failures = [
        (doc["fiscal_year"], check)
        for doc in documents
        for check in doc["validation_checks"]
        if not check["passed"]
    ]

    lines.extend(["", "## Validation Failures", ""])
    if not failures:
        lines.append("- None.")
    else:
        for year, check in failures:
            lines.append(
                f"- {year}: {check['name']} actual={check['actual']} expected={check['expected']}"
            )

    return "\n".join(lines) + "\n"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    RAW_TEXT_DIR.mkdir(parents=True, exist_ok=True)

    pdf_paths = sorted(SOURCE_DIR.glob("*.pdf"))
    documents = [parse_pdf(path) for path in pdf_paths]
    documents.sort(key=lambda doc: doc["fiscal_year"] or 0)

    payload = {
        "schema_version": 1,
        "currency": "KRW",
        "unit": "won",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_directory": str(SOURCE_DIR.relative_to(ROOT)),
        "extraction_method": "pymupdf_embedded_text",
        "documents": documents,
    }

    JSON_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT_PATH.write_text(build_report(documents), encoding="utf-8")

    print(f"Wrote {JSON_PATH}")
    print(f"Wrote {REPORT_PATH}")
    print(f"Wrote raw text files under {RAW_TEXT_DIR}")


if __name__ == "__main__":
    main()
