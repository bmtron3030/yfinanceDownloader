# yfinanceDownloader

Yahoo!, Y!Finance, and Yahoo! finance are registered trademarks of Yahoo, Inc.
This repository is not affiliated, endorsed, or vetted by Yahoo, Inc. It's an open-source tool that uses Yahoo's publicly available APIs, and is intended for research and educational purposes.
You should refer to Yahoo!'s terms of use for details on your rights to use the actual data downloaded. Remember - the Yahoo! finance API is intended for personal use only:

https://legal.yahoo.com/us/en/yahoo/terms/otos/index.html


The yfinance Downloader is a class that utilizes the open source _yfinance_ Python library to download historical data of any available stock symbol locally onto your machine. It provides methods to check if data is available for a stock symbol, retrieve symbol data as a DataFrame, and export it to CSV or Excel files. This can be useful for offline data access, creating backups of historical data for later use/analysis, or using another program to plot the data points.

### Requirements

- This Python class requires the _yfinance_ and _pandas_ Python modules. Use the ````pip install```` command to download each module individually or use the _requirements.txt_ found in this repository by running:

    ````pip install -r requirements.txt ````

### Installation

1. Make sure the latest version of Python is installed on your machine.
2. Download and save the _yfDownloader.py_ file to any local directory.
3. Download all dependencies listed in the Requirements section.

### Examples

1. In this example, the _downloadHistoricalDataOfSymbolfromyfinance_ is called to download the past 10 days of historical data in the frequency of days for the Apple stock (AAPL) in the form of a CSV.
````
from datetime import datetime, timedelta
import yfDownloader as yfd

# 1-day data
timeframe = '1D'

#Format the start and end dates
startdate = datetime.now() - timedelta(days=10) # Start date of the historical data (e.g., 10 days ago)
enddate = datetime.now() # End date of the historical data (e.g., current date)
start_date = startdate.strftime("%Y-%m-%d")
enddate = enddate.strftime("%Y-%m-%d")

yfdwnldr = yfd.yfDownloader()

def main():
 
    stocksymbol = 'AAPL'
    #Replace the following line with the desired file path on your local machine
    csvfolderpath = 'C:.../SymbolDirectory/AAPL'
    csvsavefilename = 'historicaldata'
    yfdwnldr.downloadHistoricalDataOfSymbolfromyfinance(
                                           stocksymbol,
                                           csvsavefilename,
                                           'CSV',
                                           folder=csvfolderpath,
                                           start = startdate, 
                                           end = enddate, 
                                           timeframefrequency=timeframe,
                                           dateformat='%Y/%m/%d'
                                           )
    
if __name__ == "__main__":
    main()
````


2. In this example, the _getSymbolDatafromyfinanceAsDataFrame_ is called in an attempt to get data from the stock symbol '1234' but will fail, exit out safely and notify the user when it has failed in its execution.
````
from datetime import datetime, timedelta
import yfDownloader as yfd

# 1-day data
timeframe = '1D'

#Format the start and end dates
startdate = datetime.now() - timedelta(days=10) # Start date of the historical data (e.g., 10 days ago)
enddate = datetime.now() # End date of the historical data (e.g., current date)
start_date = startdate.strftime("%Y-%m-%d")
enddate = enddate.strftime("%Y-%m-%d")

yfdwnldr = yfd.yfDownloader()

def main():
 
    stocksymbol = '1234'
    yfdwnldr.getSymbolDatafromyfinanceAsDataFrame(
                                           stocksymbol,
                                           start = startdate, 
                                           end = enddate, 
                                           timeframefrequency=timeframe
                                           )
    
if __name__ == "__main__":
    main()
````


3. In this example, the _downloadHistoricalDataOfMultipleSymbolsfromyfinance_ is called to iterate through an array of strings to download the historical data of multiple stock symbols fomr the past 90 days in the form of Excel files.
````
from datetime import datetime, timedelta
import yfDownloader as yfd

# 1-day data
timeframe = '1D'

#Format the start and end dates
startdate = datetime.now() - timedelta(days=90) # Start date of the historical data (e.g., 90 days ago)
enddate = datetime.now() # End date of the historical data (e.g., current date)
start_date = startdate.strftime("%Y-%m-%d")
enddate = enddate.strftime("%Y-%m-%d")

yfdwnldr = yfd.yfDownloader()

def main():
 
    stocksymbols = ['MSFT', 'CSCO', 'AMZN', 'IONQ', 'BOLT']
    #Replace the following lines with the desired file path and name of the save file on your local machine
    csvsavefilename = 'historicaldata'
    csvfolderpath = '.../SymbolDirectory/'
    yfdwnldr.downloadHistoricalDataOfMultipleSymbolsfromyfinance(
                                           stocksymbols,
                                           csvsavefilename,
                                           'EXCEL',
                                           csvfolderpath,
                                           startdate, 
                                           enddate, 
                                           timeframe,
                                           '%Y/%m/%d'
                                           )
    
if __name__ == "__main__":
    main()
````

