#Ultima transação de cada idCostumer
#%%
import pandas as pd

df = pd.read_excel("../data/transactions.xlsx")
df.shape
#%%
df_responde = (
    df.sort_values(by="DtTransaction", ascending=False)
    .drop_duplicates(subset=["IdCustomer"], keep="first")
)
df_responde
#%%
df_responde.shape
#%%
df_responde["IdCustomer"].nunique()
#%%
df[df["IdCustomer"] == "5f8fcbe0-6014-43f8-8b83-38cf2f4887b3"].sort_values(by="DtTransaction", ascending=False)
df_responde[df_responde["IdCustomer"] == "5f8fcbe0-6014-43f8-8b83-38cf2f4887b3"]
