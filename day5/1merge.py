#%%
import pandas as pd

user_data = {
    "id": [1,2,3,4,5],
    "name" : ["A", "B", "C", "D", "E"],
    "age": [32, 43, 23, 13, 53]
}

df_user = pd.DataFrame(user_data)
df_user

#%%
transaction = {
    "id" :  [1,2,3,4,5,6,7,8],
    "user_id" : [1, 2, 2, 1, 5, 4, 3, 6],
    "value" : [324 ,554, 5544, 33432 ,4343, 43443, 34352, 123],
    "qt" : [32, 45, 32, 34, 123, 1, 3, 3]
}

df_transaction = pd.DataFrame(transaction)
df_transaction

#%%
df_merded = df_transaction.merge(
    df_user,
    how="left",
    left_on=["user_id"],
    right_on=["id"]
)
df_merded[df_merded["id_y"].isna()]

#%%
df_transaction.merge(
    df_user,
    how="right",
    left_on="user_id", 
    right_on="id"
)
#%%
df_transaction.merge(
    df_user,
    how="outer",
    left_on="user_id",
    right_on="id"
)

#%%
df_transaction.merge(
    df_user,
    how="inner",
    left_on="user_id",
    right_on="id"
)

