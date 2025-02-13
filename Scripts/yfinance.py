import yfinance as yf
import pandas as pd

#List of healthcare companies
healthcare_tickers = ["PFE", "JNJ", "UNH", "MRNA", "CVS"]

#Create an empty DataFrame to store historical data
historical_data = pd.DataFrame()

for ticker in healthcare_tickers:
    stock = yf.Ticker(ticker)
    
    #Fetch metadata(company info)
    info = stock.info

    #Fetch last 6 months of historical data
    hist_data = stock.history(period="6mo")
    hist_data.reset_index(inplace=True)
    
    #Add extra columns
    hist_data["Ticker"] = ticker
    hist_data["Stock Name"] = info.get('shortName', 'N/A')
    
    #Append to the main DataFrame
    historical_data = pd.concat([historical_data, hist_data], ignore_index=True)

#Save the full historical data to CSV
historical_data.to_csv("healthcare_stock_data.csv", index=False)

print("Historical stock data for the last 6 months saved to healthcare_stock_history.csv")










