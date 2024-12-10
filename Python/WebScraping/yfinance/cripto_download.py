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

data = pd.DataFrame()
for Ticket in Tickets:
    print(f"Processing data for ticket: {Ticket}")
    df = yf.download(Ticket, start=start_date, end=end_date)
    df.columns = df.columns.get_level_values('Price')
    df = df.reset_index()
    df["Ticket"] = Ticket
    
    data = pd.concat([data, df])

data.to_csv("criptocurrencies_history_data.csv", index=False)


print(data.head())
print(data.tail())
print(data.shape)