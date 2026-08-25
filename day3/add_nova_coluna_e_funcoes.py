#%%
import pandas as pd
import numpy as np
df  = pd.read_csv("../data/customers.csv", sep=";")
df

#add colunas com operações aritméticas de outras
#%%
df["Points_Double"] = df["Points"]*2
df
#%%
df["Points_Half"] = df["Points_Double"] / df["Points"]
df
#%%
#coluna de constante (escalar)
df["Constante"] = 1
df
#%%
df["Poindts_Log"] = np.log(df["Points"])
df
#%%
new_names = []
for i in df["Name"]:
    new_names.append(i.upper())
df["Name"] = new_names
df
#EVITA-SE AO MAXIMO O FOR, NESSE CASO USAMOS:
df["Name"].str.upper()
df
#%%
#Pegando nomes antes do _, usando funcao
def name_change(name:str):
    return name.split("_")[0]

name_change("Fernando_Arimori")

#%%
df["First_Name"] = df["Name"].apply(name_change)
df
#%%
soma = lambda x, y: x+y
soma(1,2)
#%%
# lower_case_in_lambda = lambda name:name.lower() 
df["Lower_case_Name"] = df["Name"].apply(lambda x: x.lower())
df
#%%
df["First_Name"] = df["Name"].apply(lambda x: x.split("_")[0])
df
#%%
df["Upper_Case_Name"] = df["Name"].apply(lambda x: x.upper())
df
#%%
def ratio_points (points: int):
    if points<=2000:
        return "Baixo"
    elif points<=3000:
        return "Medio"
    else:
        return "Alto"

df["Points_Ratio"] = df["Points"].apply(ratio_points)
df
#%%
