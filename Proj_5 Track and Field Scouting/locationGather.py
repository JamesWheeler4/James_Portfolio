def locationGather():
    # Login process
    PATH = r"C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(url_login)
    time.sleep(.8)
    login = driver.find_element(By.CLASS_NAME, 'athletic-modal--form-input')
    login.send_keys(email, Keys.TAB, password, Keys.RETURN)
    time.sleep(1.5)

    conn = sqlite3.connect('APServer.sqlite')
    cur = conn.cursor()

    # Collecting HS location for Club Athletes
    athid = cur.execute('SELECT id FROM Athlete WHERE location_id = 0')
    for lines in athid:
        aid = lines[0]
        driver.get(url_locationGather1 + f'{aid}&L=4')
        data = driver.page_source.split('<')
        cur2 = conn.cursor()
        for idx, line in enumerate(data):
            if not line.strip().startswith('a _ngcontent-serverapp-c12'): continue
            if line.find('TrackAndField') < 0: continue
            print(idx, line)
            lid = int(re.findall('aspx\?SchoolID=(.+?)"', line)[0])
            print(type(aid), type(lid))
            cur2.execute('''UPDATE Athlete SET location_id = ? WHERE id = ?''', (lid, aid))
        conn.commit()
        try:
            print(aid, lid, 'updated')
        except:
            continue

    # Collecting information for HS Athletes
    cur.execute('SELECT DISTINCT location_id FROM Athlete')
    locid = cur.fetchall()
    total = len(locid)
    count = 0
    for lines in locid:
        count += 1
        lid = lines[0]
        try:
            cur.execute(('SELECT name FROM Location WHERE id = ?'), (lid,))
            data = cur.fetchone()[0]
            print(data, 'found in database')
            continue
        except:
            pass
        if lid == 0: continue
        driver.get(url_locationGather2 + f'{lid}')
        data = driver.page_source.split('\n')
        for line in data:
            cur2 = conn.cursor()
            if not line.strip().startswith('.constant("initial'): continue
            line = line.split('}')[0]
            name = re.findall('"Name":"(.+?)"', line)
            level = int(re.findall('"Level":(.+?),', line)[0])
            address = re.findall('"Address":"(.+?)"', line)
            city = re.findall('"City":"(.+?)"', line)
            state = re.findall('"State":"(.+?)"', line)[0]
            cur2.execute('''SELECT id FROM State WHERE abbrev = ?''', (state,))
            state_id = int(cur2.fetchone()[0])
            zip = re.findall('"ZipCode":"(.+?)"', line)
            phone = re.findall('"Phone":"(.+?)"', line)
            fax = re.findall('"Fax":"(.+?)"', line)
            url = re.findall('"URL":"(.+?)"', line)
            variables = (lid, name, level, address, city, state_id, zip, phone, fax, url)
            variable = list()
            for i in variables:
                try:
                    if len(i) < 1:
                        i = ''
                    variable.append(i[0])
                except:
                    variable.append(i)
            cur2.execute('''INSERT OR IGNORE INTO Location (id, name, level_id, address, city, state_id, zip, phone, fax, url)
                            VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )''',
                         (variable[0], variable[1], variable[2], variable[3], variable[4], variable[5], variable[6],
                          variable[7], variable[8], variable[9]))
            conn.commit()
            print(variable[1], 'saved', round((count/total)*100, 2), '% complete')
