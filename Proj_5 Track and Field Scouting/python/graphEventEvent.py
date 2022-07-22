def graphEventEvent():  # Updated 7/6/22 (swapped to plotly from matplotlib)
    # Connects to server
    conn = sqlite3.connect('APServer.sqlite')
    cur = conn.cursor()

    # Creates list of all event id, gender, and event name called 'events'
    set_up_q = '''SELECT Event.id, Gender.name, Event.name
                       FROM Event JOIN Gender ON Event.gender_id = Gender.id
                       ORDER BY Event.type_id, Event.id'''
    cur.execute(set_up_q)
    events = cur.fetchall()  # Ex. (1, 'Male', '100m')

    for event_base in events:  # Pulling df of base (x)
        eve_base = f'''SELECT athlete_id, AVG(mark) AS avg_mark, State.name
                        FROM Full_Result
                        JOIN Athlete ON Full_Result.athlete_id = Athlete.id
                        JOIN Location ON Athlete.location_id = Location.id
                        JOIN State ON Location.state_id = State.id
                        WHERE event_id = {event_base[0]}
                        GROUP BY athlete_id'''

        data_base = pd.read_sql(eve_base, conn)
        for event in events:

            if event_base[0] == event[0]: continue  # Skipping comparing to self
            if event_base[1] != event[1]: continue  # Skipping crossed gender comparisons

            # Pulling data of comp (y)
            comp_type_q = f'''SELECT athlete_id, AVG(mark) AS avg_mark
                    FROM Full_Result WHERE event_id = {event[0]} GROUP BY athlete_id'''
            data_1 = pd.read_sql(comp_type_q, conn)

            new = data_base.merge(data_1, on='athlete_id')
            if len(new) < 10:
                continue

            # Cleaning variables of desired data for calculations
            x = new.avg_mark_x
            y = new.avg_mark_y

            # Calculations
            r_num = round(np.corrcoef(x, y)[0, 1], 4)
            res = stats.linregress(x, y)
            r_sqtest = f'{res.rvalue ** 2:.6f}'
            r_sq = f'{round(float(r_sqtest), 4)}'

            # Cleaning final variables
            base_title = event_base[2]
            comp_title = event[2]
            gender = event[1]
            state = new.name
            n = str(len(new))

            # Creating/editing fig
            fig = px.scatter(new, x=x, y=y, color=state, trendline='ols')
            fig.update_xaxes(title=f'{base_title}')
            fig.update_yaxes(title=f'{comp_title}')
            fig.update_layout(title=f"{gender}'s {base_title} vs. {comp_title} "
                                    f"<br><sup>Overall R={r_num} R^2={r_sq} n={n}</sup>", title_x=0.5,
                                    title_font_size=32, paper_bgcolor='#f4f0e4',plot_bgcolor='#f4f0e4',
                                    legend_title='State')
            fig.update_traces(hoverinfo='x+y')

            # Saving fig
            plotly.offline.plot(fig, filename=f"images/{gender}'s {base_title} vs. {comp_title}.html")
            time.sleep(1)
            # input('Next?')
            # plt.show()
        # print(saved)
