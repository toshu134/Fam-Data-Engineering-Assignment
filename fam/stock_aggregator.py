import pandas as pd



# 1: Load the dataset

def load_data(file_path):
    """
    Reads the CSV file and returns a DataFrame
    """
    df = pd.read_csv(file_path)
    return df



# 2: Preprocess data

def preprocess_data(df):
    """
    - Converts date column to datetime
    - Sorts by ticker and date
    - Sets date as index
    """
    df['date'] = pd.to_datetime(df['date'], dayfirst=True)
    df = df.sort_values(by=['ticker', 'date'])
    df = df.set_index('date')
    return df



# 3: Monthly OHLC aggregation

def monthly_ohlc(df):
    """
    Resamples daily data to monthly data using OHLC rules
    """
    monthly_df = df.resample('M').agg({
        'open': 'first',
        'high': 'max',
        'low': 'min',
        'close': 'last'
    })
    return monthly_df



# 4: Add technical indicators

def add_technical_indicators(monthly_df):
    """
    Adds SMA and EMA indicators based on monthly closing prices
    """
    # Simple Moving Averages
    monthly_df['SMA_10'] = monthly_df['close'].rolling(window=10).mean()
    monthly_df['SMA_20'] = monthly_df['close'].rolling(window=20).mean()

    # Exponential Moving Averages
    monthly_df['EMA_10'] = monthly_df['close'].ewm(span=10, adjust=False).mean()
    monthly_df['EMA_20'] = monthly_df['close'].ewm(span=20, adjust=False).mean()

    return monthly_df



# 5: Process a single ticker

def process_single_ticker(df, ticker):
    """
    Filters data for one ticker and applies all transformations
    """
    ticker_df = df[df['ticker'] == ticker]
    monthly_df = monthly_ohlc(ticker_df)
    monthly_df = add_technical_indicators(monthly_df)
    return monthly_df



# 6: Write output CSV

def write_output(df, ticker):
    """
    Writes the processed data to CSV
    """
    output_file = f"result_{ticker}.csv"
    df.to_csv(output_file)



# 7: Main pipeline

def main():
    input_file = "C://Users//Arnav Singh//Downloads//output_file.csv"   # 🔁 change if filename is different

    df = load_data(input_file)
    df = preprocess_data(df)

    tickers = df['ticker'].unique()

    for ticker in tickers:
        monthly_data = process_single_ticker(df, ticker)
        write_output(monthly_data, ticker)

    print("✅ Monthly aggregation completed for all tickers!")


if __name__ == "__main__":
    main()
