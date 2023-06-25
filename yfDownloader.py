import yfinance as yf
import pandas as pd
from pandas import DataFrame as df
import time
import os
from datetime import datetime, timedelta

class yfDownloader():
    
    #Tests if the yfinance API is able to get any information from a given stock symbol.
    #Takes a stock symbol as a string as input.
    #Returns a boolean value (True if the API has data on the symbol, False otherwise).
    #Used internally by other functions.
    def isSymbolDataAvailableFromyfinance(self, symbol):
        dataExists = False
        try:
            yf.Ticker(symbol)
            dataExists = True
        except:
            dataExists = False
        return dataExists

    #Gets data from the yfinance API for a given stock symbol if Yahoo Finance has any data associated with the symbol.
    #Takes a stock symbol as a string, a timeframe sequence as a string, a start date as a datetime object,
    #an end date as a datetime object, and a date format as a string as input.
    #Returns a Data Frame of the symbol data if the API has data on it, None otherwise.
    def getSymbolDatafromyfinanceAsDataFrame(self, 
                                             symbol,
                                             start=(datetime.now() - timedelta(days=90)), 
                                             end=datetime.now(),
                                             timeframefrequency='1D'
                                             ):
        canGetDataFromyfinance = self.isSymbolDataAvailableFromyfinance(symbol)
        if canGetDataFromyfinance == True:
            print('Getting data for '+symbol)
            data = yf.download(symbol, start=start, end=end, interval=timeframefrequency)
            return data
        elif canGetDataFromyfinance == False:
            print('No data available from yfinance for '+symbol)
            return None
         
    #Saves a Data Frame of any given stock symbol from the yfinance API to a .csv file.
    #Takes a Data Frame of a given stock symbol, what name to save the file as in
    #the form of a string, the symbol as a string, what name of the folder to save
    #the file into (does NOT need to already exist, this function will create a new folder
    #if it does not exist) as a string, and the symbol itself as a string. "folder" and "symbol"
    #are both optional parameters, but it is recommended to specify them based on your preference.
    #Does not return anything.
    def exportSymbolDataToCSV(self, 
                              dataframeofsymbol, 
                              savefileas, 
                              savedir
                              ):
        df = pd.DataFrame(dataframeofsymbol)
        if not os.path.exists(savedir):
            os.makedirs(savedir)
            df.to_csv(savedir+'/'+savefileas+'.csv', index=False)
        else:
            df.to_csv(savedir+'/'+savefileas+'.csv', index=False)

    #Saves a Data Frame of any given stock symbol from the yfinance API to a .xlsx file.
    #Takes a Data Frame of a given stock symbol, what name to save the file as ins
    #the form of a string, the symbol as a string, what name of the folder to save
    #the file into (does NOT need to already exist, this function will create a new folder
    #if it does not exist) as a string, and the symbol itself as a string. "folder" and "symbol"
    #are both optional parameters, but it is recommended to specify them based on your preference.
    #Does not return anything.
    def exportSymbolDataToExcel(self, 
                                dataframeofsymbol, 
                                savefileas, 
                                folder = '', 
                                symbol=''):   
        df = pd.DataFrame(dataframeofsymbol)
        if folder == '':
            folder = 'symboldata' +'/'+symbol+'/'
        else:
            folder = folder+'/'
        fullsavepath = folder+savefileas+symbol+'.xlsx'
        #xlsxwriter = pd.ExcelWriter(fullsavepath)
        if not os.path.exists(folder):
            os.makedirs(folder)
            df.to_excel(fullsavepath, 'Main')
        else:
            df.to_excel(fullsavepath, 'Main')
        
    #Directly downloads any stock symbol's historical data as a .csv/.xlsx file from the yfinance API for any given duration of time in days.
    #Takes a stock symbol as a string, the timeframe frequency as a string, a start date as a datetime object, an
    #end date as a datetime object, the format to save the dates as in the form of a string,the name of what the file should 
    #be named as in the form of a string, the format to save the file as in the form of a string, and the name of the folder
    #to save the file into (does NOT need to already exist, this function will create a new folder if needed) as input. 
    #Does not return anything.
    def downloadHistoricalDataOfSymbolfromyfinance(self, 
                                                   symbol, 
                                                   savefileas, 
                                                   savefileasformat, 
                                                   folder = 'symboldata', 
                                                   start=(datetime.now() - timedelta(days=90)), 
                                                   end=datetime.now(),
                                                   timeframefrequency='1D', 
                                                   dateformat='%Y/%m/%d'
                                                   ):
        try:
            dfHistoricalData = self.getSymbolDatafromyfinanceAsDataFrame(symbol, start, end, timeframefrequency)
            fileformat = savefileasformat.lower()
            if fileformat == 'csv':
                self.exportSymbolDataToCSV(dfHistoricalData, savefileas, folder, symbol)
                print('{} successfully downloaded to {}'.format((savefileas+symbol+'.csv'), folder))
            elif fileformat == 'xlsx' or fileformat == 'excel':
                self.exportSymbolDataToExcel(dfHistoricalData, savefileas, folder, symbol)
                print('{} successfully downloaded to {}'.format((savefileas+symbol+'.xlsx'), folder))
            else:
                print('Unable to download historical data for symbol {} to {} as {}: unsupported file format detected'.format(symbol, folder, fileformat))
        except Exception as e:
                print('Unable to download historical data for symbol {} to {} : {}'.format(symbol, folder, e))
        
    #Directly downloads multiple stock symbols' historical data as .csv/.xlsx files from the yfinance API for any given duration of time in days.
    #Takes a stock a list of symbols as an array or list of strings, the timeframe frequency as a string, a start date as a datetime object, an
    #end date as a datetime object, the format to save the dates as in the form of a string,the name of what the file should 
    #be named as in the form of a string, the format to save the file as in the form of a string, and the name of the folder 
    #to save the file into (does NOT need to already exist, this function will create a new folder if needed) as input. 
    #Does not return anything.
    def downloadHistoricalDataOfMultipleSymbolsfromyfinance(self, 
                                                            symbollist, 
                                                            savefileas, 
                                                            savefileasformat, 
                                                            folder, 
                                                            start=(datetime.now() - timedelta(days=90)), 
                                                            end=datetime.now(),
                                                            timeframefrequency='1D', 
                                                            dateformat='%Y/%m/%d'
                                                            ):
        for symbol in symbollist:
            self.downloadHistoricalDataOfSymbolfromyfinance(symbol, savefileas, savefileasformat, folder, start, end, timeframefrequency, dateformat)