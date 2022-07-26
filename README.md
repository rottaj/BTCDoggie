# Bitcoin Analysis



<h2> What I want: </h2>
<ul> 
  <li> Determine relationships between btc prices & data inputs.
  <li> Data Analytics to determine trends.
  <li> Implementing a neural network for future predictions.
</ul>

<h2> UPDATED: </h2>
<p> The cleaned datasets are hardly enough for a testing set. Maybe I can still learn from this... Or find something else.</p>

<h2> Data we will use: </h2>

<ul>
  <li> BTC Price Points ( By minute )
  <li> Twitter Sentiments ( if available )
  <li> S&P 500 Points ( By minute )
</ul>

<h2> Twitter Classifier: </h2>
<p>
  The classifier for twitter data currently is only based off of follower count.
  Things I will add:
  <ul>
    <li> Retweets
    <li> Likes
    <li> Verified Accounts
  </ul>
</p>

<h2> Dataset Sources: </h2>
<ul>
  <li> <a href="https://www.kaggle.com/datasets/prasoonkottarathil/btcinusd?resource=download&select=BTC-Daily.csv">Daily Bitcoin Price</a>
  <li> <a href="https://www.kaggle.com/datasets/prasoonkottarathil/btcinusd?resource=download&select=BTC-2021min.csv">2021 Bitcoin Price By Minute</a>
</ul>

<h2> Updated: </h2>
<p> Twitter doesn't allow full archive searches with standard api key so I'll use
this: <a href="https://www.kaggle.com/datasets/kaushiksuresh147/bitcoin-tweets">Kaggle Bitcoin Tweets (1Gb).</a> Seems like a lot of hacking... this might get ugly.
