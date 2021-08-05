#!/usr/bin/env python3
import pandas as pd_nfl
import os
#set the default directory
os.chdir("/home/student/mycode/miniprojects/data")
data_file ="nfl_statistics_2020.txt"
nfl_data= pd_nfl.read_csv(data_file)

print(nfl_data.head())
print(nfl_data.shape)
#drop duplicate rows if there are any
nfl_data.drop_duplicates(inplace=True)
print(nfl_data.shape)
#remove columns with atleast one column NaN
nfl_data = nfl_data.dropna(axis="columns")
print(f"After removing NaN: {nfl_data.shape}")
nfl_data.to_json("nfl_statistics_columns_remove.tx")
print(nfl_data.columns)
print(nfl_data["IsTouchdown"].value_counts())
