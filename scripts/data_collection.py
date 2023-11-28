import yfinance as yf

def download_stock_data(ticker, start_date, end_date):
    """
    Download historical stock data from Yahoo Finance.
    """
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

# Example usage
if __name__ == '__main__':
    data = download_stock_data('AAPL', '2020-01-01', '2021-01-01')
    data.to_csv('data/historical_data/AAPL.csv')
