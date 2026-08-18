# Converta o seguinte dicionário para DataFrame e obtenha:
# Sumário de cada coluna
# Média da coluna idade
# Último nome da coluna nome

# dados = {“nome”:[“Téo”, “Nah”, “Napoleão”], “idade”: [31, 32, 14]}

#%%
import pandas as pd
dados = {"nome":["Téo", "Nah", "Napoleão"], "idade": [31, 32, 14]}
df = pd.DataFrame(dados)
df
#%%
sumario = df.columns
sumario
#%%
media_idade = df["idade"].mean()
media_idade
#%%
ultimo_nome = df.tail(1)
umtimo_nome_alt = df["nome"][2]
ultimo_nome
#%%
umtimo_nome_alt
#%%
ultimo_nome["nome"]