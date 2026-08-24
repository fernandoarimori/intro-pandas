#%%
import pandas as pd


dado = {
    "Name": ["Ana", "Eduardo", "Breno", "Lúcio", "Eduardo"],
    "Age": [30, 23, 21, 54, 65],
    "updated_at": [1,2,3,1,2]
}
#%%
df = pd.DataFrame(dado)
df

#%%
# df.drop_duplicates()
# df
#%%
df = df.sort_values(by="updated_at", ascending=False)
df
#%%
df.drop_duplicates(subset=["Name"], keep="first")

#%%
df = (
    df.sort_values(by="updated_at", ascending=False)
    .drop_duplicates(subset=["Name"], keep="first")
      )