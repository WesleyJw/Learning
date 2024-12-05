import pandas as pd
import yfinance as yf

# To search set this parameters

Ticket = "BTC-USD"
start_date = "2016-01-01"
end_date = "2024-12-03"

# Get data

df = yf.download(Ticket, start=start_date, end=end_date)

print(df.head())
print(df.tail())
