# Financial Statement Extraction Report

- Generated at: 2026-06-15T02:09:52.322767+00:00
- Source: `data/source-documents/financial-statements/`
- Method: PyMuPDF embedded text extraction. OCR was not used because the PDFs contain extractable text.
- Output JSON: `data/extracted/financial-statements/financial_statements.json`
- Raw text: `data/extracted/financial-statements/raw-text/`

## Documents

| Fiscal year | Source file | Balance rows | Income rows | Validation |
| --- | --- | ---: | ---: | --- |
| 2018 | 페이지콜 표준재무제표 201812.pdf | 41 | 45 | 5/5 passed |
| 2019 | 페이지콜 표준재무제표 201912.pdf | 46 | 51 | 5/5 passed |
| 2020 | 페이지콜 표준재무제표 202012.pdf | 47 | 48 | 5/5 passed |
| 2021 | 페이지콜 표준재무제표 202112.pdf | 52 | 48 | 5/5 passed |
| 2022 | 페이지콜 표준재무제표 202212.pdf | 49 | 49 | 5/5 passed |
| 2023 | 페이지콜 표준재무제표 202312.pdf | 56 | 46 | 5/5 passed |
| 2024 | 페이지콜 표준재무제표 202412.pdf | 54 | 44 | 5/5 passed |
| 2025 | 페이지콜 표준재무제표 202512.pdf | 50 | 44 | 5/5 passed |

## Validation Failures

- None.
