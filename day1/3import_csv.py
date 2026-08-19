#%%
import pandas as pd

df_customers = pd.read_csv("../data/customers.csv", sep=";")
df_customers
df_customers.info()
# %%
df_customers.size
#%%
df_customers.shape
df_customers.shape[0]
#%%
df_customers.info(memory_usage="deep")
#%%
df_customers["Points"].describe()
#%%
#Points esta como objects
df_customers["Points"].astype(int)
#%%
#COLUNAS RECEBEM OPERAÇÕES VETORIAIS
df_customers["Points"]+1000
#%%
df_customers["Points"] - 1000
#%% 
#FILTRAGEM EM PANDAS
df_customers["Points"] > 1000
condi = df_customers["Points"] > 1000
df_customers[condi]
#maior pontuação
#%%
df_customers[
    df_customers["Points"]==df_customers["Points"].max()
    ]["Name"].iloc[0]
#mesmo que
#%%
condicao = df_customers["Points"]==df_customers["Points"].max()
df_max = df_customers[condicao]["Name"]
df_max.iloc[0]
#%%
#Entre 1000 e 2000 points (me)
bigger_than = df_customers[
    df_customers["Points"]>=1000
]
between = bigger_than[
    bigger_than["Points"]<=2000
                      ]
between
#%%
#simple ver (teacher)
between_teacher = df_customers[
    (df_customers["Points"]>=1000) & (df_customers["Points"]<=2000) 
 ].copy()
between_teacher

#%%
# TUDO NO PYTHON É REFERENCIA
a = [1, 2, 3]
b = a
print(a)
print(b)
b.append(4)
print(a)
print(b)


a = [1, 2, 3]
b = a.copy()
print("\n")
print(a)
print(b)
b.append(4)
print(a)
print(b)
#%%
# TODA VEZ QUE FOR ALTERAR ALGUMA FATIA DE DATAFRAME FAZER UMA COPY
between_teacher["Points"] = between["Points"]+1000
between_teacher.describe()
#%%

df_customers.describe()

#Andar pelas colunas
#%%
df_customers["UUID"] #->dataset
#%%
df_customers[["UUID"]] #->dataframe
#%%
df_customers[["UUID", "Name"]] #->dataframe
#%%
colunas = df_customers.columns.to_list()
colunas.sort()
colunas
df_customers[colunas]
df_customers = df_customers[colunas] #ALTERANDO O PROPRIO DATAFRAME
df_customers

#RENOMEAR COLUNA

#%%
#RENAME CRIA UM DATAFRAME NOVO
df_customers = df_customers.rename(columns={"Name": "Nick",
                              "Points": "Score"})
#%%
df_customers
#%%
df_customers.rename(columns={"UUID": "Id"}, inplace=True) #RENOMEIA DIRETO NO DATAFRAME
df_customers