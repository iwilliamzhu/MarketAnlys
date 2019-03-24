import pandas as pd
import numpy as np

df = pd.read_csv("A.csv")

df['5-MA'] = df['close'].rolling(5).mean()
df.loc[df['index'] == 11, '12-MA'] = df['close'].rolling(12).mean()
df.loc[df['index'] == 25, '26-MA'] = df['close'].rolling(26).mean()

df['12-EMA'] = np.where(df['index'] < 12, df['close'].rolling(12).mean(), pd.Series.ewm(df['close'], span=12, adjust=False).mean())
df['26-EMA'] = np.where(df['index'] < 26, df['close'].rolling(26).mean(), pd.Series.ewm(df['close'], span=26, adjust=False).mean())
df['MACD'] = df['26-EMA'] - df['12-EMA']

print(df.head())
df.to_csv("A.csv")