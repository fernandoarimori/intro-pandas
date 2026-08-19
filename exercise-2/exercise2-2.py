# Carregue os dados do arquivo data/ipea/homicidios-mulheres-negras.csv de forma correta e informe:
# Quais colunas são do tipo numérico?
# Quantas colunas são do tipo ‘object’?
# Qual o tamanho destes dados em memória?


#%%
import pandas as ps

df = ps.read_csv("../data/ipea/homicidios-mulheres-negras.csv", sep=";")
df

#%%
type(df["cod"].iloc[0])
#%%
list_keys = df.keys()
int_keys=[]
object_keys = []
df_ = df.copy()
df_["nome"].astype("O")
df_.info()
#%%
for i in list_keys:
    if df[i].dtypes=="int64":
        int_keys.append(i)
    elif df_[i].dtypes=="object":
        object_keys.append(i)
print("Colunas tipo numerico: ", int_keys)
print("Colunas tipo objeto: ", object_keys)

#%%
df.info(memory_usage="deep")
