#%%
import pandas as pd

#Agregação é uma forma resumida de expressar dados, tipo soma e média

df =pd.read_excel("../data/transactions.xlsx")
df
#%%
condicao = df["IdCustomer"] == "5f8fcbe0-6014-43f8-8b83-38cf2f4887b3"
df[condicao]["Points"].max()

#%%
#COM TODOS
df.groupby(["IdCustomer"])["Points"].sum()
#%%
type(df.groupby(["IdCustomer"])["Points"].sum())
#%%
df.groupby(["IdCustomer"])["Points"].mean()
#%%

df_rfv = df.groupby(["IdCustomer"]).agg({
        "Points" : "sum",
        "UUID" : "count",
        "DtTransaction" : "max"
    }).rename(columns={
        "Point" : "Valor",
        "UUID" : "Frequencia",
        "DtTransaction" : "Recencia" 
    }).reset_index()

df_rfv