# Calculating and formatting r and r^2 when comparing events
def graphCorData():
    # Connects to server
    conn = sqlite3.connect('APServer.sqlite')
    cur = conn.cursor()

    # Creates list of all event id, gender, and event name called 'events'
    set_up_q = '''SELECT Event.id, Gender.name, Event.name
                    FROM Event JOIN Gender ON Event.gender_id = Gender.id
                    ORDER BY Event.type_id, Event.id'''
    cur.execute(set_up_q)
    events = cur.fetchall()  # Ex. (1, 'Male', '100m')

    # Setting up csv to write into
    with open('Female_testing0.csv', 'w', newline='') as f:
        writer = csv.writer(f)

        # Writing my headers
        headers = list()
        headers.append("event")
        for head in events:
            if head[1] == "Male": continue  # Isolates just Mens to graph
            header = head[2]
            headers.append(header)
        writer.writerow(headers)

        # Creating
        for event_base in events:
            if event_base[1] == "Male": continue  # Isolates just Mens to graph

            eve_base = f'''SELECT athlete_id, AVG(mark) AS avg_mark, State.name
                            FROM Full_Result
                            JOIN Athlete ON Full_Result.athlete_id = Athlete.id
                            JOIN Location ON Athlete.location_id = Location.id
                            JOIN State ON Location.state_id = State.id
                            JOIN Event ON Full_Result.event_id = Event.id
                            WHERE event_id = {event_base[0]} 
                            GROUP BY athlete_id'''
                            # AND State.name = "{state}"
            data_base = pd.read_sql(eve_base, conn)

            items = list()  # Creates list to be turned into csv row
            row_label = event_base[2]  # Labeling each row with given event
            items.append(row_label)  # Adds event to csv list

            for event in events:  # Setting first event(base_event) for iteration

                # Collecting event type for future inversion comparison
                base_type_q = f'''SELECT Event.type_id
                                    FROM Event
                                    WHERE id = {event_base[0]}'''
                cur.execute(base_type_q)
                base_type = cur.fetchone()[0]

                check = 1
                if row_label == event[2]:  # Fills gap in self comparison (100m vs. 100m)
                    items.append('N/A')
                    continue
                if event_base[0] == event[0]: continue  # Skipping comparing to self
                if event_base[1] != event[1]: continue  # Skipping crossed gender comparisons

                # Setting second event(comp_event) for iteration
                comp = f'''SELECT athlete_id, AVG(mark) AS avg_mark
                        FROM Full_Result WHERE event_id = {event[0]} GROUP BY athlete_id'''
                data_comp = pd.read_sql(comp, conn)
                data_full = data_base.merge(data_comp, on='athlete_id')

                # Collecting event type for future inversion comparison
                comp_type_q = f'''SELECT Event.type_id
                                    FROM Event
                                    WHERE id = {event[0]}'''
                cur.execute(comp_type_q)
                comp_type = cur.fetchone()[0]

                # Dropping datasets with <10 entries (sample too small)
                if len(data_full) < 10:
                    if check == 1: items.append('N/A')  # currently error with double entry of N/A for 1600 and 3200 (simple fix in excel)
                    continue

                # Consolidating variables for computation
                x = data_full.avg_mark_x
                y = data_full.avg_mark_y

                # Correlation Coefficient / R
                r_num = round(np.corrcoef(x, y)[0, 1], 4)

                if base_type + comp_type == 3:  # Inverting sign of correlation coefficient for comparison
                    r_num = -1*r_num

                print(row_label, event[2], r_num, base_type, comp_type)  # Checking outputs
                items.append(r_num)  # Adding to csv list

            writer.writerow(items)  # Writing csv list to csv
    f.close()  # Closing csv

    df = pandas.read_csv('Female_testing0.csv')
    print(df)
