import pandas as pd
import numpy as np
import csv
import sqlite3

# Connecting to SQL server
conn = sqlite3.connect('APServer.sqlite')
cur = conn.cursor()

# Collecting all events and titles for labeling
cur.execute('''SELECT Event.id, Gender.name, Event.name FROM Event JOIN Gender ON Event.gender_id = Gender.id''')
events = cur.fetchall()  # ex. (1, 'Male', '100m'), (2, 'Male', '200m')

for event in events:
    event_id = event[0]
    gender = event[1]
    event_name = event[2]
    mark_count = 4
    title = gender + '_' + event_name

    path = fr'C:\...\AthleticProject\ML_data\Top_{mark_count}_Marks'

    cur.execute('''SELECT DISTINCT athlete_id FROM Full_Result WHERE event_id = ?''', (event_id, ))
    athletes = cur.fetchall()  #
    # print(gender, event_name, len(df))  # Unique athlete count per event

    # Exploring each athlete's marks
    cnt = 0
    headerList = ['athlete_id', 'm1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9', 'm10']
    headerList = headerList[:mark_count+1]
    final = list()

    for athlete in athletes:
        id = athlete[0]  # Keeping for checks
        temp = list()
        # Pulling top x marks for each athlete
        cur.execute('''SELECT mark FROM Full_Result WHERE athlete_id = ? AND event_id = ? ORDER BY mark Limit ?''',
                    (id, event_id, mark_count))
        temp_df = cur.fetchall()

        if len(temp_df) < mark_count: continue  # Skips over athletes with less than 10 marks
        cnt += 1
        temp.append(id)
        for mark in temp_df: temp.append(mark[0])
        final.append(temp)

    # print(title, 'Number of athletes:', cnt)
    # for y in final:
    #     print(y)
    x = pd.DataFrame(final, columns=headerList)
    x.to_csv(path + f'\ML_Prep_{title}.csv', index=False)
