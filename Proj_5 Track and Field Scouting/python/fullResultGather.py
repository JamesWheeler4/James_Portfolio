def fullResultgather():
    conn = sqlite3.connect('APServer.sqlite')
    cur = conn.cursor()

    cur.execute('''SELECT id, type_id FROM Event''')
    event_id = cur.fetchall()

    top_athlete_id = list()
    for i in event_id:
        if i[1] == 1:
            cur.execute(('''SELECT Result.athlete_id, Result.mark, Event.gender_id FROM Result JOIN Event ON
                            Result.event_id = Event.id WHERE event_id = ? ORDER BY mark LIMIT 200'''), (i[0],))
        else:
            cur.execute(('''SELECT Result.athlete_id, Result.mark, Event.gender_id FROM Result JOIN Event ON
                            Result.event_id = Event.id WHERE event_id = ? ORDER BY mark DESC LIMIT 200'''), (i[0],))
        test = cur.fetchall()
        for j in test:
            top_athlete_id.append(j)

    PATH = r"C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(url_login)
    time.sleep(.8)
    login = driver.find_element(By.CLASS_NAME, 'athletic-modal--form-input')
    login.send_keys(email, Keys.TAB, password, Keys.RETURN)
    time.sleep(2.5)

    total = len(top_athlete_id)
    count = 0
    # skiplist = []
    for k in top_athlete_id:
        count += 1
        if (k[0] in skiplist):
            continue

        # Skipping entries already found
        try:
            cur.execute(('SELECT athlete_id FROM Full_Result WHERE athlete_id = ?'), (k[0],))
            data = cur.fetchone()[0]
            # print(data, 'found in database')
            # skiplist.append(data)
            # print(len(skiplist))
            continue
        except:
            print(k, 'outside db -------------------')
            pass

        # Skips over broken webpages
        broken = False
        skips = (13511981, 5612886, 14392584, 16280418)
        for skip in skips:
            if skip == k[0]: broken = True
        if broken == True: continue

        # Pulling all the data from each athletes personal page
        driver.get(url_fullResultGather1 + f"AID={k[0]}&L=4")
        time.sleep(2)
        data = driver.page_source.split('\n')

        # Parsing the pulled data
        for l in data:
            if l.find('card-block px-2 pt-2 pb-0 in collapse') < 0: continue
            year_raw = re.findall('season_(.+?)"', l)[0]
            if year_raw.startswith('1'):
                year = year_raw[1:5]
            else:
                year = year_raw[0:4]
            m = l.split('<h5')
            if int(year) < 2008:
                print(year, 'too old')
                continue
            for n in m:
                if not n.startswith('>'): continue
                event_raw = re.findall('>(.+?)</h5>', n)[0]
                if event_raw.find('<') > 0:
                    cut = re.split('(<.+?>)', event_raw)
                    event_raw = cut[0] + cut[2]
                event_swap = topNameSwap(event_raw)
                cur.execute(('SELECT id FROM Event WHERE name = ? AND gender_id = ?'), (event_swap, k[2]))
                try:
                    event_id = cur.fetchone()[0]
                except:
                    continue
                o = n.split('<i>')
                for p in o[1:]:
                    mark_raw = 0
                    try:
                        mark_raw = re.findall('result/.+?">(.+?)<', p)[0]
                        mark = topMarkCalc(event_raw, mark_raw)
                    except:
                        continue
                    date_raw = re.findall('style="width: 60px;">(.+?)</td>', p)[0] + ' ' + year
                    date = datetime.strptime(date_raw, '%b %d %Y').date()
                    cur.execute('''INSERT OR IGNORE INTO Full_Result (event_id, athlete_id, date, year, mark)
                                    VALUES ( ?, ?, ?, ?, ? )''', (event_id, k[0], date, year, mark))

                    conn.commit()
        perc = round(((count / total) * 100), 2)
        print(f'{perc}%')
