# Converta a seguinte lista de dados para uma Series Pandas e obtenha:
# Média
# Desvio Padrão
# Máximo Valor

# dados = [10, 20, 42, 9, 12, 35, 24, 10, 8, 14, 21]

#%%
import pandas as pd

main_data = [10, 20, 42, 9, 12, 35, 24, 10, 8, 14, 21]
data_serie = pd.Series(main_data, name = "data")
data_serie.describe()
#%%
media = data_serie.mean()
#%%
desvio_padrao = data_serie.std()
#%%
valor_max = data_serie.max()
print("média = ", media, "\ndesvio padrão = ", desvio_padrao, "\nvalor máximo = ", valor_max)
