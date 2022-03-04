import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import glob
import time
import re

queries = list()


def colmarkcomp(eve, mark):  # Creates comparable marks
    run = ('100m', '200m', '400m', '800m', '1500m', '5000m', '110mh','100mh', '400mh')
    field = ('shot', 'discus', 'javelin', 'hj', 'pv', 'lj', 'tj', 'hammer')

    for i in run:
        if i == eve:
            try:
                strip = mark.strip().split(':')
                sec = strip[1]
                min = int(strip[0]) * 60
                markcomp = min + float(sec[0:5])
                return markcomp
            except:
                markcomp = (mark.strip())
                return markcomp[:-1]
    for i in field:
        if i == eve:
            try:
                s = mark.strip()
                markcomp = round(float(s[:-1]) * 3.28084, 2)
                return markcomp
            except:
                markcomp = mark
                return markcomp


def collegeEventType(x):  # Splits event type into those ranked ascending and descending
    run = ('100m', '200m', '400m', '800m', '1500m', '5000m', '110mh', '100mh', '400mh')
    field = ('shot', 'discus', 'javelin', 'hj', 'pv', 'lj', 'tj', 'hammer')

    for i in run:
        if x == i:
            return 'T'

    for i in field:
        if x == i:
            return 'F'


def collegeresults(query):  # Login, Gather, Parse, Store
    PATH = r"C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    email = 'webotis@gmail.com'
    password = 'Bqm4P8XrqwWH3uz'

    # Login 
    driver.get("https://www.athletic.net/account/login")
    time.sleep(.8)
    login = driver.find_element(By.CLASS_NAME, 'athletic-modal--form-input')
    login.send_keys(email, Keys.TAB, password, Keys.RETURN)
    time.sleep(1.5)
    
    # Gather
    dataT = list()
    dataF = list()
    for i in query:
        meetname = (i[0])
        print(meetname)
        meetnum = i[1]
        gender = i[2]
        eventm = ('100m', '200m', '400m', '800m', '1500m', '5000m', '110mh', '400mh', 'shot', 'discus', 'javelin', 'hj',
                  'pv', 'lj', 'tj', 'hammer')
        eventf = ('100m', '200m', '400m', '800m', '1500m', '5000m', '100mh', '400mh', 'shot', 'discus', 'javelin', 'hj',
                  'pv', 'lj', 'tj', 'hammer')
        if gender == 'm':
            event = eventm
        else:
            event = eventf

        for i in event:
            driver.get(f"https://www.athletic.net/TrackAndField/meet/{meetnum}/results/{gender}/1/{i}")
            goop = driver.page_source.split('<td _ngcontent-serverapp-c145="">') # removed ="">
            eve = i
            for i in goop[1::2]:
                temp = list()
                temp.append(eve)

                place = re.findall('([0-9]*)\.</td><td _n', i)
                try:
                    temp.append(place[0])
                except:
                    temp.append(place)

                grade = re.findall('nowrap;">(.+?)</td>', i)
                temp.append(grade[0])

                name = re.findall('Athlete.aspx\?AID=[0-9]*" class="ng-star-inserted">(.*?)</a>', i)
                temp.append(name[0])

                mark = re.findall('result/.*?">(.*?)<', i)
                if len(mark[0].strip()) <= 4:
                    # print(mark[0]) # Check to see if any marks are lost
                    continue
                temp.append(mark[0])

                markcomp = colmarkcomp(eve, mark[0])
                temp.append(round(float(markcomp), 2))

                school = re.findall('SchoolID=[0-9]*" class="ng-star-inserted">(.*?)</a>', i)
                temp.append(school[0])

                temp.append(collegeEventType(eve))

                if temp[-1] == 'T':
                    dataT.append(temp)
                else:
                    dataF.append(temp)

            datapdT = pd.DataFrame(dataT)
            datapdF = pd.DataFrame(dataF)

        # Parse
        if gender == 'm':
            path = fr'C:\Users\15037\PycharmProjects\PythonForEveryone\AthleticProject\APMale\CTrack{meetname}.csv'
        else:
            path = fr'C:\Users\15037\PycharmProjects\PythonForEveryone\AthleticProject\APFemale\CTrack{meetname}.csv'

        datapdT.to_csv(path, index=False)
        print(meetname, gender, 'track minted')

        if gender == 'm':
            path = fr'C:\Users\15037\PycharmProjects\PythonForEveryone\AthleticProject\APMale\CField{meetname}.csv'
        else:
            path = fr'C:\Users\15037\PycharmProjects\PythonForEveryone\AthleticProject\APFemale\CField{meetname}.csv'
        
        #Store
        datapdF.to_csv(path, index=False)
        print(meetname, gender, 'field minted')
