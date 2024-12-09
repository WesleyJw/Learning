import pandas as pd
import yfinance as yf

# Criptos to Download

# Bitcoin - BTC-USD
# Cardano - ADA-USD
# Etherium - ETH-USD
# Theter - USDT-USD
# BNB - BNB-USD
# XRP - XRP-USD
# Dogecoin - DOGE-USD

# To search set this parameters

Tickets = ["BTC-USD", "ADA-USD", "ETH-USD", "USDT-USD", "BNB-USD", "XRP-USD", "DOGE-USD"]
start_date = "2016-01-01"
end_date = "2024-12-03"

# Get data

df = yf.download(Tickets, start=start_date, end=end_date)

print(df.head())
print(df.tail())
print(df.shape)
