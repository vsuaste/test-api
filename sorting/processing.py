import pandas as pd
import numpy as np

def statistical_info(df):
    maximum = df.max(axis=1)
    minimum = df.min(axis=1)
    median = df.median(axis=1)
    mean = df.mean(axis=1)
    quantile = df.quantile([0.25, 0.75], axis=1).T
    res = pd.concat([maximum, minimum, median, mean, quantile], axis=1)
    res.columns = ['maximum', 'minimum', 'median', 'mean', '25%', '75%']
    return res

tables = ['no_sort.csv', 'sort_by_id.csv', 'sort_by_name.csv']
for i in range(len(tables)):
    df = pd.read_csv(tables[i], header=None)
    stats_df = pd.concat([df[[0]], statistical_info(df.iloc[:, 1:])], axis=1)
    stats_df.columns = ['name', 'maximum', 'minimum', 'median', 'mean', '25%', '75%']
    stats_df.to_csv("stats_"+tables[i], index=False)
    print("stats_"+tables[i])
