#Ultima transação de cada idCostumer
#%%
import pandas as pd

df = pd.read_excel("../data/transactions.xlsx")
df.shape
#%%
df_responde = (
    df.sort_values(by="DtTransaction", ascending=False)
    .drop_duplicates(subset=["IdCustomer"], keep="last")
)
df_responde