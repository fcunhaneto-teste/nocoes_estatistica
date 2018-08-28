import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('/home/francisco/Projects/Pycharm/nocoes_estatistica/files/cap01/questionario.csv')
df_m = df[df.Sexo != 'F']

desc = df_m.describe()
s = df_m['Alt']
print(s.describe())

plt.boxplot(s)
plt.show()
plt.close()
