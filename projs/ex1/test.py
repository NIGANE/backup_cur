import requests
import pandas

url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"
data = requests.get(url).json()
df = pandas.Dataframe(data)
