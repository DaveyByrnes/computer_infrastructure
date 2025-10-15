
# copy code from problem sheet here
#!/usr/bin/env python3

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import os

now = datetime.now()

timestamp = now.strftime("%Y%m%d-%H%M%S")
print(timestamp)

file = f"data/{timestamp}.csv" # creates csv file with timestamp name

# create tickers

tickers = ["META", "AAPL", "AMZN", "NFLX", "GOOG"]

data = yf.download(tickers, interval="1h", period="5d")

timestamp = now.strftime("%Y%m%d-%H%M%S")
file = f"data/{timestamp}.csv" # creates csv file with timestamp name

tickers = ["META", "AAPL", "AMZN", "NFLX", "GOOG"]

data = yf.download(tickers, interval="1h", period="5d")

data.to_csv(file)

print(f"The data has been saved")

def plot_data():

    data_files = [f for f in os.listdir("data") if f.endswith(".csv")]
    if not data_files:
        print("No data files found in the 'data' directory.")
        return
    
    # sort files to get the latest one
    data_files.sort(reverse=True)
    latest_file = data_files[0]
    file_path = os.path.join("data", latest_file)

    # read the latest data file
    df = pd.read_csv(file_path, header=[0,1], index_col=0)

    # extract closing data
    close_data = df['Close']

    # plot closing prices
    plt.figure(figsize=(10, 6))
    for ticker in close_data.columns:
        plt.plot(close_data.index, close_data[ticker], label=ticker)
    plt.xlabel('Time')
    plt.ylabel('Closing Price')
    plt.title(f"Stock Closing Prices - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    plt.legend()
    plt.grid(True)

    # timestamp filename
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    file_path = f"plots/stock_prices_{timestamp}.png"
    os.makedirs("plots", exist_ok=True)
    plt.savefig(file_path)
    print(f"Plot saved to {file_path}")

# run function
plot_data()