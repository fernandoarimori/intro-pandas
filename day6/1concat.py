#%%
import pandas as pd

data1 = {
    "index" : [1, 2, 3, 4, 5],
    "nome" : ["A", "B", "C", "D", "E"],
    "values" : [324, 234, 543, 231, 232]
}

df1 = pd.DataFrame(data1)
df1

#%%
data2 = {
    "index" : [6, 7, 8, 9, 10],
    "nome" : ["A1", "B2", "C3", "D4", "E5"],
    "values" : [1324, 1234, 1543, 1231, 1232]
}
df2 = pd.DataFrame(data2)
df2

#%%
concat_1 = pd.concat([df1, df2])
concat_1.reset_index()
concat_1.set_index("index")

#%%
data3 = {
    "last_name" : ["1A", "2B", "3C", "D4", "5E"],
    "values_2" : [1324, 1234, 1543, 1231, 1232]
}
df3 = pd.DataFrame(data3)
df3

#%%
concat_axis_1 = pd.concat( [concat_1, df3], axis=1 )
concat_axis_1.set_index("index")