import pandas as pd
import os


TICKERS = ["AAPL", "AMD", "AMZN", "AVGO", "CSCO",
           "MSFT", "NFLX", "PEP", "TMUS", "TSLA"]

SUMMARY_FILE = "summary_report.csv"


def summarize_ticker(file_name, ticker):
    df = pd.read_csv(file_name)

    summary = {
        "ticker": ticker,
        "start_date": df["date"].iloc[0],
        "end_date": df["date"].iloc[-1],
        "months": len(df),
        "min_close": df["close"].min(),
        "max_close": df["close"].max(),
        "avg_close": round(df["close"].mean(), 2),
        "latest_EMA_20": round(df["EMA_20"].iloc[-1], 2)
    }

    return summary


def main():
    print(" Generating summary report...")

    summary_data = []

    for ticker in TICKERS:
        file_name = f"result_{ticker}.csv"

        if not os.path.exists(file_name):
            print(f"Missing file: {file_name}")
            continue

        summary = summarize_ticker(file_name, ticker)
        summary_data.append(summary)

    summary_df = pd.DataFrame(summary_data)
    summary_df.to_csv(SUMMARY_FILE, index=False)

    print(f" Summary report generated: {SUMMARY_FILE}")



if __name__ == "__main__":
    main()
