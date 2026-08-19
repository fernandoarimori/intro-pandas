# Carregue os dados do arquivo data/ipea/homicidios.csv de forma correta e informe:
# Quantidade de linhas
# Quantidade de colunas
# Nome da primeira coluna
# Nome da última coluna

#%%
import pandas as pd

df = pd.read_csv("../data/ipea/homicidios.csv", sep=";")
df
#%%
df.shape
rows = df.shape[0]
rows #with header
#%%
columns = df.columns.size
columns

#%%
first_row= df.iloc[0]
first_row #first row

#%%
first_column = df.keys()
first_column[0]

#%%
test_first_column = df.head(1)
test_first_column
#%%
last_column = df.keys()
last_column[-1]
#%%
last_test = df.tail(1)
last_test