# Web Automation Testing Tool

A simple Python-based automation testing tool that checks whether a website loads correctly and verifies that links are not broken.

## Features

- Automated webpage loading test
- Broken link detection
- HTML test report generation
- Command-line tool for testing any website

## Tech Stack

- Python
- Selenium
- PyTest
- Requests

## Project Structure
web_testing_tool/
│
├── tests/                 # Automated test cases
│   ├── test_page_load.py  # Webpage loading test
│   └── test_links.py      # Broken link validation
│
├── reports/               # Generated HTML test reports
│
├── conftest.py            # PyTest configuration and fixtures
├── main.py                # CLI entry point for running tests
├── requirements.txt       # Project dependencies
└── README.md


