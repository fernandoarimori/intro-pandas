#%%
import pandas as pd

#%%
df = pd.read_csv("../data/exercise_export/concat_all_homicidios.csv", sep=";")
df["homicidios"].tail(5)

#%%
df_stack = (df.set_index(['cod', 'nome', 'período'])
            .stack()
            .reset_index()
            .rename(columns={"level_3": "tipo_homicidio", 0: "valor"}))
#%%
df_stack
df_stack.columns
#%%
#UNSTACKING
df_unstack = (df_stack.
              set_index(['cod', 'nome', 'período', 'tipo_homicidio'])
              .unstack()
              .reset_index()
            )
df_unstack

#%%
homicidios = df_unstack["valor"].columns.to_list()
homicidios
#%%
indicadores = df_unstack.columns.droplevel(1).to_list()[:3]
indicadores
#%%
df_unstack.columns = indicadores + homicidios
df_unstack