import pandas as pd
import numpy as np

def statistical_info(df):
    maximum = df.max(axis=1)
    minimum = df.min(axis=1)
    median = df.median(axis=1)
    mean = df.mean(axis=1)
    res = pd.concat([maximum, minimum, median, mean], axis=1)
    res.columns = ['maximum', 'minimum', 'median', 'mean']
    return res

tables = ['no_sort.csv', 'sort_by_id.csv', 'sort_by_name.csv']
for i in range(3):
    df = pd.read_csv(tables[i], header=None)
    stats_df = pd.concat([df[[0]], statistical_info(df.iloc[:, 1:])], axis=1)
    stats_df.columns = ['name', 'maximum', 'minimum', 'median', 'mean']
    stats_df.to_csv("stats_"+tables[i], index=False)
    print("stats_"+tables[i])

stats_no_sort = pd.read_csv('stats_no_sort.csv')
stats_sort_by_id = pd.read_csv('stats_sort_by_id.csv')
stats_sort_by_name = pd.read_csv('stats_sort_by_name.csv')

difference_id = pd.concat([stats_no_sort[['name']],stats_sort_by_id.iloc[:, 1:]-stats_no_sort.iloc[:, 1:]], axis=1)
difference_name = pd.concat([stats_no_sort[['name']],stats_sort_by_name.iloc[:, 1:]-stats_no_sort.iloc[:, 1:]], axis=1)

difference_id.to_csv("difference_id.csv", index=False)
difference_name.to_csv("difference_name.csv", index=False)