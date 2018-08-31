import pandas as pd
import matplotlib.pyplot as plt
from pandasutils.pandasutils import frequency

transp_util =[2, 3, 2, 1, 2, 1, 2, 1, 2, 3, 1, 1, 1, 2, 2, 3, 1, 1, 1, 1, 2,
              1, 1, 2, 2, 1, 2, 1, 2, 3]

print(len(transp_util))

s = pd.DataFrame({
    'transp': transp_util,
})

fr = frequency(s, 'transp')
with open('ex03.txt','w') as f:
    fr.to_string(f)

plt.figure(figsize=(5,5))
plt.title('Meios de Transportes Diferentes')
y = ('Um', 'Dois', 'Três')
colors = ['#B7CEEC', '#99C68E', '#FFF8C6']
plt.pie(fr.freq, labels=y,  autopct='%1.1f%%', colors=colors)
plt.savefig('ex03.png')
plt.close()
