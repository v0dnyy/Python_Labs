import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


a = []
for i in range(1, 100):
    a.append(i)

a = np.random.permutation(a)

column_one = []
for elem in a:
    if elem <= 10:
        column_one.append(0)
    else:
        column_one.append(elem)

column_two = []
for elem in a:
    if elem >= 90:
        column_two.append(100)
    else:
        column_two.append(elem)

column_one = np.array(column_one)
df = pd.DataFrame({
    '10': column_one,
    '90': column_two
})

print(df)
column_one.sort()
print(column_one)
print(column_two)

fig, axs = plt.subplots(1, 2)
n_bins = len(df)
axs[0].hist(df['10'], bins=n_bins)
axs[0].set_title('10')
axs[1].hist(df['90'], bins=n_bins)
axs[1].set_title('90')

plt.show()
