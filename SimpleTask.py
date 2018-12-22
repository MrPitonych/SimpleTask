import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data1.csv', usecols=['time','gFx', 'gFy', 'gFz'], sep=';', low_memory=False)
dictionary = {';':',', ',':'.'}
df.replace(dictionary, regex=True, inplace=True)
df=df.astype(float)

df.plot(x='time')
plt.show()