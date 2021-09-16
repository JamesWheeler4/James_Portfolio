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

Duplicated harvest multiple times

DELETE FROM harvest

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

Might redo this so that I can use the date as a primary key
		This will probably be done with the addition of hours_tall_fescue, hours_rye, hours_garlic, hours_hazelnut, hours_date

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

Adding a crop table so that it can be a PK reference with total acres and goal hours

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
-- Making all of my PK and FK to link my tables

-- PK field_info.field_id		FK harvest.harvest_field_id
-- PK crop.crop				FK field_info.field_crop, cost.cost_crop, acres.acres_crop
-- PK hours.hours_date			FK harvest.harvest_date, acres.acres_date, team.team_date

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
Tables have differing format

UPDATE field_info
SET
	field_crop = REPLACE(field_crop, 'Rye', 'rye');

UPDATE field_info
SET
	field_crop = REPLACE(field_crop, 'Tall Fescue', 'tall_fescue');
