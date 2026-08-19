#%%
import pandas as pd

df = pd.read_excel("../data/transactions.xlsx")
df
#%%
df.size
#%%
df.shape
#%%
#primeiras 5 linhas
df.iloc[0:5]
#Ou
#%%
df.head()
#5 ultimas
#%%
df.tail()
#OU
#%%
df.iloc[(23502-5):23503]

#%%
#ORDENANDO COLUNAS
new_column = df.columns.to_list()
new_column.sort(reverse=True)
df = df[new_column]
df

#OU
#%%
new_column = ["UUID", "Points", "IdCustomer", "DtTransaction"]
df = df[new_column]
df
#%%
df.info(memory_usage="deep")

