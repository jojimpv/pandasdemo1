"""
Basic operations and APIs
"""
import numpy as np
import pandas as pd

np_array = np.random.rand(3)
pd_series = pd.Series(np_array)
pd_series2 = pd.Series(np_array, index=('F', 'S', 'T'))
pd_df = pd.DataFrame(np.random.rand(3, 4))

print(f'{np_array} \n {pd_series} \n {pd_df}')

pd_series2.index

df = pd_df
df.dtypes
df.shape
df.size
df.columns = ['A', 'B', 'C', 'D']
df.columns  # types other than int are shown as "object"
