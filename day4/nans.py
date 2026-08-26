#%%
import pandas as pd
import numpy as np

dado = {
    "Name": ["Fernando", "Art", "Derek", "Ana", "Bruno"],
    "Age": [35, 28, 43, 32, np.nan],
    "Salary": [np.nan, 4532.32, 2310.32, 23111, np.nan]
}
df = pd.DataFrame(dado)
df
#%%
df["Age"].isna() 
#%%
df["Age"].isna().sum() #SOMA DOS BOOLEANOS
#%%
df["Salary"].isna().sum()
#%%
df.isna()
df.isna().sum()
#%%
df.isna().mean()
#%%
#MODO MAIS INICIANTE DE PREENCHER, MAIS USADO EM ANALISE DE
#  DADOS MAS NUNCA USAR EM MACHINE LEARNING, RETORNA DATAFRAME NOVO
df.fillna({
    "Age": df["Age"].mean(),
    "Salary": df["Salary"].mean()
    })
# %%
#REMOVE A LINHA INTEIRA
df.dropna()
#%%
#DROPA A LINHA NA QUAL AGE "E" SALARY É NAN
df.dropna(subset= ["Age", "Salary"], how="all")
#DROPA A LINHA NA QUAL AGE "OU" SALARY É NAN
df.dropna(subset= ["Age", "Salary"], how="any")
#%%
#REMOVENDO POR COLUNA
df.dropna(axis=1, how="any")