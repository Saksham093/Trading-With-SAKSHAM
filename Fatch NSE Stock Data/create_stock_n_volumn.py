import os
import pandas as pd

start_date = '2020-01-01'  # set start date...
stock_price = pd.DataFrame()
stock_volume = pd.DataFrame()

# Create lists to store data before creating DataFrames...
price_data = []
volume_data = []

for file in os.listdir('./Stocks'):
    df_ = pd.read_csv(os.path.join('./Stocks', file))
    symbol = file.replace('.csv', '')
    
    # Filter data based on the start_date...
    filtered_data = df_[df_['Date'] >= start_date][['Date', 'Open', 'Volume']]  # Filter data based on your needs...
    filtered_data = filtered_data.rename(columns={'Open': symbol, 'Volume': symbol})
    
    # Append data to lists...
    price_data.append(filtered_data[['Date', symbol]])
    volume_data.append(filtered_data[['Date', symbol]])

# Merge data from lists into DataFrames...
stock_price = pd.DataFrame(price_data[0])
stock_volume = pd.DataFrame(volume_data[0])

for i in range(1, len(price_data)):
    stock_price = pd.merge(stock_price, price_data[i], on='Date', how='outer')
    stock_volume = pd.merge(stock_volume, volume_data[i], on='Date', how='outer')

stock_price.set_index('Date', inplace=True)
stock_volume.set_index('Date', inplace=True)

# save result to xlsx file...
stock_price.to_excel('stock_price.xlsx')
stock_volume.to_excel('stock_volume.xlsx')