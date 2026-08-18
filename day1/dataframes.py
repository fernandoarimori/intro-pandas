#%%
import pandas as pd



dic_data = {
    "name" : ["Fernando", "Art", "Adriana"],
    "last name":["Arimori", "Waywood", "Cardoso"],
    "age": [35, 28 ,43]
        }

dic_data["age"][0]
#%%
data_dataframe = pd.DataFrame(dic_data)
data_dataframe

#%%
data_dataframe["age"]
#%%
data_dataframe["age"].iloc[0:]
data_dataframe["age"].describe()
#%%
#Dataframe é um conjunto de Series
type(data_dataframe["name"])
#%%
data_dataframe["last name"]
#%%
# é uma Serie, e tambem uma linha
data_dataframe.iloc[0:]
#%%
data_dataframe.iloc[1]
#%%
data_dataframe["age"]
#%%
data_dataframe.index
#%%
data_dataframe.columns
#%%
data_dataframe.info() #objects  é tudo que não é numerico
#%%
data_dataframe.info(memory_usage="deep")
#%%
data_dataframe.dtypes
#%%
data_dataframe.dtypes["age"]
#%%
#add series
data_dataframe["weight"] = [120.0, 130.0, 87.3]
data_dataframe.describe()
sumary = data_dataframe.describe()
#%%
sumary["weight"]["mean"]
#%%
#amostragem das 2 primeiras linhas
data_dataframe.head(2)
data_dataframe.iloc[0:2]
#amostragem de ultima 2 linhas
data_dataframe.tail(2)