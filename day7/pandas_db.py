#%% 
import pandas as pd
import sqlalchemy

#%%
engine = sqlalchemy.create_engine("sqlite:///../data/database.db")

#%%
df_all_customers = pd.read_sql_table("customers", engine) #return all DataFrame
df_all_customers

#%%
query = """
SELECT * FROM customers limit 10
"""
pd.read_sql_query(query, engine)
#limited consult

#%%

query_join = """
SELECT * FROM customers as t1
LEFT JOIN transactions as t2
ON t1.UUID = t2.IdCustomer
limit 10
"""
df_join = pd.read_sql_query(query_join, engine)
df_join


#SEND DATA TO DATABASE

#%%
user_data = {
    "id": [1,2,3,4,5],
    "name" : ["A", "B", "C", "D", "E"],
    "age": [32, 43, 23, 13, 53]
}

df_user = pd.DataFrame(user_data)
df_user

#%%
transaction = {
    "id" :  [1,2,3,4],
    "name" : ["F", "G", "H", "I"],
    "age" : [32, 45, 32, 34]
}

df_transaction = pd.DataFrame(transaction)
df_transaction


#%%
df_user.to_sql("tb_test", engine, index=False)
#%%
pd.read_sql("tb_test", engine)
#%%
df_transaction.to_sql("tb_test", engine, index=False, if_exists="append")
#%%
pd.read_sql("tb_test", engine)





#%%
#DELETING TABLE
query = "DROP TABLE IF EXISTS tb_test"

with engine.connect() as conn:
    conn.execute(query)
    conn.commit()
