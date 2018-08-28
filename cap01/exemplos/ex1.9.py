import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    '/home/francisco/Projects/Pycharm/nocoes_estatistica/files/cap01/questionario.csv')
print(df)

# Totais
s = df['Peso']
sd = s.describe()

q3 = sd['75%']
median = sd['50%']
q1 = sd['25%']

# c_assimetric_bowley = ((q3 - median) - (median - q1)) / (q3 - q1)
cb = (q3 + q1 - 2*median) / (q3 - q1)

q3 = sd['75%']
median = sd['50%']
q1 = sd['25%']

# Masculino
df_m = df[df.Sexo != 'F']

sm = df_m['Peso']
sdm = sm.describe()

q3_m = sdm['75%']
median_m = sdm['50%']
q1_m = sdm['25%']

cb_m = (q3_m + q1_m - 2*median_m) / (q3_m - q1_m)

sdm['cb'] = cb_m

# Feminino
df_f = df[df.Sexo != 'M']

sf = df_f['Peso']
sdf = sf.describe()

q3_f= sdf['75%']
median_f = sdf['50%']
q1_f = sdf['25%']

# c_assimetric_bowley = ((q3 - median) - (median - q1)) / (q3 - q1)
cb_f = (q3_f + q1_f - 2*median_f) / (q3_f - q1_f)

sdf['cb'] = cb_f

plt.figure(figsize=(4,4))
plt.boxplot([s, sf, sm])
plt.title('Distribuições de Peso')
plt.xlabel('Distribuição')
plt.ylabel('Peso')
plt.xticks([1, 2, 3], ['T', 'F', 'M'])

plt.savefig('peso_distr.png')
plt.close()
