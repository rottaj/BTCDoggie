import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
  #df = pd.read_csv(r'./data/BTC-2021min.csv')  
  dfBtcDaily = pd.read_csv(r'./data/BTC-Daily.csv')
  dfBtcTweets = pd.read_csv(r'./data/BTC-Tweets.csv')
  #dfTweetsCleaned = pd.to_datetime(dfBtcTweets.date.astype(str), format="%Y-%m-%d %H:%M:%S").sort_values().to_numpy()

 
  z1 = dfBtcDaily.index[dfBtcDaily.date == "2021-07-01 00:00:00"].astype('int')
  dfBtcDailyCleaned = dfBtcDaily[0: 243] # This is hacky, but works. Idk Index64Int is.
  print(dfBtcDailyCleaned)


  fig, (ax1, ax2) = plt.subplots(1, 2)
  fig.set_size_inches(10, 10)
  ax1.plot(dfBtcDailyCleaned['date'].iloc[::-1], dfBtcDailyCleaned['high'].iloc[::-1])
  ax1.set_ylabel("Highest Price")
  ax1.set_xlabel("Date")
  fig.suptitle("Bitcoin Price from July 2021 - March 2022")

  ax2.plot(
    pd.to_datetime(dfBtcTweets.date.astype(str),
    format="%Y-%m-%d %H:%M:%S").sort_values(), 
    dfBtcTweets.user_followers)
 
  figTwo, ax3 = plt.subplots()
  ax3.plot(dfBtcDailyCleaned['date'].iloc[::-1], dfBtcDailyCleaned['high'].iloc[::-1], color="blue")
  ax4 = ax3.twinx()
  ax4.plot(
    pd.to_datetime(dfBtcTweets.date.astype(str)),
    #format="%Y-%m-%d %H:%M:%S").sort_values(), 
    dfBtcTweets.user_followers,
    color="red")
  ax4.grid(None)
  plt.show()
