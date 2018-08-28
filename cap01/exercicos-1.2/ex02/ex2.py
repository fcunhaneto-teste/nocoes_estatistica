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

plt.figure(figsize=(6,4))
plt.bar(freq_f.index, freq_f.freq)
plt.title('Distribuição de Fisioterapia')
plt.xlabel('Horas')
plt.ylabel('Frequencia')
plt.xticks(freq_f.index) # obriga a mostrar todos os números no eixo x
plt.savefig('fisio.png')
plt.close()

freq_s = frequency(df, 'sequelas')
freq_s.index.names = ['sim/não']
freq_s.columns.names = ['sequelas']

with open('sequelas.txt','w') as f:
    freq_s.to_string(f)

plt.figure(figsize=(6,5))
plt.bar(freq_s.index, freq_s.total)
plt.title('Distribuição de Sequelas')
plt.xlabel('Sim ou Não')
plt.ylabel('Totais')
plt.xticks(freq_s.index) # obriga a mostrar todos os números no eixo x
plt.savefig('sequelas.png')
plt.close()

freq_c = frequency(df, 'cirurgia')
freq_c.columns.names = ['complexidade']
freq_c.rename(index={'a':'alta', 'b':'baixa', 'm': 'media'}, inplace=True)

with open('cirurgia.txt','w') as f:
    freq_c.to_string(f)

plt.figure(figsize=(6,5))
plt.bar(freq_c.index, freq_c.total)
plt.title('Distribuição de Complexidade da Cirurgia')
plt.xlabel('Frequencia')
plt.ylabel('Totais')
plt.xticks(freq_c.index) # obriga a mostrar todos os números no eixo x
plt.savefig('cirurgia.png')
plt.close()

# df_sem_sequela = df[df['sequela' != 's']]
# print(df_sem_sequela)

