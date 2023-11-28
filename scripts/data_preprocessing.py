import pandas as pd

def preprocess_data(file_path):
    """
    Preprocess the stock data.
    """
    df = pd.read_csv(file_path, index_col='Date', parse_dates=True)
    df['Return'] = df['Close'].pct_change()
    df.dropna(inplace=True)
    return df

# Example usage
if __name__ == '__main__':
    df = preprocess_data('data/historical_data/AAPL.csv')
    df.to_csv('data/processed_data/AAPL_processed.csv')
