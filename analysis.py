import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
  #df = pd.read_csv(r'./data/BTC-2021min.csv')  
  df = pd.read_csv(r'./data/BTC-Daily.csv')
  print(df)
  plt.plot(df['date'].iloc[::-1], df['high'].iloc[::-1])
  #plt.xticks(np.arange(min(df['date']), max(df['date'])), rotation='vertical')
  locs, labels = plt.xticks();
  print(locs, labels)
  plt.ylabel("Highest Price")
  plt.xlabel("Date")
  plt.title("Bitcoin Price from Novemeber 2014 - March 2022")
  plt.show()

