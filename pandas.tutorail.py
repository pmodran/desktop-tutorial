import pandas as pd

mp_path = '/Users/mma2998/Downloads/ARMA-2024_10.xlsx'  



mp_dataframe = pd.read_excel(mp_path)


print(mp_dataframe.head())

mp_shape = mp_dataframe.shape

print(mp_shape)

print(mp_dataframe.describe())