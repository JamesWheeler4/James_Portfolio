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
    email = 'webotis@gmail.com'
    password = 'Bqm4P8XrqwWH3uz'

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

    # Ending Script, might need to turn off
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


def markcalc(x, y):  # input will be (event[0], mark[0])
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


def nameswap(x):
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


def scoring(i):
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


def toptenfinal(dflist):
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


def topglob(gender, type):

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


def colmarkcomp(eve, mark):
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


def collegeEventType(x):
    run = ('100m', '200m', '400m', '800m', '1500m', '5000m', '110mh', '100mh', '400mh')
    field = ('shot', 'discus', 'javelin', 'hj', 'pv', 'lj', 'tj', 'hammer')

    for i in run:
        if x == i:
            return 'T'

    for i in field:
        if x == i:
            return 'F'


def collegeresults(query):
    PATH = r"C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    email = 'webotis@gmail.com'
    password = 'Bqm4P8XrqwWH3uz'

    # Login process
    driver.get("https://www.athletic.net/account/login")
    time.sleep(.8)
    login = driver.find_element(By.CLASS_NAME, 'athletic-modal--form-input')
    login.send_keys(email, Keys.TAB, password, Keys.RETURN)
    time.sleep(1.5)

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

        datapdF.to_csv(path, index=False)
        print(meetname, gender, 'field minted')

    # return data







'''Test Queries'''
# OrHSM = 'OrHSM', 118089, -1
# OrHSF = 'OrHSF', 118089, 1
# WaHSM = 'WaHSM', 118613, -1
# WaHSF = 'WaHSF', 118613, 1
# IdHSM = 'IdHSM', 116889, -1
# IdHSF = 'IdHSF', 116889, 1
# CaHSM = 'CaHSM', 116431, -1
# CaHSF = 'CaHSF', 116431, 1

# queries.extend((OrHSM, OrHSF))
# queries.extend((OrHSF, WaHSF, IdHSF))

# testAPpros(queries)

