import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandasutils.pandasutils import frequency, frequency_by_natural_order, \
    frequency_by_buckets



pd.set_option('precision', 2)
pd.options.display.float_format = '{:,.2f}'.format

df = pd.read_csv('../files/cap01/questionario.csv')
print(df.describe())

age = frequency_by_natural_order(df, 'Idade')
percent = age['freq'] * 100

plt.figure(figsize=(6,4))
plt.bar(percent.index, percent)
plt.title('Distribuição de Idades')
plt.xlabel('Idade')
plt.ylabel('Frequencia')
plt.xticks(percent.index) # obriga a mostrar todos os números no eixo x
plt.savefig('idade.png')
plt.close()

toler = frequency(df, 'Toler')
percent = toler['freq'] * 100

plt.figure(figsize=(5,5))
plt.title('Tolerância a Cigarro')
y = ('tolerante', 'intolerante', 'indiferente')
colors = ['#B7CEEC', '#99C68E', '#FFF8C6']
plt.pie(percent, labels=y,  autopct='%1.1f%%', colors=colors)
plt.savefig('toler.png')
plt.close()


weight = frequency_by_buckets(df, 'Peso', 10, 40, 100)
percent = weight['freq'] * 100


plt.figure(figsize=(10,8))
plt.bar(['40-50', '50-60', '60-70', '70-80', '80-90', '90-100'], percent)
plt.title('Distribuição de Pesos')
plt.xlabel('Peso')
plt.ylabel('Frequencia')
plt.savefig('peso.png')
plt.close()
