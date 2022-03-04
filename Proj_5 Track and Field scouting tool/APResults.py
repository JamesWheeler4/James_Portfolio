import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import glob
import time
import re


def scoring(i):  # Assigns scores to placement of new data
    if i == 1: return 10
    if i == 2: return 8
    if i == 3: return 6
    if i == 4: return 5
    if i == 5: return 4
    if i == 6: return 3
    if i == 7: return 2
    if i == 8: return 1
    if i == 9: return 0
    if i == 10: return 0


def toptenfinal(dflist):  # Calculates and scores top ten marks in each event
    y = None
    count = 1
    last = list()
    temp = list()

    for line in dflist:
        x = line[0]
        line[1] = count
        last.append(x)
        if y == x:
            continue
        try:
            if count < 10 and x != last[-2]:
                count = 1
                continue
        except:
            pass
        if count < 11:
            # print('into lp2', count, x)
            score = scoring(count)
            if count == 10:
                y = x
            line.append(score)
            temp.append(line)
            count = count + 1
            # print('temp', temp)
            continue
        else:
            # print('clearing')
            count = 1
    return temp


def topglob(gender, type):  # Groups and processes all gathered data to output results, Repeated for each event type and gender

    globby = glob.glob(fr'C:\Users\15037\PycharmProjects\PythonForEveryone\AthleticProject\AP{gender}\H{type}*.csv')

    df_list = []
    for f in globby:
        csv = pd.read_csv(f)
        df_list.append(csv)

    ahigh = pd.concat(df_list)
    ahighsort = ahigh[['10', '2', '3', '5', '6', '7', '8', '1']]
    ahighsort = pd.DataFrame(ahighsort)
    ahighsort = ahighsort.rename(columns={'10': '0', '2': '1', '3': '2', '5': '3', '6': '4', '7': '5', '8': '6', '1': '7'} )


    ahighsort.to_csv(fr'C:\Users\15037\PycharmProjects\PythonForEveryone\AthleticProject\AP{gender}\C{type}ahs.csv', index=False)
    globby = glob.glob(fr'C:\Users\15037\PycharmProjects\PythonForEveryone\AthleticProject\AP{gender}\C{type}*.csv')

    df_list = []
    for i in globby:
        csv = pd.read_csv(i)
        df_list.append(csv)

    all = pd.concat(df_list)

    if type == 'Track':
        allsort = all.sort_values(['0', '5'])
    else:
        allsort = all.sort_values(['0', '5'], ascending=False)

    vals = allsort.values
    aslist = vals.tolist()

    topall = pd.DataFrame(aslist)
    topall.to_csv(f'TopAll_{gender}_{type}.csv', index=False)
    topten = pd.DataFrame(toptenfinal(aslist))
    topten.to_csv(f'TopTen_{gender}_{type}.csv', index=False)
