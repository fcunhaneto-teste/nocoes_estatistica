import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('../files/cap01/questionario_aspas.csv')
s = df['Peso']

plt.figure(figsize=(10,8))
plt.boxplot(s)
plt.show()
