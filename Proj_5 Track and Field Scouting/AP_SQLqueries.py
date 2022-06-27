## Selecting athletes for machine learning

# Finding number of marks per athlete per event
SELECT event_id, athlete_id, COUNT(athlete_id) AS counts
	FROM Full_Result
	GROUP BY athlete_id, event_id
	ORDER BY event_id, counts DESC

# Finding athletes with atleast 20 marks in a given event
SELECT tbl.event_id, tbl.athlete_id, tbl.counts, Event.name
FROM (SELECT event_id, athlete_id, COUNT(athlete_id) AS counts
	FROM Full_Result
	GROUP BY athlete_id, event_id
	ORDER BY event_id, counts DESC) AS tbl JOIN Event ON tbl.event_id = Event.id
WHERE tbl.counts > 20

# Finding which event has the most athletes with over 20 marks in a given event
SELECT Event.name, COUNT(DISTINCT tbl.athlete_id) AS athlete_count, tbl.event_id
FROM (SELECT event_id, athlete_id, COUNT(athlete_id) AS counts
	FROM Full_Result
	GROUP BY athlete_id, event_id
	ORDER BY event_id, counts DESC) AS tbl JOIN Event ON tbl.event_id = Event.id
WHERE tbl.counts > 20
GROUP BY tbl.event_id

# Finding which events have the most total marks
SELECT Event.name, sum(tbl.counts) AS sums, tbl.event_id
FROM (SELECT event_id, athlete_id, COUNT(athlete_id) AS counts
	FROM Full_Result
	GROUP BY athlete_id, event_id
	ORDER BY event_id, counts DESC) AS tbl JOIN Event ON tbl.event_id = Event.id
WHERE tbl.counts > 20
GROUP BY tbl.event_id
ORDER BY sums DESC


## Calculating total and percentage marks per year by grade

# Total marks for 2022
SELECT count(*)
FROM Full_Result JOIN Athlete ON Full_Result.athlete_id = Athlete.id
WHERE Full_Result.year = 2022 AND Athlete.grade != 'FR' AND Athlete.grade != 'SO'

# Total marks and unique athletes for 2022 per grade
SELECT Athlete.grade, COUNT(*) AS total_marks, COUNT (DISTINCT Full_Result.athlete_id) AS unique_athletes
FROM Full_Result JOIN Athlete ON Full_Result.athlete_id = Athlete.id
WHERE Full_Result.year = 2022 AND Athlete.grade != 'FR' AND Athlete.grade != 'SO'
GROUP BY Athlete.grade

# Percentage of marks and unique athletes in each grade for 2022 marks
SELECT Athlete.grade, 
(COUNT(*)*100)/(SELECT count(*)
	FROM Full_Result JOIN Athlete ON Full_Result.athlete_id = Athlete.id
	WHERE Full_Result.year = 2022 AND Athlete.grade != 'FR' AND Athlete.grade != 'SO')
	AS perc_marks, 
(COUNT (DISTINCT Full_Result.athlete_id)*100)/(SELECT COUNT (DISTINCT Full_Result.athlete_id) AS unique_athletes
	FROM Full_Result JOIN Athlete ON Full_Result.athlete_id = Athlete.id
	WHERE Full_Result.year = 2022 AND Athlete.grade != 'FR' AND Athlete.grade != 'SO') AS perc_unique_ath
FROM Full_Result JOIN Athlete ON Full_Result.athlete_id = Athlete.id
WHERE Full_Result.year = 2022 AND Athlete.grade != 'FR' AND Athlete.grade != 'SO'
GROUP BY Athlete.grade


## Exploring changes year over year (first looking at 100m mens)

# Grouped by athlete with avg mark and last year of mark
SELECT athlete_id, round(AVG(mark), 2) AS average_mark, MAX(year) AS last_year
FROM Full_Result
WHERE event_id = 1 AND mark < 16
GROUP BY athlete_id
ORDER BY average_mark 

# Grouped by year with min, max, and avg
SELECT MAX(mark) AS slowest, MIN(mark) AS fastest, round(AVG(mark), 2) AS average_mark, year
FROM Full_Result
WHERE event_id = 1 AND mark < 16
GROUP BY year
ORDER BY year DESC

# Showing min, max, avg for each year
SELECT MAX(fr.mark) AS slowest, MIN(fr.mark) AS fastest, round(AVG(fr.mark), 2) AS average_mark, fr.year,
FROM Full_Result AS fr
WHERE event_id = 1 AND mark < 16
GROUP BY year
ORDER BY year DESC

# Calculating year over year percentage change
SELECT year, ROUND(avg(mark), 2) AS avg_mark, 
		ROUND(LAG(avg(mark)) OVER (ORDER BY year), 2) AS last_year, 
		ROUND((LAG(avg(mark)) OVER (ORDER BY year))/ avg(mark) - 1, 2)*100 AS percent_change
FROM Full_Result
WHERE event_id = 1 AND mark < 16
GROUP BY year
ORDER BY year
