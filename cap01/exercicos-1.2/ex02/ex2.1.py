import pandas as pd
import matplotlib.pyplot as plt
from pandasutils.pandasutils import frequency, frequency_by_natural_order

p = [x for x in range(1, 16)]

f = [7 ,8, 5, 6, 4, 5, 7, 7, 6, 8, 6, 5, 5, 4, 5]

ss = 'ssnnnssnnssnsnn'
s = list(ss)

cs = 'amammbambmbbmma'
c = list(cs)

df = pd.DataFrame({
    'paciente': p,
    'fisio': f,
    'sequelas': s,
    'cirurgia': c
})

with open('ex2_dataframe.txt','w') as f:
    df.to_string(f)

freq_f = frequency_by_natural_order(df, 'fisio')
freq_f.columns.names = ['horas']

with open('fisioterapia.txt','w') as f:
    freq_f.to_string(f)


freq_s = frequency(df, 'sequelas')
freq_s.index.names = ['sim/não']
freq_s.columns.names = ['sequelas']

with open('sequelas.txt','w') as f:
    freq_s.to_string(f)

freq_c = frequency(df, 'cirurgia')
freq_c.columns.names = ['complexidade']
freq_c.rename(index={'a':'alta', 'b':'baixa', 'm': 'media'}, inplace=True)

with open('cirurgia.txt','w') as f:
    freq_c.to_string(f)

fig = plt.figure(figsize=(10, 8))

ax1 = fig.add_subplot(2, 2, 1)
ax1.bar(freq_f.index, freq_f.freq, color=['#4dbcd3', '#bbe1ca'])
ax1.set_title('Fisioterapia')
ax1.set_xlabel('horas')
ax1.set_ylabel('frequencia/pacientes')

ax2 = fig.add_subplot(2, 2, 2)
ax2.bar(freq_s.index, freq_s.total, color=['#4dbcd3', '#bbe1ca'])
ax2.set_title('Sequelas')
ax2.set_xlabel('sim/não')
ax2.set_ylabel('total pacientes')

ax3 = fig.add_subplot(2, 2, 3)
ax3.bar(freq_c.index, freq_c.total, color=['#4dbcd3', '#bbe1ca'])
ax3.set_title('Cirurgia')
ax3.set_xlabel('complexidade')
ax3.set_ylabel('total pacientes')

fig.show()
fig.savefig('fisioterapia_subplots.png')
plt.close()
# df_sem_sequela = df[df['sequela' != 's']]
# print(df_sem_sequela)

