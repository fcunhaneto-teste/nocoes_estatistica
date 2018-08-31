import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandasutils.pandasutils import frequency, frequency_by_natural_order, \
    frequency_by_buckets



pd.set_option('precision', 2)
pd.options.display.float_format = '{:,.2f}'.format

df = pd.read_csv('/home/francisco/Projects/Pycharm/nocoes_estatistica/files/cap01/ex24/cancer.csv')
with open('ex24.txt', 'w') as f:
    df.to_string(f)

# Diagnostico

s_diagnostico = pd.Series(df['Grupo'])
freq_d = frequency_by_natural_order(df, 'Grupo')
plt.bar([1, 2, 3, 4], freq_d['tot'])
plt.savefig('diagnostico.png')
plt.close()

# Glicose
plt.figure(figsize=(12,8))
freq_gl = frequency_by_buckets(df, 'GL', 20, 50, 300)
s_gl = pd.Series(freq_gl['GL'])

x = ['[50,70)', '[70,90)', '[90,110)', '[110,130)', '[130,150)',
     '[150,170)', '[170,190)', '[190,210)', '[210,230)', '[230,250)',
     '[250,270)', '[270,290)', '[290,310)']

plt.bar(x, s_gl)
plt.savefig('glicose.png')
plt.close()

# Idade
plt.figure(figsize=(10,8))
# print(df['Idade'].max())
# print(df['Idade'].min())
# print(df['Idade'].describe())
df_idade = frequency_by_buckets(df, 'Idade', 10, 5, 105)
percent = df_idade['freq'] * 100
x = ['[5, 15)', '[15, 25)', '[25, 35)', '[35, 45)', '[45, 55)', '[55, 65)', '[65, 75)', '[75, 85)', '[85, 95)', '[95, 105)']
plt.bar(x, percent)
plt.savefig('idade_hist.png')

plt.figure(figsize=(4,4))
s = df['Idade']
plt.boxplot(s)
plt.savefig('idade_boxplot.png')
plt.close()