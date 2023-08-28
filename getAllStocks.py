import finnhub
import pandas as pd
import json

finnhub_client = finnhub.Client(api_key="cii36ghr01quio6uhf90cii36ghr01quio6uhf9g")

def getAllStocks():
    allStocks = finnhub_client.stock_symbols('US')
    stockSymbol = ""
    for stock in allStocks:
        stockSymbol = stockSymbol + ", " + stock["displaySymbol"]
    stockSymbol = stockSymbol[2:]
    return stockSymbol.split(',')