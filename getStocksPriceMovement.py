import finnhub
import pandas as pd
import json
import tabulate
from getAllStocks import *

allStocks = getAllStocks()
for stock in allStocks:
    stocksData = finnhub_client.company_basic_financials(stock, 'all')
    stocksData = json.dumps(stocksData, indent=4)
    with open("stocksData/" + stock + ".json", "w") as stocksDataOutFile:
        stocksDataOutFile.write(stocksData)



# with open ("stocksData/apple.json", "w") as AppleOutfile:
#     AppleOutfile.write(appleData)
# with open ("stocksData/snowflake.json", "w") as snowflakeOutfile:
#     snowflakeOutfile.write(snowflakeJson)