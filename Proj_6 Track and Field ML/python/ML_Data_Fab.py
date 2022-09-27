import random
import pandas as pd
import numpy as np
import glob
import os

path_10 = r'C:\...\AthleticProject\ML_data\Top_10_Marks'
path_6 = r'C:\...\AthleticProject\ML_data\Top_6_Marks'
path_4 = r'C:\...\AthleticProject\ML_data\Top_4_Marks'

glob_10 = glob.glob(path_10 + '\*.csv')
glob_6 = glob.glob(path_6 + '\*.csv')
glob_4 = glob.glob(path_4 + '\*.csv')


def average(lst):
    return sum(lst) / len(lst)


def jitterBug(x):
    # Turns 1 entry into 1+10
    multiple = 10
    turn = 0
    x_multiplied = []
    while turn < (multiple):
        turn += 1
        x_jit = []
        for num in x:
            # Currently jitters each number +/- 2%
            bottom = int((num*0.995)*100)
            top = int((num*1.005)*100)
            jitter = ((random.randrange(bottom, top, 1)) / 100)
            # Collects new full entry
            x_jit.append(jitter)
        # Collects all new, jittered entries
        x_multiplied.append(sorted(x_jit))
        # print(x, x_multiplied)
    return x_multiplied


for x in glob_4:
    # Pulling Data
    df = pd.read_csv(f'{x}')
    df = df.drop(columns=['athlete_id'])
    # Setting name for each loop
    names = x.split('_')[-2:]
    s = '_'
    name = s.join(names).split('.')[0]
    df_avg = round(df['m1'].mean(), 1)
    print(name, df_avg)

    lst = df.values.tolist()
    multiplied_lst = []
    for y in range(len(df)):
        jittered_10x = jitterBug(lst[y])
        og = lst[y]
        multiplied_lst.append(og)
        for set in jittered_10x:
            multiplied_lst.append(set)
    print('og Length', len(lst), 'multiplied Length', len(multiplied_lst))
    multi_df = pd.DataFrame(multiplied_lst)
    multi_df.columns = ['m1', 'm2', 'm3', 'm4']
    print(df.describe())
    print(multi_df.describe())
    multi_df.to_csv(f'{name}_x10_05_percent_jitter.csv', index=False)
