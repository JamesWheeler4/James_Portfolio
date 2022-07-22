def topGather(queries):
    '''queries formatting (
    SELECT Codes.id, Gender.id
    FROM Codes JOIN Gender
    WHERE Codes.classification_id = 3
    ) no ON gives each gender_id for each codes_id
    '''

    PATH = r"C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(url_login)
    time.sleep(.8)
    login = driver.find_element(By.CLASS_NAME, 'athletic-modal--form-input')
    login.send_keys(email, Keys.TAB, password, Keys.RETURN)
    time.sleep(1.5)

    length = len(queries)
    complete = 0
    for i in queries:
        leagueq = i[0]
        gender = i[1]
        if gender == 1:  # Changing URL for Female
            leagueq = str(leagueq) + '&gender=f'
            genid = 1
        else:
            leagueq = leagueq
            genid = 2
        driver.get(url_topGather1 + f'{leagueq}')
        data = driver.page_source.split('colspan="9"')
        conn = sqlite3.connect('APServer.sqlite')
        cur = conn.cursor()
        print(i[0])
        cur.execute("SELECT year FROM Codes WHERE id = ?", (i[0],))
        year = cur.fetchone()[0]
        print(year)

        # input('Next?')

        for lines in data[1:]:  # Splits by Event
            try:
                event = re.findall('.Event=[0-9]*&amp;type=4">(.*?)</a>', lines)[0]
            except:
                event = re.findall('.Event=[0-9]*">(.*?)</a>', lines)[0]
            if event.startswith('4x') is True or event.startswith('SMR') is True or event.find('Relay') > 0:
                continue
            try:
                etype = int(topEventType(event))
                eve = topNameSwap(event)
            except:
                continue

                # Testing ------------------------------------------------------------------------

            try:
                eventid = int(re.findall('.Event=(.*?)&amp;type=4">.*?</a>', lines)[0])
            except:
                eventid = int(re.findall('.Event=(.*?)">.*?</a>', lines)[0])
            # print(eventid, eve, etype, genid)
            cur.execute('''INSERT OR IGNORE INTO Event (id, name, type_id, gender_id)
                        VALUES ( ?, ?, ?, ? )''', (eventid, eve, etype, genid))

            entry = lines.split('"padding-left:0px;"')
            for j in entry[1:]:  # Split by Entry in given Event
                try:
                    athid = re.findall('.Athlete\.aspx\?AID=([0-9]*)"', j)[0]
                    name = re.findall('.Athlete\.aspx\?AID=[0-9]*">(.*?)</a>', j)[0]
                    grade = re.findall('.<td>(.+?)</td><td nowrap', j)
                    mark = re.findall('./result/.+?">(.+?)<', j)
                    markcomp = topMarkCalc(event, mark[0])
                    try:
                        locid = int(re.findall('School.aspx\?SchoolID=([0-9]*)">.*?</a>', j)[0])
                    except:
                        locid = 0
                    try:
                        grade = int(grade[0])
                    except:
                        if grade == '15-16':
                            grade = 10
                        else:
                            grade = 12
                    cur.execute('''INSERT OR IGNORE INTO Athlete (id, name, gender_id, location_id)
                                    VALUES ( ?, ?, ?, ? )''', (athid, name, genid, locid))
                    cur.execute('''INSERT OR IGNORE INTO Result (event_id, athlete_id, mark, grade, year)
                                            VALUES ( ?, ?, ?, ?, ? )''', (eventid, athid, markcomp, grade, year))

                    conn.commit()

                except:
                    print('passed', event, athid)
                    print(athid, name, genid, locid, eventid, markcomp, grade, year)
                    input("next?")
                    continue
        complete += 1
        print(i, 'Saved')
        print("Percent complete:", round(100*(complete/length), 2))
        time.sleep(1.5)
