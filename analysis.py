import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

if __name__ == "__main__":
  dfBtcDaily = pd.read_csv(r'./data/BTC-Daily.csv')
  dfBtcTweets = pd.read_csv(r'./data/BTC-Tweets.csv')
  #dfTweetsCleaned = pd.to_datetime(dfBtcTweets.date.astype(str), format="%Y-%m-%d %H:%M:%S").sort_values().to_numpy()

 
  z1 = dfBtcDaily.index[dfBtcDaily.date == "2021-07-01 00:00:00"].astype('int')
  dfBtcDailyCleaned = dfBtcDaily[0: 243] # This is hacky, but works. Idk Index64Int is.
  print(dfBtcDailyCleaned)

  # Starting w/ user followers, will add more later.

  
  print(len(dfBtcTweets['date']))
  dfBtcTweets['user_followers'].fillna(0.0)
  testDf = dfBtcTweets['user_followers'].astype(float).groupby(
    pd.to_datetime(dfBtcTweets['date'], format="%Y-%m-%d %H:%M:%S").dt.to_period('D')).sum() 
  
  print(testDf)
  print(testDf.index)
  print(testDf.values)
  print(len(testDf))

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
  '''
  ax4.plot(
    pd.to_datetime(dfBtcTweets.date.astype(str)),
    #format="%Y-%m-%d %H:%M:%S").sort_values(), 
    dfBtcTweets.user_followers,
    color="red")
  ax4.grid(None)

  '''
  ax4.plot(
    testDf.index.astype(str),
    testDf.values,
    color='red'
  )

  plt.show()

