from asyncore import read
from cmath import isnan
from fnmatch import translate
import pandas as pd
import numpy as np

df = pd.read_excel('Database.xlsx')

print(df.columns)

for col in df.columns:
    df[col].fillna(" ", inplace=True)

    for index, row in enumerate(df[col]):
        if isinstance(row, float):
            row = round(row, 2)

        row = str(row)

        row = row.replace("0", "০")
        row = row.replace("1", "১")
        row = row.replace("2", "২")
        row = row.replace("3", "৩")
        row = row.replace("4", "৪")
        row = row.replace("5", "৫")
        row = row.replace("6", "৬")
        row = row.replace("7", "৭")
        row = row.replace("8", "৮")
        row = row.replace("9", "৯")

        df.iloc[index, df.columns.get_loc(df[col].name)] = row;

for col in df.columns:
    if "Unnamed" in df[col].name:
        df.rename(columns={df[col].name: ""}, inplace=True)

df.to_excel("output.xlsx", index=False)