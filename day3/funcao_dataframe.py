#%%
import pandas as pd

dado = {
    "Name": ["Fernando", "Andrea", "Art", "Eduardo"],
    "Recencia": [10, 1 , 30, 100],
    "Valor": [180, 200, 15, 1000],
    "Frequencia": [7, 14, 1, 30]
}

df = pd.DataFrame(dado)
df
#%%
def rfv (row):
    rate = 0

    if row["Recencia"] >10 :
        rate+= 10
    elif 5 <= row["Recencia"] >=3:
        rate+=5
    else:
        rate+=0

    if row["Valor"] >100 :
        rate+= 10
    elif 15 <= row["Valor"] >=10:
        rate+=5
    else:
        rate+=0     

    if row["Frequencia"] >10 :
        rate+= 10
    elif 7 <= row["Frequencia"] >=5:
        rate+=5
    else:
        rate+=0        
    return rate

df["RFV"] = df.apply(rfv, axis=1)
df
