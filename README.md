# Monthly Stock Aggregation & Technical Indicators Pipeline

## Overview

This project processes daily stock price data and generates monthly aggregated summaries along with key technical indicators.
The objective is to provide a macro-level view of stock performance over a 2-year period.

The solution is implemented using Python and Pandas only, following clean, modular, and vectorized data engineering practices.

---

## Dataset

Input File:
- daily_stock_data.csv

Time Range:
- 2 years (daily frequency)

Stocks Covered (10):
- AAPL, AMD, AMZN, AVGO, CSCO, MSFT, NFLX, PEP, TMUS, TSLA

Input Schema:
date, volume, open, high, low, close, adjclose, ticker

---

## Functional Requirements Implemented

1. Monthly Aggregation (OHLC)

Daily data is resampled to monthly frequency using the following logic:

- Open  : First trading day of the month
- Close : Last trading day of the month
- High  : Maximum price during the month
- Low   : Minimum price during the month

2. Technical Indicators (Monthly Close Based)

The following indicators are calculated using monthly closing prices:

- SMA 10 : Simple Moving Average (10 months)
- SMA 20 : Simple Moving Average (20 months)
- EMA 10 : Exponential Moving Average (10 months)
- EMA 20 : Exponential Moving Average (20 months)

Note:
Initial SMA values contain NaN due to insufficient historical data.
This behavior is mathematically correct and expected.

3. Output Partitioning

- 10 separate CSV files are generated
- Each file contains exactly 24 rows (2 years × 12 months)
- File naming convention:
  result_<TICKER>.csv

---

## Project Structure

project/
│── stock_aggregator.py   (Core data processing)

│── validate.py            (Output validation & checks)

│── summary_report.py     (Macro-level summary)

│── main.py 

│── daily_stock_data.csv           (Input dataset)

│── result_AAPL.csv
│── result_AMD.csv
│── ...
│── summary_report.csv
│── README.md

---

## Scripts Description

stock_aggregator.py
- Loads and preprocesses daily data
- Performs monthly OHLC aggregation
- Computes SMA and EMA indicators
- Writes one CSV file per ticker

validate.py
- Ensures each output file has exactly 24 rows
- Verifies required columns
- Confirms expected NaN behavior in SMA columns
- Checks EMA columns for unexpected NaNs

summary_report.py
- Produces a macro-level summary CSV
- Includes:
  - Start and end dates
  - Minimum, maximum, and average close prices
  - Latest EMA-20 value per ticker

main.py 
- Executes the full pipeline in sequence:
  1. Monthly aggregation
  2. Validation
  3. Summary report generation

---

## How to Run

Run full pipeline:
python main.py

Run scripts individually:
python monthly_stock_aggregation.py
python validate_results.py
python generate_summary_report.py

---

## Assumptions Made

- Dataset contains valid trading data for each month
- Monthly aggregation uses calendar month-end
- Technical indicators are calculated only on monthly closing prices
- Initial NaN values in SMA columns are expected due to rolling window size

---

## Tools & Libraries Used

- Python 3
- Pandas

---

## Key Highlights

- Correct OHLC aggregation logic
- Vectorized Pandas operations
- Clean and modular code structure
- Output validation included
- Suitable for production-style data pipelines

---

## Submission Notes

- Repository is public
- All assumptions are clearly documented
- Solution strictly follows assignment constraints
