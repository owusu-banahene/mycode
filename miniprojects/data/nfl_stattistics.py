#!/usr/bin/env python3
import pandas as pd_nfl
import os
def main():
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
    nfl_data.head(10).to_json("nfl_statistics.json")
    #output the first 10 to .lxsx and and last 10 to .csv
    nfl_data.head(10).to_excel("nfl_statistics.xlsx")
    nfl_data.tail(10).to_csv("nfl_statistics.csv")
    print(nfl_data.columns)
    print(nfl_data["IsTouchdown"].value_counts())


if __name__ =="__main__":
    main()
