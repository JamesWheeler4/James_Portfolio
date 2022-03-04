import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import glob
import time
import re

queries = list()


# Run All
def testAPpros(queries):
    df = login(queries)
    return df


# Login
def login(queries):
    PATH = r"C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    email = 'XXXXXXX@gmail.com'
    password = 'XXXXXXX'

    # Login process
    driver.get("https://www.athletic.net/account/login")
    time.sleep(.8)
    login = driver.find_element(By.CLASS_NAME, 'athletic-modal--form-input')
    login.send_keys(email, Keys.TAB, password, Keys.RETURN)
    time.sleep(1.5)

    for i in queries:
        name = (i[0])
        leagueq = i[1]
        gender = i[2]
        if gender > 0:  # Changing URL for Female
            leagueq = str(leagueq) + '&gender=f'
            gen = 'female'
        else:
            leagueq = leagueq
            gen = 'male'

        # Finding Data
        driver.get(f"https://www.athletic.net/TrackAndField/Division/Top.aspx?DivID={leagueq}")
        data = driver.page_source
        time.sleep(2)
        # Organizing data down to the page contents
        data = data.split('<div')
        chunk = None
        for i in data:
            if i.startswith(' class="table-responsive mTop5"'):
                chunk = i
            else:
                continue
        events = chunk.split('class="needed"')
        time.sleep(.5)

        # Print data to CSV
        running = list()
        field = list()
        df = gather(events)

        for lines in df:
            if lines[1] == 'R':
                running.append(lines)
            else:
                field.append(lines)
        runningdf = pd.DataFrame(running)
        fielddf = pd.DataFrame(field)

        if gender < 0:
            path = fr'C:\Users\15037\PycharmProjects\PythonForEveryone\AthleticProject\APMale\HTrack{name}.csv'
        else:
            path = fr'C:\Users\15037\PycharmProjects\PythonForEveryone\AthleticProject\APFemale\HTrack{name}.csv'

        runningdf.to_csv(path, index=False)
        print(name, gen, 'minted')

        if gender < 0:
            path = fr'C:\Users\15037\PycharmProjects\PythonForEveryone\AthleticProject\APMale\HField{name}.csv'
        else:
            path = fr'C:\Users\15037\PycharmProjects\PythonForEveryone\AthleticProject\APFemale\HField{name}.csv'

        fielddf.to_csv(path, index=False)
        print(name, gen, 'minted')

    # Ending Script, will keep window open to inspect 
    # while True:
    #     closer = input("Would you like to close Y/N: ")
    #     if closer.upper() == 'Y':
    #         driver.quit()
    #         quit()
    #     else:
    #         continue


def eventType(x):  # Determine what event type the each entry is to sort later
    eventR = ('100 Meters', '200 Meters', '400 Meters', '800 Meters', '1500 Meters', '1600 Meters',
              '3000 Meters', '3200 Meters', '110m Hurdles - 39"', '300m Hurdles - 36"', '100m Hurdles - 33"',
              '300m Hurdles - 30"')
    eventF = ('Shot Put - 12lb', 'Shot Put - 4kg', 'Discus - 1.6kg', 'Discus - 1kg', 'Javelin - 800g',
              'Javelin - 600g', 'High Jump', 'Pole Vault', 'Long Jump', 'Triple Jump', 'Hammer - 16lb',
              'Hammer - 4kg')

    for i in eventR:
        if i == x:
            return 'R'

    for i in eventF:
        if i == x:
            return 'F'


def markcalc(x, y):  # Input will be (event[0], mark[0]), Creates comparable mark metric 
    eventR = ('100 Meters', '200 Meters', '400 Meters', '800 Meters', '1500 Meters', '1600 Meters',
              '3000 Meters', '3200 Meters', '110m Hurdles - 39"', '300m Hurdles - 36"', '100m Hurdles - 33"',
              '300m Hurdles - 30"')
    eventF = ('Shot Put - 12lb', 'Shot Put - 4kg', 'Discus - 1.6kg', 'Discus - 1kg', 'Javelin - 800g',
              'Javelin - 600g', 'High Jump', 'Pole Vault', 'Long Jump', 'Triple Jump', 'Hammer - 16lb',
              'Hammer - 4kg')
    for i in eventR:
        if i == x:
            try:
                lst = y.split(':')
                markcomp = (int(lst[0]) * 60) + float(lst[1])
            except:
                markcomp = float(y)

    for i in eventF:
        if i == x:
            spl = y.split("'")
            inch = round(float(spl[1].strip()) / 12, 2)
            markcomp = int(spl[0]) + inch
    return round(markcomp, 2)


def nameswap(x):  # Used to simplify and correspond with college marks when combining
    dict = {'100 Meters': '100m', '200 Meters': '200m', '400 Meters': '400m', '800 Meters': '800m',
            '1500 Meters': '1500m', '100m Hurdles - 33"': '100mh', '110m Hurdles - 39"': '110mh',
            'Shot Put - 12lb': 'shot', 'Shot Put - 4kg': 'shot', 'Discus - 1.6kg': 'discus',
            'Discus - 1kg': 'discus', 'Javelin - 800g': 'javelin', 'Javelin - 600g': 'javelin',
            'High Jump': 'hj', 'Pole Vault': 'pv', 'Long Jump': 'lj', 'Triple Jump': 'tj',
            'Hammer - 16lb': 'hammer', 'Hammer - 4kg': 'hammer', '3000 Meters': '3000m',
            '300m Hurdles - 36"': '300mh', '1600 Meters': '1600m', '3200 Meters': '3200m',
            '300m Hurdles - 30"': '300mh'}
    for k, v in dict.items():
        if k == x:
            x = v
    return x


def gather(events):  # Parsing and gathering the entries
    df = list()
    p = list()

    # Gathering data
    for i in events[1:]:  # Splitting events
        sp = i.split('<td class="compareHide">')  # Dropping the metadata
        try:
            for j in sp:
                lp = list()
                if j.startswith('><tr><td'):  # Data split by event chunk
                    event = re.findall('.Event=[0-9]*&amp;type=4">(.*?)</a>', j)
                    eve = event[0]
                elif j.startswith('<input class="compareCheckbox'):  # Iterating through athlete entries (relay)
                    if eve == '4x100 Relay' or eve == '4x200 Relay' or eve == '4x400 Relay' or \
                            eve == '4x800 Relay' or eve.startswith('SMR') is True:
                        continue

                    else:  # Iterating through athlete entries (individual)
                        lp.append(event[0])
                        eType = eventType(lp[0])
                        # print(eType)
                        lp.append(eType)
                        # print(lp)


                        place = re.findall('."padding-left:0px;">([0-9]*)\.</td>', j)
                        if len(place) == 0:
                            place = p[0]
                        else:
                            p.insert(0, place)
                        lp.append(place[0])

                        grade = re.findall('.<td>(.+?)</td><td nowrap', j)
                        if len(grade) < 1:
                            grade = 'N/A'
                            lp.append(grade)

                        else:
                            lp.append(grade[0])

                        athid = re.findall('.Athlete\.aspx\?AID=([0-9]*)"', j)
                        lp.append(athid[0])

                        name = re.findall('.Athlete\.aspx\?AID=[0-9]*">(.*?)</a>', j)
                        lp.append(name[0])

                        mark = re.findall('./result/.+?">(.+?)<', j)
                        markcomp = markcalc(event[0], mark[0]) # input will be (event[0], mark[0])
                        lp.append(mark[0])
                        lp.append(markcomp)

                        loc = re.findall('School.aspx\?SchoolID=[0-9]*">(.*?)</a>', j)
                        if len(loc) < 1:
                            loc = 'N/A'
                            lp.append(loc)
                        else:
                            lp.append(loc[0])

                        locid = re.findall('School.aspx\?SchoolID=([0-9]*)">.*?</a>', j)
                        if len(locid) < 1:
                            locid = 'N/A'
                            lp.append(locid)
                        else:
                            lp.append(locid[0])
                        lp.append((nameswap(eve)))
                    df.append(lp)  # Adding all collected data to main list
                else:
                    print('skipped', j)
                    continue
        except:
            continue
    return df

