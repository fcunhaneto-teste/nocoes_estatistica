import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('../files/cap01/questionario_aspas.csv')
df_m = df[df.Sexo != 'F']

desc = df_m.describe()
s = df_m['Alt']
print(s.describe())

plt.boxplot(s)
plt.show()
plt.close()

