import pandas as pd
import matplotlib.pyplot as plt

li = [22, 29, 33, 35, 35, 37, 38, 43, 43, 44, 48, 52, 53, 55, 57, 61, 62, 67,
      69]

s = pd.Series(li)
print(s.describe())

plt.boxplot(s)
plt.show()
plt.close()