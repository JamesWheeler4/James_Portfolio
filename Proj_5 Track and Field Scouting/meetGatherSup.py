def meetMarkCalc(x, y):
    run = ('100m', '200m', '400m', '800m', '1500m', '5000m', '110mh','100mh', '400mh')
    field = ('shot', 'discus', 'javelin', 'hj', 'pv', 'lj', 'tj', 'hammer')

    for i in run:
        if i == x:
            try:
                strip = y.strip().split(':')
                sec = strip[1]
                min = int(strip[0]) * 60
                markcomp = min + float(sec[0:5])
                return markcomp
            except:
                markcomp = (y.strip())
                return markcomp[:-1]
    for i in field:
        if i == x:
            try:
                s = y.strip()
                markcomp = round(float(s[:-1]) * 3.28084, 2)
                return markcomp
            except:
                markcomp = y
                return markcomp
              

def meetCleanUp(m):
    done = False
    while not done:
        PATH = r"C:\Program Files (x86)\chromedriver.exe"
        driver = webdriver.Chrome(PATH)
        driver.get(url_login)
        time.sleep(.8)
        login = driver.find_element(By.CLASS_NAME, 'athletic-modal--form-input')
        login.send_keys(email, Keys.TAB, password, Keys.RETURN)
        time.sleep(1.5)

        conn = sqlite3.connect('APServer.sqlite')
        cur = conn.cursor()

        for i in m:
            meetnum = i[0]
            gender = i[1]
            event_name = i[2]
            missed_events = list()
            driver.get(url_meetCleanUp1 + f'{meetnum}/results/{gender}/1/{event_name}')
            data_raw = driver.page_source.split('<td _ngcontent-serverapp-c145="">')
            time.sleep(1.5)
            cur2 = conn.cursor()
            if gender == 'f':
                gender_id = 1
            else:
                gender_id = 2
            sqlevent_id = cur2.execute('''SELECT id FROM Event WHERE name = ? AND gender_id = ?''',
                                       (event_name, gender_id))
            try:
                event_id = sqlevent_id.fetchone()[0]
            except:
                print(event_name, gender_id, 'no sql pull')
            for k in data_raw:
                data_a = k.split('\n')
                for j in data_a:
                    if not j.strip().startswith('<anet-site-app'): continue
                    label = re.findall('h4 _ngcontent-serverapp-c157="">(.+?)<!', j)
                    try:
                        label = label[0]
                        m.pop(0)
                    except:
                        a = meetnum, gender_id, event_name
                        missed_events.append(a)
                    j = j.split('A ng-star-inserted')
                    for entry in j[1:]:
                        grade = re.findall('nowrap;">(.+?)</td>', entry)[0]
                        names = re.findall('class="ng-star-inserted">(.*?)</a>', entry)
                        name = names[0]
                        athlete_id = re.findall('lete.aspx\?AID=(.+?)"', entry)[0]
                        mark = re.findall('result/.*?">(.*?)<', entry)
                        if len(mark[0].strip()) <= 4:
                            print(mark[0], 'passing')  # Check to see if any marks are lost
                            continue
                        markcomp = round(float(meetMarkCalc(event_name, mark[0])), 2)
                        location_id = re.findall('SchoolID=(.+?)"', entry)[0]

                        # print(athlete_id, name, grade, gender_id, location_id, event_id, athlete_id, markcomp)

                        cur.execute('''INSERT OR IGNORE INTO Athlete (id, name, grade, gender_id, location_id)
                                                VALUES ( ?, ?, ?, ?, ? )''',
                                    (athlete_id, name, grade, gender_id, location_id))
                        cur.execute('''INSERT OR IGNORE INTO Result (event_id, athlete_id, mark)
                                                        VALUES ( ?, ?, ? )''', (event_id, athlete_id, markcomp))
                        conn.commit()
        print(m)
        if len(m) == 0:
            done = True
