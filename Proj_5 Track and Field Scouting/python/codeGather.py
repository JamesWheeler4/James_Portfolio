def codeGather():
    PATH = r"C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    # Login process
    conn = sqlite3.connect('APServer.sqlite')
    cur1 = conn.cursor()
    driver.get(url_login)
    time.sleep(.8)
    login = driver.find_element(By.CLASS_NAME, 'athletic-modal--form-input')
    login.send_keys(email, Keys.TAB, password, Keys.RETURN)
    time.sleep(1.5)

    # List can be added to
    states = ('Oregon', 'Washington', 'Idaho', 'Nevada')

    # Collects id_codes for given state back to 2012
    for state in states:
        cur1.execute('''INSERT OR IGNORE INTO State (name) VALUES ( ?)''', (state,))
        cur1.execute('''SELECT id FROM State WHERE name = ?''', (state,))
        state_id = cur1.fetchone()[0]

        driver.get(url_codeGather1 + f'{state}/')
        data = driver.page_source.split('h_Season_2')
        # print(data[1:12])
        for line in data[1:12]:
            id = re.findall('State=(.+?)"', line)[0]
            year = re.findall('>(.+?)</a', line)[0]
            # print(state_id, id, year)

            cur1.execute('''INSERT OR IGNORE INTO PreCode (id, state_id, year)
                                            VALUES ( ?, ?, ?)''',
                         (id, state_id, year))
            conn.commit()

    # Creating a list of id(state in a given year, state_id, and year to pull school codes from
    codes = list()
    for state in states:
        cur1.execute('''SELECT id FROM State WHERE name = ?''', (state,))
        state_id = cur1.fetchone()[0]
        cur1.execute('''SELECT * FROM PreCode WHERE state_id = ?''', (state_id,))
        code = cur1.fetchall()
        for line in code:
            codes.append(line)

    # Gathering
    for code in codes:
        driver.get(url_codeGather2 + f'{code[0]}/')
        data = driver.page_source.split('\n')
        for lines in data:
            state_id = code[1]
            '''Gathered State Information'''
            if lines.find(f'"title":"{state}"') > 0:
                id_state = re.findall('"id":(.+?),"title"', lines)[-1]
                cur1.execute('''SELECT id FROM Classification WHERE name = "State"''')
                class_id_state = cur1.fetchone()[0]
                div_id_state = 0
                dist_id_state = 0
                cur1.execute('''INSERT OR IGNORE INTO Codes 
                                    (id, name, division_id, district_id, classification_id, state_id, year)
                                VALUES ( ?, ?, ?, ?, ?, ?, ? )''',
                             (id_state, state, div_id_state, dist_id_state, class_id_state, state_id, code[2]))
                conn.commit()

            '''Gather Division Information'''
            if lines.find('font-size:140%') < 0: continue
            data_div = lines.split('font-size:140%')[1:]
            for j in data_div:
                divs = j.split('href=')[1]
                id_div = re.findall('DivID=(.+?)"', divs)[0]
                name_div = re.findall('>(.+?)<i class=', divs)[0].strip()
                cur1.execute('''SELECT id FROM Classification WHERE name = "Division"''')
                dist_id_div = 0
                class_id_div = cur1.fetchone()[0]
                cur1.execute('''INSERT OR IGNORE INTO Codes 
                                    (id, name, division_id, district_id, classification_id, state_id, year)
                                VALUES ( ?, ?, ?, ?, ?, ?, ? )''',
                             (id_div, name_div, id_div, dist_id_div, class_id_div, state_id, code[2]))
                conn.commit()
                '''Gathering District Information'''
                dists = j.split('href=')[2:]
                for line in dists:
                    '''Gathering Location Information'''
                    if line.find('School') > 0:
                        try:
                            id_loc = re.findall('SchoolID=(.+?)">', line)
                            name_loc = re.findall('"truncate">(.+?)</span>', line)
                            cur1.execute('''SELECT id FROM Classification WHERE name = "Location"''')
                            class_id_loc = cur1.fetchone()[0]
                            cur1.execute('''INSERT OR IGNORE INTO Codes
                                            (id, name, division_id, district_id, classification_id, state_id, year)
                                        VALUES ( ?, ?, ?, ?, ?, ?, ? )''',
                                         (
                                         int(id_loc[0]), name_loc[0], id_div, id_dist, class_id_loc, state_id, code[2]))
                            conn.commit()
                        except:
                            continue

                    '''Functions and gathers all District info'''
                    if line.find('School') > 0 or line.find('class="L4"') > 0: continue

                    id_dist = re.findall('DivID=(.+?)"', line)[0]
                    name_dist = re.findall('>(.+?)<i class=', line)[0]
                    cur1.execute('''SELECT id FROM Classification WHERE name = "District"''')
                    class_id_dist = cur1.fetchone()[0]
                    cur1.execute('''INSERT OR IGNORE INTO Codes 
                                        (id, name, division_id, district_id, classification_id, state_id, year)
                                    VALUES ( ?, ?, ?, ?, ?, ?, ? )''',
                                 (id_dist, name_dist, id_div, id_dist, class_id_dist, state_id, code[2]))

                    conn.commit()
            time.sleep(1.5)

    print('Codes gathered')
