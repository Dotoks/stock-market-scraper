import finnhub
import pandas as pd
import json
import tabulate
from ratelimiter import RateLimiter
from getAllStocks import *

allStocks = getAllStocks()
rateLimiter = RateLimiter(max_calls=1, period=2)
for stock in allStocks:
    with rateLimiter:
        stocksData = finnhub_client.company_basic_financials(stock, 'all')
        stocksData = json.dumps(stocksData, indent=4)
        with open("stocksData/" + stock + ".json", "w") as stocksDataOutFile:
            stocksDataOutFile.write(stocksData)


# with open ("stocksData/apple.json", "w") as AppleOutfile:
#     AppleOutfile.write(appleData)
# with open ("stocksData/snowflake.json", "w") as snowflakeOutfile:
#     snowflakeOutfile.write(snowflakeJson)cl