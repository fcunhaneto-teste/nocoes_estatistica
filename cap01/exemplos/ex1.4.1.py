import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('/home/francisco/Projects/Pycharm/nocoes_estatistica/files/cap01/questionario.csv')
s = df['Peso']

plt.figure(figsize=(10,8))
plt.boxplot(s)
plt.show()
