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

df_ca = df[df.cirurgia == 'a']

print(df_ca)

df_cm = df[df.cirurgia == 'm']

print(df_cm)

df_cb = df[df.cirurgia == 'b']

print(df_cb)



