#%%
import pandas as pd


#%%
ages = [10, 21, 30]
ages
sum_ = sum(ages)
sum_
#%%
avgr =  int(sum_/ len(ages))
avgr
#%%
total = 0
for i in ages:
    total+= (avgr-i)**2

variancia = total/(len(ages) -1)
variancia
#%%
series_ages = pd.Series(ages)
series_ages.mean()
#%%
series_ages.var()
#%%
series_ages.median()
#%%
series_ages.quantile(0.6)
#%%
series_ages.describe()
#%%
series_ages.shape
#obtendo o primeiro elemento
ages[0]
#%%
series_ages[0] #!!cada valor associado a um índice, não é uma lista
series_ages.index = ["a", "b", "c"] # trocando índices
#%%
series_ages["b"]
series_ages
#usar sempre o índice

#%%
#explicitamente a posição, usando atributo iloc
series_ages.iloc[0] #-> pegar dados ordenados, e.g [0:]
#nomeando series
#%%
#usa-se o loc para retornar o valor do índice, como em um dicionario
series_ages.loc["a"]
#%%
series_ages.name = "ages" #-> da pra passar um name no construtor
series_ages

#UMA SERIE É COMO UMA COLUNA DO EXCEL