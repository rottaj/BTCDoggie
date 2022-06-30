import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
  #df = pd.read_csv(r'./data/BTC-2021min.csv')  
  dfBtcDaily = pd.read_csv(r'./data/BTC-Daily.csv')
  dfBtcTweets = pd.read_csv(r'./data/BTC-Tweets.csv')
  #dfTweetsCleaned = pd.to_datetime(dfBtcTweets.date.astype(str), format="%Y-%m-%d %H:%M:%S").sort_values().to_numpy()
  dfBtcTweets.sort_values(by="date")
  print(dfBtcTweets.iloc[0], dfBtcTweets.iloc[-1])
  

  dfBtcDaily.set_index('date', inplace=True)
  dfBtcDaily[dfBtcTweets[0]:dfBtcTweets[-1]]


  '''
  plt.plot(df['date'].iloc[::-1], df['high'].iloc[::-1])
  #plt.xticks(np.arange(min(df['date']), max(df['date'])), rotation='vertical')
  locs, labels = plt.xticks();
  print(locs, labels)
  plt.ylabel("Highest Price")
  plt.xlabel("Date")
  plt.title("Bitcoin Price from Novemeber 2014 - March 2022")
  '''

  '''
  fig, (ax1, ax2) = plt.subplots(1, 2)
  fig.set_size_inches(10, 10)
  ax1.plot(dfBtcDaily['date'].iloc[::-1], dfBtcDaily['high'].iloc[::-1])
  ax1.set_ylabel("Highest Price")
  ax1.set_xlabel("Date")
  ax1.set_title("Bitcoin Price from Novemeber 2014 - March 2022")

  ax2.plot(
    pd.to_datetime(dfBtcTweets.date.astype(str),
    format="%Y-%m-%d %H:%M:%S").sort_values(), 
    dfBtcTweets.user_followers)
 
  figTwo, ax3 = plt.subplots()
  ax3.plot(dfBtcDaily['date'].iloc[::-1], dfBtcDaily['high'].iloc[::-1], color="blue")
  ax4 = ax3.twinx()
  ax4.plot(
    pd.to_datetime(dfBtcTweets.date.astype(str),
    format="%Y-%m-%d %H:%M:%S").sort_values(), 
    dfBtcTweets.user_followers,
    color="red")
  #print(pd.to_datetime(dfBtcTweets.date.astype(str),format="%Y-%m-%d %H:%M:%S").sort_values())
  #print(
  plt.show()
  '''
