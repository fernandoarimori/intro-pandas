#%%
import pandas as pd
import datetime
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
#%%
def samples_in_days(x):
    time_spend = datetime.datetime.now() - x.max()
    return time_spend.days

df_rfv_with_days = df.groupby(["IdCustomer"]).agg({
        "Points" : "sum",
        "UUID" : "count",
        "DtTransaction" : "max"
    }).rename(columns={
        "Points" : "Valor",
        "UUID" : "Frequencia",
        "DtTransaction" : "Recencia" 
    }).reset_index()

df_rfv_with_days
#%%

df_rfv_with_days = df_rfv_with_days.groupby(["IdCustomer"]).agg(
    Valor = ("Valor", "sum"),
    Frequencia = ("Frequencia", "count"),
    Recencia = ("Recencia", "max"),
    DayPass = ("Recencia", samples_in_days)
).reset_index()

df_rfv_with_days