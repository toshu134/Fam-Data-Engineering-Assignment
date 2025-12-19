import pandas as pd
import os


TICKERS = ["AAPL", "AMD", "AMZN", "AVGO", "CSCO",
           "MSFT", "NFLX", "PEP", "TMUS", "TSLA"]

EXPECTED_ROWS = 24

REQUIRED_COLUMNS = [
    "open", "high", "low", "close",
    "SMA_10", "SMA_20", "EMA_10", "EMA_20"
]


def validate_file(file_name, ticker):
    print(f"\n Validating {file_name}")

    df = pd.read_csv(file_name)

    # 1. Check row count
    if len(df) != EXPECTED_ROWS:
        print(f"Row count error for {ticker}: {len(df)} rows found")
    else:
        print("Row count correct (24 rows)")

    # 2. Check required columns
    missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_cols:
        print(f"Missing columns: {missing_cols}")
    else:
        print("All required columns present")

    # 3. Check SMA NaNs (expected behavior)
    sma10_nan = df["SMA_10"].isna().sum()
    sma20_nan = df["SMA_20"].isna().sum()

    print(f"SMA_10 NaN count: {sma10_nan} (expected: 9)")
    print(f"SMA_20 NaN count: {sma20_nan} (expected: 19)")

    # 4. Check EMA NaNs (should be zero)
    ema10_nan = df["EMA_10"].isna().sum()
    ema20_nan = df["EMA_20"].isna().sum()

    if ema10_nan == 0 and ema20_nan == 0:
        print("EMA columns have no NaNs")
    else:
        print("Unexpected NaNs in EMA columns")


def main():
    print("Starting validation of result files...")

    for ticker in TICKERS:
        file_name = f"result_{ticker}.csv"

        if not os.path.exists(file_name):
            print(f"\n File not found: {file_name}")
            continue

        validate_file(file_name, ticker)

    print("\nValidation completed.")


if __name__ == "__main__":
    main()
