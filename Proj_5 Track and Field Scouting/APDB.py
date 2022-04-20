def buildAPDB():
    conn = sqlite3.connect('APServer.sqlite')
    cur = conn.cursor()

    # Building
    cur.executescript('''

    CREATE TABLE IF NOT EXISTS Athlete (
        id     INTEGER NOT NULL PRIMARY KEY UNIQUE,
        name   TEXT ,
        grade  INTEGER,
        gender_id INTEGER,
        location_id INTEGER
    );

    CREATE TABLE IF NOT EXISTS Location (
        id     INTEGER NOT NULL PRIMARY KEY UNIQUE,
        name   TEXT,
        level_id INTEGER,
        address TEXT,
        city   TEXT,
        state_id    INTEGER,
        zip    TEXT,
        phone  TEXT,
        fax    TEXT,
        url    TEXT
    );

    CREATE TABLE IF NOT EXISTS Level (
        id      INTEGER NOT NULL PRIMARY KEY UNIQUE,
        name    TEXT
    );

    INSERT OR IGNORE INTO Level (id, name)
        VALUES (4, "High School"), (16, "Track Club"), (8, "College");

    CREATE TABLE IF NOT EXISTS Event (
        id      INTEGER NOT NULL PRIMARY KEY UNIQUE,
        name    TEXT,
        type_id INTEGER,
        gender_id INTEGER
    );

    INSERT OR IGNORE INTO Event (id, name, type_id, gender_id)
        VALUES (7, '5000m', 1, 2), (25, '5000m', 1, 1), (15, 'hammer', 2, 2), (33, 'hammer', 2, 1),
                (40, '400mh', 1, 1), (41, '400mh', 1, 2);

    CREATE TABLE IF NOT EXISTS Type (
        id      INTEGER NOT NULL PRIMARY KEY UNIQUE,
        name    TEXT UNIQUE
    );

    INSERT OR IGNORE INTO Type (name)
        VALUES ("Track"), ("Field");

    CREATE TABLE IF NOT EXISTS Gender (
        id      INTEGER NOT NULL PRIMARY KEY UNIQUE,
        name    TEXT UNIQUE
    );

    INSERT OR IGNORE INTO Gender (name)
        VALUES ("Female"), ("Male");

    CREATE TABLE IF NOT EXISTS Result (
        event_id    INTEGER,
        athlete_id  INTEGER,
        mark        INTEGER,
        PRIMARY KEY (event_id, athlete_id)
    );

    CREATE TABLE IF NOT EXISTS Full_Result (
        event_id    INTEGER,
        athlete_id  INTEGER,
        date        TEXT,
        year        INTEGER,
        mark        INTEGER,
        PRIMARY KEY (event_id, athlete_id, date)
    );

     CREATE TABLE IF NOT EXISTS State (
        id      INTEGER NOT NULL PRIMARY KEY UNIQUE,
        name    TEXT UNIQUE,
        abbrev  TEXT
    );

    INSERT OR IGNORE INTO State (id, name, abbrev)
        VALUES (1, "Oregon", "OR"), (2, "Washington", "WA"), (3, "Idaho", "ID"), (4, "Nevada", "NV"), 
        (5, "California", "CA"), (6, "Indiana", "IN"), (7, "Utah", "UT"), (8, "Alabama", "AL"),
        (9, "Georgia", "GA");

     CREATE TABLE IF NOT EXISTS Classification (
        id      INTEGER NOT NULL PRIMARY KEY UNIQUE,
        name    TEXT UNIQUE
    );

    INSERT OR IGNORE INTO Classification (name)
        VALUES ("State"), ("Division"), ("District"), ("Location");

     CREATE TABLE IF NOT EXISTS Codes (
        id      INTEGER NOT NULL PRIMARY KEY UNIQUE,
        name    TEXT,
        division_id INTEGER,
        district_id INTEGER,
        classification_id INTEGER,
        state_id INTEGER
    )

    ''')
    print('APDB BUILT')

def dropAPDB():
    conn = sqlite3.connect('APServer.sqlite')
    cur = conn.cursor()

    cur.executescript('''
    DROP TABLE IF EXISTS Athlete;
    DROP TABLE IF EXISTS Location;
    DROP TABLE IF EXISTS Level;
    DROP TABLE IF EXISTS Event;
    DROP TABLE IF EXISTS Type;
    DROP TABLE IF EXISTS Gender;
    DROP TABLE IF EXISTS Result;
    DROP TABLE IF EXISTS Full_Result;
    DROP TABLE IF EXISTS State;
    DROP TABLE IF EXISTS Classification;
    DROP TABLE IF EXISTS Codes;
    ''')
    print('APDB CLEARED')
