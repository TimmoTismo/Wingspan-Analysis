import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Read in data
df = pd.read_csv("data\wingspan birds.csv")

#Filter rows and columns
df = df[df["Common name"].notnull()].iloc[:, 0:26]

#Fill in null values in individual food costs column
df.iloc[:, 16:23] = df.iloc[:, 16:23].fillna(0)

#Fill  in null values in Total food cost column
df["Total food cost"] = np.where(df["/ (food cost)"] == 'X', 1, df.iloc[:, 16:23].sum(axis=1))




print(df[df["Total food cost"]==3].sort_values(by=df["Victory points"]+df["Egg capacity"]))
