#Renomear 2 colunas para nome e descrição
#%%
import pandas as pd

df = pd.read_csv("../data/products.csv", 
                 sep=";",
                 names=["Id", "Name", "Description"])
df

#%%
df.rename(columns={
    "Name": "Nome",
    "Description": "Descrição"
}, inplace=True)
df
