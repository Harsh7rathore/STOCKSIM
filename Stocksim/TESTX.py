# import pandas as pd
# import requests
# import datetime 
# import os
# import yfinance as yf
from datetime import *
# # # # # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key

# # # tradables = {"ASBL":"AAPL", "COMO":"NVDA", "COSA":"MSFT", "ENEC":"AXP", "HITR":"AMZN", "HOME":"KO", "INPA":"LLY", "REMT":"INTC", "RITM":"WMT", "SHFA":"JPM", "SHIF":"IBM", "THRE":"XOM", "UNRE":"UNH", "UNPO":"ORCL"}
# # # for i in tradables:
# # #     url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol={}&apikey=A97HEVFBKYFWOQWM'.format(tradables[i])
# # #     pd.DataFrame(requests.get(url).json()["Time Series (Daily)"]).T.to_csv("Stocksim/plot/data/{}.csv".format(i),header=False)
# sdate = "2023-10-24"
# x = None
# name = "ASBL"
# dnrows=10
# with open("Stocksim/plot/data/{}.csv".format(name), "r") as f:
#     for count, l in enumerate(f): #count number of iterations ie lines moved
#         if str(l).startswith(sdate): # if line starts with sdate
#             print(count, l)
#             df = pd.read_csv("Stocksim/plot/data/{}.csv".format(name),header=None,index_col=0,skiprows=count,nrows=dnrows) #skip number of lines equal to count and read dnrows lines
#             df.index.name=None # removing index name
#             df.columns = ["O","H","L","C","V"] # renaming index columns to simpler ones
#             df["D"] = df["C"]-df["O"] # change
#             df["D%"] = df["D"]/df["O"]*100 # perc change
#             break
# print(count)
# print(df)
# # #  3 days change
# print()
# dx = pd.read_csv("Stocksim/plot/data/{}.csv".format("ASBL"),header=None,index_col=0,skiprows=count+dnrows,nrows=3)
# print(dx)
# # dx.columns = ["Open","High","Low","Close","Volume"]
# # print(dx)
# # df = pd.concat([df,dx],axis=0).iloc[3:]
# # print(df)
# # url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol={}&apikey=A97HEVFBKYFWOQWM'.format("MSFT")
# # pd.DataFrame(requests.get(url).json()["Time Series (Daily)"]).T.to_csv("Stocksim/plot/data/{}.csv".format("MSFT"),header=False)
# # msft = yf.Ticker("MSFT")
# # x = msft.history(period="max")
# # pd.DataFrame(x).loc[:,"Open":"Volume"].to_csv("Stocksim/plot/data/{}.csv".format("MSFT"),header=False)
# import customtkinter as ctk
# import matplotlib.pyplot as plt
# from plot.data import tradable

# tr = tradable("ASBL","2023-02-01", 10)
# up = tr.data[tr.data["D%"]>0]
# down = tr.data[tr.data["D%"]<0]

# print(up)
# print(down)

# col1 = 'red'
# col2 = 'green'

# plt.bar(up.index, up.Close-up.Open, bottom=up.Open, color=col1) 
# plt.bar(up.index, up.High-up.Close,width=0.2, bottom=up.Close, color=col1) 
# plt.bar(up.index, up.Low-up.Open,width=0.2, bottom=up.Open, color=col1) 

# plt.bar(down.index, down.Close-down.Open, bottom=down.Open, color=col2) 
# plt.bar(down.index, down.High-down.Open, width=0.2, bottom=down.Open, color=col2) 
# plt.bar(down.index, down.Low-down.Close, width=0.2,bottom=down.Close, color=col2)

# plt.show()

datex = "2023-02-01"
def next_day(date):
    date = datetime.strptime(date, "%Y-%m-%d")
    date = date + timedelta(days=1)
    return str(date.strftime("%Y-%m-%d"))
print(next_day(datex))