#%%
import pandas as pd

df_user = pd.read_csv("../data/customers.csv", sep=";")
df_user

#%%
df_transaction = pd.read_excel("../data/transactions.xlsx")
df_transaction
#%%
df_transaction_product = pd.read_parquet("../data/transactions_cart.parquet")
df_transaction_product

#%%
df_merged_transaction_user_product = df_transaction.merge(
    df_user,
    how="inner",
    left_on= "IdCustomer",
    right_on="UUID",
    suffixes=["_transaction", "_customer"]
).merge(
    df_transaction_product,
    how="left",
    left_on="UUID_transaction",
    right_on="IdTransaction"
    )


# %%
checking =df_transaction.merge(
    df_user,
    how="left",
    left_on= "IdCustomer",
    right_on="UUID"
).copy()
checking[checking["UUID_y"].isna()]
checking
#%%
df_merged_transaction_user_product 