import pandas as pd
import matplotlib.pyplot as plt
from pandasutils.pandasutils import frequency_by_natural_order


dias = [15, 17, 16, 15, 17, 14, 17, 16, 16, 17, 15, 18, 14, 17, 15, 14, 15,
        16, 17, 18, 18, 17, 15, 16, 14, 18, 18, 16, 15, 14]

df = pd.DataFrame({
    'dias': dias,
})

s = frequency_by_natural_order(df, 'dias')
with open('ex05.txt','w') as f:
    s.to_string(f)

plt.figure(figsize=(5,5))
plt.title('Dias para Cicatrizção')
y = ('14 dias', '15 dias', '16 dias', '17 dias', '18 dias')
colors = ['#B7CEEC', '#99C68E', '#FFF8C6', '#4DBCD3', '#BBE1CA']
explode = (0.1, 0.1, 0, 0, 0)
plt.pie(s.freq, labels=y,  autopct='%1.1f%%', colors=colors, explode=explode,
        shadow=True)
# plt.savefig('ex05.png')
plt.show()
plt.close()

