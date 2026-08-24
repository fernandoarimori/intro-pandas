#%%
import pandas as pd

df = pd.read_csv("../data/customers.csv", sep=";")
df
#%%
df.sort_values(by="Points", inplace=True, ascending=False)  #ascending faz ao contraio
#%%
#ENCADEAMENTO DE METODOS,
#FAZENDO VALORES SORTIDOS E 
#RENOMEANDO COLUNAS
#NESSE CASO NÃO SE USA O INPLACE, PORQUE O MESMO NÃO RETORNA UM DATAFRAME
df = (df.sort_values(by="Points", ascending=False)
      .rename(columns = {"UUID": "ID", "Name": "Nick", "Points": "Score"}))
df

#%%
#SORTINDO EM ORDEM DECRECENTES DE PONTOS
#POREM SE TIVER MESMA PONTUACAOM APLICAR 
#REGRA DE DESEMPATE POR ORDEM ALFABETICA
df.sort_values(by=["Score", "Nick"], ascending=[False, True])
#nesse caso está sortindo primeiro pelo score e depois pelo nick
#OU SEJA QUEM TEM MESMO PONTUACAO, FICA EM ORDEM ALFABETICA
df.sort_values(by=["Score", "Nick"], ascending=[False, True]).tail(10)
#%%
df = (df.sort_values(by=["Score", "Nick"], ascending=[False, True])
      .rename(columns = {"UUID": "ID", "Name": "Nick", "Points": "Score"}))
df


