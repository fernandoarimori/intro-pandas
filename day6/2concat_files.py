#%%
import pandas as pd
import os

def import_files(path:str):
    name  = path.split("/")[-1].split(".")[0]
    df = pd.read_csv(path, sep=";")
    df = df.rename(columns={"valor" : name}).set_index(["cod", "nome", "período"])
    return df

dfs = []
data_path = "../data/ipea/"
data_list = os.listdir(data_path)
data_list[0]
#%%
for i in data_list:
    dfs.append(import_files(data_path+i))

#%%
dfs[0]
#%%
homicidios_concat = pd.concat(dfs, axis=1).reset_index(0)
homicidios_concat.to_csv("../data/exercise_export/concat_all_homicidios.csv", sep = ";", index=False)