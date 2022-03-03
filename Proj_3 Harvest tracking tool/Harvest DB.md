## Harvest Project MySQL notebook

### Making database

CREATE DATABASE harvest_project;

USE harvest_project;

### Creating tables

CREATE TABLE field_info (
field_id CHAR(3),
field_name VARCHAR(20),
field_acres int,
field_crop VARCHAR(20),
field_variety VARCHAR(20),
field_planted int,
field_historic int,
field_goal int,
field_address VARCHAR(50),
field_latitude VARCHAR(10),
field_longitude VARCHAR(10)
);


CREATE TABLE harvest (
harvest_field_id CHAR(3),
harvest_pounds int,
harvest_date DATE
);


CREATE TABLE cost (
cost_crop VARCHAR(20),
cost_fixed int,
cost_harvest_hour int
);

CREATE TABLE acres (
acres_crop VARCHAR(20),
acres_completed int,
acres_date DATE
);

CREATE TABLE hours (
hours_crop VARCHAR(20),
hours_harvesting int,
hours_date DATE
);

CREATE TABLE team (
team_id CHAR(3),
team_rating int,
team_date DATE
);

ALTER TABLE field_info
MODIFY field_planted CHAR(4);


### Adding sample data

INSERT INTO field_info (
field_id, field_name, field_acres, field_crop, 
field_variety, field_planted, field_historic, 
field_goal, field_address, field_latitude, field_longitude
) 
VALUES
	(
		'001' , 'Jensen West' , 50000, 'Tall Fescue' , 'Griffin' , '2018 ', 2048, 2200 , '3158 Tincidunt Ave' , '37.64197' , '108.31591'
	),(
		'002', 'Jensen East', 52000, 'Tall Fescue', 'Griffin', '2017',1958,2200, '4917 Mauris St.', '38.41713', '110.22463'
	),(
		'003', 'Chandler North',20000, 'Rye', 'Mccarthy', '2019',2025,2100, '659-5805 Eu Street', '38.75847', '111.20352'
	),(
		'004', 'Chandler South',12000, 'Rye', 'Patton', '2016',1856,2000, '786-7592 Nec St.', '39.73564', '113.24467'
	),(
		'005', 'Hunter 1',8000, 'Rye', 'Lindsay', '2015',1821,2000, '351-3648 Et, St.', '47.88749', '114.11515'
	),(
		'006', 'Hunter 2',5400,'Rye', 'Lindsay', '2019',1563,2000, '1027 Ornare Avenue', '48.67543', '121.38371'
	),(
		'007', 'Hunter 3',20000,'Rye', 'Lindsay', '2018',1478,2000, '636-8926 Sem St.', '49.1287', '123.22147'
	),(
		'008', 'Lemondrop',25000, 'Tall Fescue', 'Cervantes', '2018', 1854,2100, '189-5838 Duis St.', '52.59378', '125.80603'
	),(
		'009', 'Highway' ,3500, 'Tall Fescue', 'Oconnor', '2016',1954, 2100, '1791 Donec Street', '53.92373', '126.60008'
	),(
		'010', 'Camera North',4680, 'Tall Fescue', 'Haney', '2015',1745,2000, '925-3664 Integer Rd.', '55.53132', '126.98958'
	);

INSERT INTO harvest (
harvest_field_id, harvest_pounds, harvest_date
)
VALUES
(
	'001', 22500, '2021-09-18'
    ),(
    '001', 24150, '2021-09-18'
    ),(
    '001', 24856, '2021-09-18'
    ),(
    '001', 21456, '2021-09-18'
    ),(
    '001', 23458, '2021-09-18'
    ),(
    '002', 26584, '2021-09-19'
    ),(
    '002', 21458, '2021-09-19'
    ),(
    '002', 23548, '2021-09-19'
    ),(
    '002', 21456, '2021-09-19'
    ),(
    '002', 23578, '2021-09-19'
    ),(
    '003', 25895, '2021-09-20'
    ),(
    '007', 25478, '2021-09-20'
    ),(
    '007', 23698, '2021-09-20'
    ),(
    '005', 24856, '2021-09-20'
    );

INSERT INTO acres  (
acres_crop, acres_completed, acres_date
)
VALUES
(
	'tall_fescue', 50000, '2021-09-18'
    ),(
    'tall_fescue', 52000, '2021-09-19'
    ),(
    'rye', 41000, '2021-09-20'
    );

INSERT INTO hours (
hours_tall_fescue, hours_rye, hours_garlic, hours_hazelnut, hours_date
)
VALUES
(
	10, 0, 0, 0, '2021-09-18'
    ),(
    11, 0, 0, 0, '2021-09-19'
    ),(
    0, 8, 0, 0, '2021-09-20'
    );

### Fixing duplication mistake

##### Duplicated harvest multiple times

DELETE FROM harvest

##### Rerun harvest sample data, continue

INSERT INTO cost (
cost_crop, cost_fixed, cost_harvest_hour
)
VALUES
(
	'tall_fescue' , 500000, 200000
    ),(
    'rye', 400100, 200100
    ),(
    'garlic', 1200000, 250000
    ),(
    'hazelnut', 200000, 50000
    );

### Recreating hours table

CREATE TABLE hours (
hours_tall_fescue int,
hours_rye int, 
hours_garlic int,
hours_hazelnut int,
hours_date DATE
)

DROP TABLE hours;

INSERT INTO team (
team_id, team_rating, team_date
)
VALUES
(
	'STB', 8, '2021-09-18'
    ),(
    'WRB', 7, '2021-09-18'
    ),(
    'CTO', 10, '2021-09-18'
    ),(
    'VAV', 6, '2021-09-18'
    ),(
    'AFO', 8, '2021-09-18'
    ),(
    'CTB', 4, '2021-09-18'
    ),(
	'STB', 9, '2021-09-19'
    ),(
    'WRB', 7, '2021-09-19'
    ),(
    'CTO', 10, '2021-09-19'
    ),(
    'VAV', 7, '2021-09-19'
    ),(
    'AFO', 7, '2021-09-19'
    ),(
    'CTB', 5, '2021-09-19'
    ),(
    'STB', 7, '2021-09-20'
    ),(
    'WRB', 7, '2021-09-20'
    ),(
    'CTO', 10, '2021-09-20'
    ),(
    'VAV', 9, '2021-09-20'
    ),(
    'AFO', 9, '2021-09-20'
    ),(
    'CTB', 4, '2021-09-20'
    );

### Adding crop table

##### Adding a crop table so that it can be a PK reference with total acres and goal hours

CREATE TABLE crop (
crop VARCHAR(20),
crop_acres_total int,
crop_hours_goal int
);

INSERT INTO  crop (
crop, crop_acres_total, crop_hours_goal
)
VALUES
(
	'tall_fescue', 220000, 3000
    ),(
    'rye', 180000, 3000
    ),(
    'garlic', 10000, 1200
    ),(
    'hazelnut', 19500, 1500
    );

### Adding primary and foreign keys
##### Making all of my PK and FK to link my tables

##### PK field_info.field_id		FK harvest.harvest_field_id
##### PK crop.crop				FK field_info.field_crop, cost.cost_crop, acres.acres_crop
##### PK hours.hours_date			FK harvest.harvest_date, acres.acres_date, team.team_date

ALTER TABLE field_info
ADD CONSTRAINT PK_field_info PRIMARY KEY (field_id);

ALTER TABLE crop
ADD CONSTRAINT PK_crop PRIMARY KEY (crop);

ALTER TABLE hours
ADD CONSTRAINT PK_hours PRIMARY KEY (hours_date);

ALTER TABLE harvest
ADD CONSTRAINT FK_harvest_field_id
FOREIGN KEY (harvest_field_id) REFERENCES field_info(field_id);

ALTER TABLE field_info
ADD CONSTRAINT FK_field_crop
FOREIGN KEY (field_crop) REFERENCES crop(crop);

ALTER TABLE cost
ADD CONSTRAINT FK_cost_crop
FOREIGN KEY (cost_crop) REFERENCES crop(crop);

ALTER TABLE acres
ADD CONSTRAINT FK_acres_crop
FOREIGN KEY (acres_crop) REFERENCES crop(crop);

ALTER TABLE harvest
ADD CONSTRAINT FK_harvest_date
FOREIGN KEY (harvest_date) REFERENCES hours(hours_date);

ALTER TABLE acres
ADD CONSTRAINT FK_acres_date
FOREIGN KEY (acres_date) REFERENCES hours(hours_date);

ALTER TABLE team
ADD CONSTRAINT FK_team_date
FOREIGN KEY (team_date) REFERENCES hours(hours_date);

### Fixing table formatting
##### Tables have differing format

UPDATE field_info
SET
	field_crop = REPLACE(field_crop, 'Rye', 'rye');

UPDATE field_info
SET
	field_crop = REPLACE(field_crop, 'Tall Fescue', 'tall_fescue');
	
### Changing the format of acres table

DROP TABLE acres;

CREATE TABLE acres (
acres_tall_fescue_comp int, 
acres_rye_comp int, 
acres_garlic_comp int, 
acres_hazelnut_comp int,
acres_date DATE
);

INSERT INTO acres
(
acres_tall_fescue_comp,
acres_rye_comp, 
acres_garlic_comp, 
acres_hazelnut_comp,
acres_date
)
VALUES
(
50000, 0, 0, 0, '2021-09-18'
),(
52000, 0, 0, 0, '2021-09-19'
),(
0, 48000, 0, 0, '2021-09-20'
);

### Adding more data to work with

INSERT INTO acres 
(
acres_tall_fescue_comp, acres_rye_comp, acres_garlic_comp, acres_hazelnut_comp, acres_date
)
VALUES
(
	0, 42000, 0, 0, '2021-09-21'
),(
	0, 40000, 0, 0, '2021-09-22'
),(
	0, 0, 5000, 0, '2021-09-23'
),(
	0, 0, 5000, 0, '2021-09-24'
),(
	0, 0, 0, 2000, '2021-09-25'
),(
	0, 0, 0, 2100, '2021-09-26'
),(
	0, 0, 0, 2200, '2021-09-27'
),(
	48000, 0, 0, 0, '2021-09-28'
),(
	40000, 0, 0, 0, '2021-09-29'
);

INSERT INTO harvest 
	(
	harvest_field_id, harvest_pounds, harvest_date
    )
VALUES
(
'007', 23458, '2021-09-22'
),(
'007', 21458, '2021-09-22'
),(
'006', 23578, '2021-09-22'
),(
'006', 24856, '2021-09-22'
),(
'011', 12000, '2021-09-23'
),(
'011', 15246, '2021-09-24'
),(
'012', 25478, '2021-09-25'
),(
'012', 21456, '2021-09-26'
),(
'013', 23548, '2021-09-27'
),(
'008', 25478, '2021-09-28'
),(
'008', 23548, '2021-09-28'
),(
'008', 21456, '2021-09-28'
),(
'009', 25895, '2021-09-29'
),(
'009', 23548, '2021-09-29'
),(
'010', 21456, '2021-09-29'
),(
'010', 23458, '2021-09-29'
);

INSERT INTO hours 
(
hours_tall_fescue, hours_rye, hours_garlic, hours_hazelnut, hours_date
)
VALUES
(
	0, 11, 0, 0, '2021-09-21'
),(
	0, 10, 0, 0, '2021-09-22'
),(
	0, 0, 12, 0, '2021-09-23'
),(
	0, 0, 11, 0, '2021-09-24'
),(
	0, 0, 0, 8, '2021-09-25'
),(
	0, 0, 0, 9, '2021-09-26'
),(
	0, 0, 0, 8, '2021-09-27'
),(
	13, 0, 0, 0, '2021-09-28'
),(
	10, 0, 0, 0, '2021-09-29'
);

INSERT INTO team (
team_id, team_rating, team_date
)
VALUES
(
	'STB', 5, '2021-09-21'
    ),(
    'WRB', 7, '2021-09-21'
    ),(
    'CTO', 7, '2021-09-21'
    ),(
    'VAV', 10, '2021-09-21'
    ),(
    'AFO', 9, '2021-09-21'
    ),(
    'CTB', 7, '2021-09-21'
    ),(
	'STB', 7, '2021-09-22'
    ),(
    'WRB', 10, '2021-09-22'
    ),(
    'CTO', 9, '2021-09-22'
    ),(
    'VAV', 9, '2021-09-22'
    ),(
    'AFO', 8, '2021-09-22'
    ),(
    'CTB', 4, '2021-09-22'
    ),(
    'STB', 9, '2021-09-23'
    ),(
    'WRB', 7, '2021-09-23'
    ),(
    'CTO', 5, '2021-09-23'
    ),(
    'VAV', 7, '2021-09-23'
    ),(
    'AFO', 7, '2021-09-23'
    ),(
    'CTB', 10, '2021-09-23'
    ),(
	'STB', 9, '2021-09-24'
    ),(
    'WRB', 5, '2021-09-24'
    ),(
    'CTO', 7, '2021-09-24'
    ),(
    'VAV', 7, '2021-09-24'
    ),(
    'AFO', 10, '2021-09-24'
    ),(
    'CTB', 9, '2021-09-24'
    ),(
	'STB', 7, '2021-09-25'
    ),(
    'WRB', 5, '2021-09-25'
    ),(
    'CTO', 7, '2021-09-25'
    ),(
    'VAV', 7, '2021-09-25'
    ),(
    'AFO', 10, '2021-09-25'
    ),(
    'CTB', 9, '2021-09-25'
    ),(
    'STB', 7, '2021-09-26'
    ),(
    'WRB', 7, '2021-09-26'
    ),(
    'CTO', 5, '2021-09-26'
    ),(
    'VAV', 7, '2021-09-26'
    ),(
    'AFO', 7, '2021-09-26'
    ),(
    'CTB', 10, '2021-09-26'
    ),(
	'STB', 9, '2021-09-27'
    ),(
    'WRB', 5, '2021-09-27'
    ),(
    'CTO', 7, '2021-09-27'
    ),(
    'VAV', 7, '2021-09-27'
    ),(
    'AFO', 10, '2021-09-27'
    ),(
    'CTB', 9, '2021-09-27'
    ),(
	'STB', 9, '2021-09-28'
    ),(
    'WRB', 6, '2021-09-28'
    ),(
    'CTO', 8, '2021-09-28'
    ),(
    'VAV', 4, '2021-09-28'
    ),(
    'AFO', 9, '2021-09-28'
    ),(
    'CTB', 7, '2021-09-28'
    ),(
    'STB', 5, '2021-09-29'
    ),(
    'WRB', 7, '2021-09-29'
    ),(
    'CTO', 7, '2021-09-29'
    ),(
    'VAV', 10, '2021-09-29'
    ),(
    'AFO', 9, '2021-09-29'
    ),(
    'CTB', 9, '2021-09-29'
    );

### Adding a universal date table 
##### This will be used as a PK so data entry order is not an issue

CREATE TABLE date (
date DATE);

INSERT INTO date (
date
)
VALUES
('2021-01-01
'),('2021-01-02
'),( '2021-01-03
'),( '2021-01-04
'),( '2021-01-05
'),( '2021-01-06
' ),( '2021-01-07
' ),( '2021-01-08
' ),( '2021-01-09
' ),( '2021-01-10
' ),( '2021-01-11
' ),( '2021-01-12
' ),( '2021-01-13
' ),( '2021-01-14
' ),( '2021-01-15
' ),( '2021-01-16
' ),( '2021-01-17
' ),( '2021-01-18
' ),( '2021-01-19
' ),( '2021-01-20
' ),( '2021-01-21
' ),( '2021-01-22
' ),( '2021-01-23
' ),( '2021-01-24
' ),( '2021-01-25
' ),( '2021-01-26
' ),( '2021-01-27
' ),( '2021-01-28
' ),( '2021-01-29
' ),( '2021-01-30
' ),( '2021-01-31
' ),( '2021-02-01
' ),( '2021-02-02
' ),( '2021-02-03
' ),( '2021-02-04
' ),( '2021-02-05
' ),( '2021-02-06
' ),( '2021-02-07
' ),( '2021-02-08
' ),( '2021-02-09
' ),( '2021-02-10
' ),( '2021-02-11
' ),( '2021-02-12
' ),( '2021-02-13
' ),( '2021-02-14
' ),( '2021-02-15
' ),( '2021-02-16
' ),( '2021-02-17
' ),( '2021-02-18
' ),( '2021-02-19
' ),( '2021-02-20
' ),( '2021-02-21
' ),( '2021-02-22
' ),( '2021-02-23
' ),( '2021-02-24
' ),( '2021-02-25
' ),( '2021-02-26
' ),( '2021-02-27
' ),( '2021-02-28
' ),( '2021-03-01
' ),( '2021-03-02
' ),( '2021-03-03
' ),( '2021-03-04
' ),( '2021-03-05
' ),( '2021-03-06
' ),( '2021-03-07
' ),( '2021-03-08
' ),( '2021-03-09
' ),( '2021-03-10
' ),( '2021-03-11
' ),( '2021-03-12
' ),( '2021-03-13
' ),( '2021-03-14
' ),( '2021-03-15
' ),( '2021-03-16
' ),( '2021-03-17
' ),( '2021-03-18
' ),( '2021-03-19
' ),( '2021-03-20
' ),( '2021-03-21
' ),( '2021-03-22
' ),( '2021-03-23
' ),( '2021-03-24
' ),( '2021-03-25
' ),( '2021-03-26
' ),( '2021-03-27
' ),( '2021-03-28
' ),( '2021-03-29
' ),( '2021-03-30
' ),( '2021-03-31
' ),( '2021-04-01
' ),( '2021-04-02
' ),( '2021-04-03
' ),( '2021-04-04
' ),( '2021-04-05
' ),( '2021-04-06
' ),( '2021-04-07
' ),( '2021-04-08
' ),( '2021-04-09
' ),( '2021-04-10
' ),( '2021-04-11
' ),( '2021-04-12
' ),( '2021-04-13
' ),( '2021-04-14
' ),( '2021-04-15
' ),( '2021-04-16
' ),( '2021-04-17
' ),( '2021-04-18
' ),( '2021-04-19
' ),( '2021-04-20
' ),( '2021-04-21
' ),( '2021-04-22
' ),( '2021-04-23
' ),( '2021-04-24
' ),( '2021-04-25
' ),( '2021-04-26
' ),( '2021-04-27
' ),( '2021-04-28
' ),( '2021-04-29
' ),( '2021-04-30
' ),( '2021-05-01
' ),( '2021-05-02
' ),( '2021-05-03
' ),( '2021-05-04
' ),( '2021-05-05
' ),( '2021-05-06
' ),( '2021-05-07
' ),( '2021-05-08
' ),( '2021-05-09
' ),( '2021-05-10
' ),( '2021-05-11
' ),( '2021-05-12
' ),( '2021-05-13
' ),( '2021-05-14
' ),( '2021-05-15
' ),( '2021-05-16
' ),( '2021-05-17
' ),( '2021-05-18
' ),( '2021-05-19
' ),( '2021-05-20
' ),( '2021-05-21
' ),( '2021-05-22
' ),( '2021-05-23
' ),( '2021-05-24
' ),( '2021-05-25
' ),( '2021-05-26
' ),( '2021-05-27
' ),( '2021-05-28
' ),( '2021-05-29
' ),( '2021-05-30
' ),( '2021-05-31
' ),( '2021-06-01
' ),( '2021-06-02
' ),( '2021-06-03
' ),( '2021-06-04
' ),( '2021-06-05
' ),( '2021-06-06
' ),( '2021-06-07
' ),( '2021-06-08
' ),( '2021-06-09
' ),( '2021-06-10
' ),( '2021-06-11
' ),( '2021-06-12
' ),( '2021-06-13
' ),( '2021-06-14
' ),( '2021-06-15
' ),( '2021-06-16
' ),( '2021-06-17
' ),( '2021-06-18
' ),( '2021-06-19
' ),( '2021-06-20
' ),( '2021-06-21
' ),( '2021-06-22
' ),( '2021-06-23
' ),( '2021-06-24
' ),( '2021-06-25
' ),( '2021-06-26
' ),( '2021-06-27
' ),( '2021-06-28
' ),( '2021-06-29
' ),( '2021-06-30
' ),( '2021-07-01
' ),( '2021-07-02
' ),( '2021-07-03
' ),( '2021-07-04
' ),( '2021-07-05
' ),( '2021-07-06
' ),( '2021-07-07
' ),( '2021-07-08
' ),( '2021-07-09
' ),( '2021-07-10
' ),( '2021-07-11
' ),( '2021-07-12
' ),( '2021-07-13
' ),( '2021-07-14
' ),( '2021-07-15
' ),( '2021-07-16
' ),( '2021-07-17
' ),( '2021-07-18
' ),( '2021-07-19
' ),( '2021-07-20
' ),( '2021-07-21
' ),( '2021-07-22
' ),( '2021-07-23
' ),( '2021-07-24
' ),( '2021-07-25
' ),( '2021-07-26
' ),( '2021-07-27
' ),( '2021-07-28
' ),( '2021-07-29
' ),( '2021-07-30
' ),( '2021-07-31
' ),( '2021-08-01
' ),( '2021-08-02
' ),( '2021-08-03
' ),( '2021-08-04
' ),( '2021-08-05
' ),( '2021-08-06
' ),( '2021-08-07
' ),( '2021-08-08
' ),( '2021-08-09
' ),( '2021-08-10
' ),( '2021-08-11
' ),( '2021-08-12
' ),( '2021-08-13
' ),( '2021-08-14
' ),( '2021-08-15
' ),( '2021-08-16
' ),( '2021-08-17
' ),( '2021-08-18
' ),( '2021-08-19
' ),( '2021-08-20
' ),( '2021-08-21
' ),( '2021-08-22
' ),( '2021-08-23
' ),( '2021-08-24
' ),( '2021-08-25
' ),( '2021-08-26
' ),( '2021-08-27
' ),( '2021-08-28
' ),( '2021-08-29
' ),( '2021-08-30
' ),( '2021-08-31
' ),( '2021-09-01
' ),( '2021-09-02
' ),( '2021-09-03
' ),( '2021-09-04
' ),( '2021-09-05
' ),( '2021-09-06
' ),( '2021-09-07
' ),( '2021-09-08
' ),( '2021-09-09
' ),( '2021-09-10
' ),( '2021-09-11
' ),( '2021-09-12
' ),( '2021-09-13
' ),( '2021-09-14
' ),( '2021-09-15
' ),( '2021-09-16
' ),( '2021-09-17
' ),( '2021-09-18
' ),( '2021-09-19
' ),( '2021-09-20
' ),( '2021-09-21
' ),( '2021-09-22
' ),( '2021-09-23
' ),( '2021-09-24
' ),( '2021-09-25
' ),( '2021-09-26
' ),( '2021-09-27
' ),( '2021-09-28
' ),( '2021-09-29
' ),( '2021-09-30
' ),( '2021-10-01
' ),( '2021-10-02
' ),( '2021-10-03
' ),( '2021-10-04
' ),( '2021-10-05
' ),( '2021-10-06
' ),( '2021-10-07
' ),( '2021-10-08
' ),( '2021-10-09
' ),( '2021-10-10
' ),( '2021-10-11
' ),( '2021-10-12
' ),( '2021-10-13
' ),( '2021-10-14
' ),( '2021-10-15
' ),( '2021-10-16
' ),( '2021-10-17
' ),( '2021-10-18
' ),( '2021-10-19
' ),( '2021-10-20
' ),( '2021-10-21
' ),( '2021-10-22
' ),( '2021-10-23
' ),( '2021-10-24
' ),( '2021-10-25
' ),( '2021-10-26
' ),( '2021-10-27
' ),( '2021-10-28
' ),( '2021-10-29
' ),( '2021-10-30
' ),( '2021-10-31
' ),( '2021-11-01
' ),( '2021-11-02
' ),( '2021-11-03
' ),( '2021-11-04
' ),( '2021-11-05
' ),( '2021-11-06
' ),( '2021-11-07
' ),( '2021-11-08
' ),( '2021-11-09
' ),( '2021-11-10
' ),( '2021-11-11
' ),( '2021-11-12
' ),( '2021-11-13
' ),( '2021-11-14
' ),( '2021-11-15
' ),( '2021-11-16
' ),( '2021-11-17
' ),( '2021-11-18
' ),( '2021-11-19
' ),( '2021-11-20
' ),( '2021-11-21
' ),( '2021-11-22
' ),( '2021-11-23
' ),( '2021-11-24
' ),( '2021-11-25
' ),( '2021-11-26
' ),( '2021-11-27
' ),( '2021-11-28
' ),( '2021-11-29
' ),( '2021-11-30
' ),( '2021-12-01
' ),( '2021-12-02
' ),( '2021-12-03
' ),( '2021-12-04
' ),( '2021-12-05
' ),( '2021-12-06
' ),( '2021-12-07
' ),( '2021-12-08
' ),( '2021-12-09
' ),( '2021-12-10
' ),( '2021-12-11
' ),( '2021-12-12
' ),( '2021-12-13
' ),( '2021-12-14
' ),( '2021-12-15
' ),( '2021-12-16
' ),( '2021-12-17
' ),( '2021-12-18
' ),( '2021-12-19
' ),( '2021-12-20
' ),( '2021-12-21
' ),( '2021-12-22
' ),( '2021-12-23
' ),( '2021-12-24
' ),( '2021-12-25
' ),( '2021-12-26
' ),( '2021-12-27
' ),( '2021-12-28
' ),( '2021-12-29
' ),( '2021-12-30
' ),( '2021-12-31'
);

### Moving PK and FKs around to accept new *date* table

ALTER TABLE date
ADD CONSTRAINT PK_date PRIMARY KEY (date);

##### Changing all the FKs over to the new date table

ALTER TABLE harvest DROP FOREIGN KEY FK_harvest_date;

ALTER TABLE harvest
ADD CONSTRAINT FK_harvest_date
FOREIGN KEY (harvest_date) REFERENCES date(date);

ALTER TABLE acres DROP FOREIGN KEY FK_acres_date;

ALTER TABLE acres
ADD CONSTRAINT FK_acres_date
FOREIGN KEY (acres_date) REFERENCES date(date);

ALTER TABLE team DROP FOREIGN KEY FK_team_date;

ALTER TABLE team
ADD CONSTRAINT FK_team_date
FOREIGN KEY (team_date) REFERENCES date(date);

ALTER TABLE hours DROP PRIMARY KEY;

ALTER TABLE hours
ADD CONSTRAINT FK_hours_date
FOREIGN KEY (hours_date) REFERENCES date(date);
