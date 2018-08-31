import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandasutils.pandasutils import frequency, frequency_by_natural_order, \
    frequency_by_buckets



pd.set_option('precision', 2)
pd.options.display.float_format = '{:,.2f}'.format

df = pd.read_csv('/home/francisco/Projects/Pycharm/nocoes_estatistica/files/cap01/ex24/cancer.csv')

df_1 = df[df.Grupo == 1]
df_2 = df[df.Grupo == 2]
df_3 = df[df.Grupo == 3]
df_4 = df[df.Grupo == 4]

s_1 = df_1['Idade']
s_2 = df_2['Idade']
s_3 = df_3['Idade']
s_4 = df_4['Idade']
s_1d = s_1.describe()
print(s_2.describe())
print(s_3.describe())
print(s_4.describe())

font_1 = {'family': 'serif',
        'color':  'darkred',
        }

fig = plt.figure(figsize=(10, 8))
plt.boxplot([s_1, s_2, s_3, s_4])
plt.xlabel('Grupo')
plt.ylabel('Idade')
plt.grid()


plt.text(1, s_1d['50%'], str(s_1d['50%']), fontdict=font_1)
plt.text(1, s_1d['25%'], str(s_1d['25%']))
plt.text(1, s_1d['75%'], str(s_1d['75%']))
fig.savefig('grupo_idade.png')
plt.close()
