# mysetup.py
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# import pandasql as ps
from collections import defaultdict
import os, datetime, pickle, pathlib

import textwrap


import itertools, random
from pathlib import Path
from pulp import (LpProblem, LpMinimize, LpBinary, LpVariable,
                  lpSum, PULP_CBC_CMD)


# Set plotting styles
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

def save_dataframe(df, dir_path, file_name):
    # Create the directory if it doesn't exist
    os.makedirs(dir_path, exist_ok=True)
    
    # Full path to save the file
    file_path = os.path.join(dir_path, file_name)
    
    # Save the dataframe (as CSV, for example)
    df.to_csv(file_path, index=False)
    
    print(f"DataFrame saved to {file_path}")


def save_pickle(df, dir_path, file_name):

    file_path = dir_path +"/" + file_name  +".pkl"
    with open(file_path, "wb") as file:
        pickle.dump(df, file)

        
def load_pickle( dir_path, file_name):

    file_path = dir_path +"/" + file_name  +".pkl"
    with open(file_path, "rb") as file:
        load_file = pickle.load(file)

    return load_file


def check_sorted(df, col, ascending = True, time_data = True):

    if time_data: 
        if ascending: 
            check_sort = (df[col].diff().dropna() >=  np.timedelta64(0,"s") ).all()
        else:
            check_sort = (df[col].diff().dropna() <=  np.timedelta64(0,"s") ).all()
    else:
        if ascending: 
            check_sort = (df[col].diff().dropna() >= 0 ).all()
        else:
            check_sort = (df[col].diff().dropna() <= 0 ).all()

    if not check_sort:
        raise ValueError(f"Col {col} is not sorted ") 

def check_year_distribution(df, col_time): 
    df_so_year = pd.to_datetime(df[col_time]).dt.year
    return df_so_year.value_counts()


def rename_ID(df, mapping):

    area_mapping = mapping["area_mapping"]
    facility_mapping = mapping["facility_mapping"]
    person_mapping = mapping["person_mapping"]
    stay_mapping = mapping["stay_mapping"]

    if "STAY_ID" in df.columns:
        df["STAY_ID"] = df["STAY_ID"].map(stay_mapping)
    if "FACILITY" in df.columns:
        df["FACILITY"] = df["FACILITY"].map(facility_mapping)
    if "PERSON_ID" in df.columns:
        df["PERSON_ID"] = df["PERSON_ID"].map(person_mapping)
    if "AREA" in df.columns:
        df["AREA"] = df["AREA"].map(area_mapping)

    return df

print("Setup complete.")
