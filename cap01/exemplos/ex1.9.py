import pandas as pd
import matplotlib.pyplot as plt
from pandasutils.pandasutils import frequency, frequency_by_buckets, frequency_by_natural_order

df = pd.read_csv('/home/francisco/Projects/Pycharm/nocoes_estatistica/files/cap01/questionario.csv')
print(df)
df_m = df[df.Sexo != 'F']
print(df_m)