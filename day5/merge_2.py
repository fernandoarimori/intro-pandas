#%%
import pandas as pd

dt_user = pd.read_csv("../data/customers.csv", sep=";")
dt_user

#%%
dt_transaction = pd.read_excel("../data/transactions.xlsx")
dt_transaction
#%%
dt_transaction_product = pd.read_parquet("../data/")

#%%
dt_transaction.merge(
    dt_user,
    how="inner",
    left_on= "IdCustomer",
    right_on="UUID",
    suffixes=["_transaction", "_customer"]
)


# %%
checking =dt_transaction.merge(
    dt_user,
    how="left",
    left_on= "IdCustomer",
    right_on="UUID"
).copy()
checking[checking["UUID_y"].isna()]