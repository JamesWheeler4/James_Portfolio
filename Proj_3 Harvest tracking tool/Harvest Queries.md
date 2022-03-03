# Harvest Queries

### % Acres harvested per crop/total

##### tall_fescue % comp
SELECT (SUM(acres_tall_fescue_comp)/
	(SELECT crop_acres_total
	FROM harvest_project.crop
	WHERE crop = 'tall_fescue')) AS 'tall_fescue_%_comp'
FROM harvest_project.acres;

##### rye % comp
SELECT (SUM(acres_rye_comp)/
	(SELECT crop_acres_total
	FROM harvest_project.crop
	WHERE crop = 'rye')) AS 'rye_%_comp'
FROM harvest_project.acres;

##### garlic % comp
SELECT (SUM(acres_garlic_comp)/
	(SELECT crop_acres_total
	FROM harvest_project.crop
	WHERE crop = 'garlic')) AS 'garlic_%_comp'
FROM harvest_project.acres;

##### hazelnut % comp
SELECT (SUM(acres_hazelnut_comp)/
	(SELECT crop_acres_total
	FROM harvest_project.crop
	WHERE crop = 'hazelnut')) AS 'hazelnut_%_comp'
FROM harvest_project.acres;

##### % total acres harvested
SELECT (SUM(acres_tall_fescue_comp) + 
	SUM(acres_rye_comp) + 
    SUM(acres_garlic_comp) + 
    SUM(acres_hazelnut_comp))
/
	(SELECT SUM(crop_acres_total)
	FROM harvest_project.crop) AS 'total % comp'
FROM harvest_project.acres;

### Acres per day per crop/total

##### tall_fescue acres/day
SELECT (SUM(acres_tall_fescue_comp)/
	(SELECT COUNT(hours_tall_fescue)
    FROM harvest_project.hours
    WHERE hours_tall_fescue != 0))/100 AS 'tall_fescue acres/day'
FROM harvest_project.acres;

##### rye acres/day
SELECT (SUM(acres_rye_comp)/
	(SELECT COUNT(hours_rye)
    FROM harvest_project.hours
    WHERE hours_rye != 0))/100 AS 'rye acres/day'
FROM harvest_project.acres;

##### garlic acres/day
SELECT (SUM(acres_garlic_comp)/
	(SELECT COUNT(hours_garlic)
    FROM harvest_project.hours
    WHERE hours_garlic != 0))/100 AS 'garlic acres/day'
FROM harvest_project.acres;

##### hazelnut acres/day
SELECT (SUM(acres_hazelnut_comp)/
	(SELECT COUNT(hours_hazelnut)
    FROM harvest_project.hours
    WHERE hours_hazelnut != 0))/100 AS 'hazelnut acres/day'
FROM harvest_project.acres;

##### total acres/day
SELECT (SUM(acres_tall_fescue_comp) + 
	SUM(acres_rye_comp) + 
    SUM(acres_garlic_comp) + 
    SUM(acres_hazelnut_comp))
/
	(SELECT COUNT(hours_date)
	FROM harvest_project.hours)/100 AS 'total acres/day'
FROM harvest_project.acres;

### Acres per hour per crop/total

##### tall_fescue acres/hour
SELECT (SUM(acres_tall_fescue_comp)/
	(SELECT SUM(hours_tall_fescue)
    FROM harvest_project.hours
    WHERE hours_tall_fescue != 0))/100 AS 'tall_fescue acres/hour'
FROM harvest_project.acres;

##### rye acres/hour
SELECT (SUM(acres_rye_comp)/
	(SELECT SUM(hours_rye)
    FROM harvest_project.hours
    WHERE hours_rye != 0))/100 AS 'rye acres/hour'
FROM harvest_project.acres;

##### garlic acres/hour
SELECT (SUM(acres_garlic_comp)/
	(SELECT SUM(hours_garlic)
    FROM harvest_project.hours
    WHERE hours_garlic != 0))/100 AS 'garlic acres/hour'
FROM harvest_project.acres;

##### hazelnut acres/hour
SELECT (SUM(acres_hazelnut_comp)/
	(SELECT SUM(hours_hazelnut)
    FROM harvest_project.hours
    WHERE hours_hazelnut != 0))/100 AS 'hazelnut acres/hour'
FROM harvest_project.acres;

##### total acres/hour
SELECT (SUM(acres_tall_fescue_comp) + 
	SUM(acres_rye_comp) + 
    SUM(acres_garlic_comp) + 
    SUM(acres_hazelnut_comp))
/
	(SELECT (SUM(hours_tall_fescue) + 
		SUM(hours_rye) +
        SUM(hours_garlic) +
        SUM(hours_hazelnut))
	FROM harvest_project.hours)/100 AS 'total acres/hour'
FROM harvest_project.acres;

### Yield per acre per crop

##### tall_fescue yield/acre
SELECT (IFNULL(SUM(harvest_pounds), 0) +
	((SELECT IFNULL(SUM(harvest_pounds), 0)
	FROM harvest_project.harvest
	WHERE harvest_field_id = '002') +
	(SELECT IFNULL(SUM(harvest_pounds), 0)
	FROM harvest_project.harvest
	WHERE harvest_field_id = '008') +
	(SELECT IFNULL(SUM(harvest_pounds), 0)
	FROM harvest_project.harvest
	WHERE harvest_field_id = '009') +
	(SELECT IFNULL(SUM(harvest_pounds), 0)
	FROM harvest_project.harvest
	WHERE harvest_field_id = '010')))
    /
    (SELECT (SUM(acres_tall_fescue_comp)/100)
	FROM harvest_project.acres) AS 'tall_fescue yield/acre'
FROM harvest_project.harvest
WHERE harvest_field_id = '001';

##### rye yield/acre
SELECT (IFNULL(SUM(harvest_pounds), 0) +
	((SELECT IFNULL(SUM(harvest_pounds), 0)
	FROM harvest_project.harvest
	WHERE harvest_field_id = '004') +
	(SELECT IFNULL(SUM(harvest_pounds), 0)
	FROM harvest_project.harvest
	WHERE harvest_field_id = '005') +
	(SELECT IFNULL(SUM(harvest_pounds), 0)
	FROM harvest_project.harvest
	WHERE harvest_field_id = '006') +
	(SELECT IFNULL(SUM(harvest_pounds), 0)
	FROM harvest_project.harvest
	WHERE harvest_field_id = '007')))
    /
    (SELECT (SUM(acres_rye_comp)/100)
	FROM harvest_project.acres) AS 'rye yield/acre'
FROM harvest_project.harvest
WHERE harvest_field_id = '003';

##### garlic yield/acre
SELECT (IFNULL(SUM(harvest_pounds), 0) +
	((SELECT IFNULL(SUM(harvest_pounds), 0)
	FROM harvest_project.harvest
	WHERE harvest_field_id = '?') +
	(SELECT IFNULL(SUM(harvest_pounds), 0)
	FROM harvest_project.harvest
	WHERE harvest_field_id = '?') +
	(SELECT IFNULL(SUM(harvest_pounds), 0)
	FROM harvest_project.harvest
	WHERE harvest_field_id = '?') +
	(SELECT IFNULL(SUM(harvest_pounds), 0)
	FROM harvest_project.harvest
	WHERE harvest_field_id = '?')))
    /
    (SELECT (SUM(acres_garlic_comp)/100)
	FROM harvest_project.acres) AS 'garlic yield/acre'
FROM harvest_project.harvest
WHERE harvest_field_id = '?';

##### hazelnut yield/acre
SELECT (IFNULL(SUM(harvest_pounds), 0) +
	((SELECT IFNULL(SUM(harvest_pounds), 0)
	FROM harvest_project.harvest
	WHERE harvest_field_id = '?') +
	(SELECT IFNULL(SUM(harvest_pounds), 0)
	FROM harvest_project.harvest
	WHERE harvest_field_id = '?') +
	(SELECT IFNULL(SUM(harvest_pounds), 0)
	FROM harvest_project.harvest
	WHERE harvest_field_id = '?') +
	(SELECT IFNULL(SUM(harvest_pounds), 0)
	FROM harvest_project.harvest
	WHERE harvest_field_id = '?')))
    /
    (SELECT (SUM(acres_hazelnut_comp)/100)
	FROM harvest_project.acres) AS 'hazelnut yield/acre'
FROM harvest_project.harvest
WHERE harvest_field_id = '?';

### Cost per acre per crop

##### tall_fescue cost/acre
SELECT (((cost_fixed/100) + (
	(cost_harvest_hour/100) 
    *
	(SELECT SUM(hours_tall_fescue)
    FROM harvest_project.hours
    WHERE hours_tall_fescue != 0)))
/
	((SELECT (SUM(acres_tall_fescue_comp)/100)
	FROM harvest_project.acres
	WHERE acres_tall_fescue_comp != 0)
	/
    (SELECT COUNT(hours_tall_fescue)
    FROM harvest_project.hours
    WHERE hours_tall_fescue !=0))) AS 'tall_fescue cost/acre'
FROM harvest_project.cost
WHERE cost_crop = 'tall_fescue';

##### rye cost/acre
SELECT (((cost_fixed/100) + (
	(cost_harvest_hour/100) 
    *
	(SELECT SUM(hours_rye)
    FROM harvest_project.hours
    WHERE hours_rye != 0)))
/
	((SELECT (SUM(acres_rye_comp)/100)
	FROM harvest_project.acres
	WHERE acres_rye_comp != 0)
	/
    (SELECT COUNT(hours_rye)
    FROM harvest_project.hours
    WHERE hours_rye !=0))) AS 'rye cost/acre'
FROM harvest_project.cost
WHERE cost_crop = 'rye';

##### garlic cost/acre
SELECT (((cost_fixed/100) + (
	(cost_harvest_hour/100) 
    *
	(SELECT SUM(hours_garlic)
    FROM harvest_project.hours
    WHERE hours_garlic != 0)))
/
	((SELECT (SUM(acres_garlic_comp)/100)
	FROM harvest_project.acres
	WHERE acres_garlic_comp != 0)
	/
    (SELECT COUNT(hours_garlic)
    FROM harvest_project.hours
    WHERE hours_garlic !=0))) AS 'garlic cost/acre'
FROM harvest_project.cost
WHERE cost_crop = 'garlic';

##### hazelnut cost/acre
SELECT (((cost_fixed/100) + (
	(cost_harvest_hour/100) 
    *
	(SELECT SUM(hours_hazelnut)
    FROM harvest_project.hours
    WHERE hours_hazelnut != 0)))
/
	((SELECT (SUM(acres_hazelnut_comp)/100)
	FROM harvest_project.acres
	WHERE acres_hazelnut_comp != 0)
	/
    (SELECT COUNT(hours_hazelnut)
    FROM harvest_project.hours
    WHERE hours_hazelnut !=0))) AS 'hazelnut cost/acre'
FROM harvest_project.cost
WHERE cost_crop = 'hazelnut';
