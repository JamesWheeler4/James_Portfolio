def meetGather(query):
    PATH = r"C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(url_login)
    time.sleep(.8)
    login = driver.find_element(By.CLASS_NAME, 'athletic-modal--form-input')
    login.send_keys(email, Keys.TAB, password, Keys.RETURN)
    time.sleep(2.5)

    conn = sqlite3.connect('APServer.sqlite')
    cur = conn.cursor()

    missed_events = list()

    for i in query:
        meetnum = i[0]
        gender_id = i[1]
        eventm = ('100m', '200m', '400m', '800m', '1500m', '5000m', '110mh', '400mh',
                  'shot', 'discus', 'javelin', 'hj', 'pv', 'lj', 'tj', 'hammer')
        eventf = ('100m', '200m', '400m', '800m', '1500m', '5000m', '100mh', '400mh',
                  'shot', 'discus', 'javelin', 'hj', 'pv', 'lj', 'tj', 'hammer')
        if gender_id == 1:
            events = eventf
            gender = 'f'
        else:
            events = eventm
            gender = 'm'

        for i in events:
            driver.get(url_meetGather1 + f'{meetnum}/results/{gender}/1/{i}')
            data_raw = driver.page_source.split('<td _ngcontent-serverapp-c145="">')
            time.sleep(1.5)
            for k in data_raw:
                data_a = k.split('\n')
                for j in data_a:
                    if not j.strip().startswith('<anet-site-app'): continue
                    label = re.findall('h4 _ngcontent-serverapp-c157="">(.+?)<!', j)
                    try:
                        label=label[0]
                    except:
                        a = meetnum, gender, i
                        missed_events.append(a)
                        continue
                    j = j.split('A ng-star-inserted')
                    for entry in j[1:]:
                        # print(label, entry)
                        cur2 = conn.cursor()
                        grade = re.findall('nowrap;">(.+?)</td>', entry)[0]
                        names = re.findall('class="ng-star-inserted">(.*?)</a>', entry)
                        name = names[0]
                        athlete_id = re.findall('lete.aspx\?AID=(.+?)"', entry)[0]
                        mark = re.findall('result/.*?">(.*?)<', entry)
                        if len(mark[0].strip()) <= 4:
                            print(mark[0], 'passing') # Check to see if any marks are lost
                            continue
                        markcomp = round(float(meetMarkCalc(i, mark[0])), 2)
                        location_id = re.findall('SchoolID=(.+?)"', entry)[0]
                        sqlevent_id = cur2.execute('''SELECT id FROM Event WHERE name = ? AND gender_id = ?''',
                                                   (i, gender_id))
                        try:
                            event_id = sqlevent_id.fetchone()[0]
                        except:
                            print(i, gender_id, 'no sql pull')
                        print(athlete_id, name, grade, gender_id, location_id, event_id, athlete_id, markcomp)

                        cur.execute('''INSERT OR IGNORE INTO Athlete (id, name, grade, gender_id, location_id)
                                                VALUES ( ?, ?, ?, ?, ? )''', (athlete_id, name, grade, gender_id, location_id))
                        cur.execute('''INSERT OR IGNORE INTO Result (event_id, athlete_id, mark)
                                                        VALUES ( ?, ?, ? )''', (event_id, athlete_id, markcomp))
                        conn.commit()

    for m in missed_events:
        print(m)
    Colcleanup(missed_events)
