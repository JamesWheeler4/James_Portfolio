# Portfolio
## James Wheeler 
**[Resume](https://docs.google.com/document/d/1KZVGh-1VK24UmyeQ2OWw1RhE-p72onsg2fxrD2kxV9k/edit?usp=sharing)** - 
**[LinkedIn](https://www.linkedin.com/in/james-wheeler-85115b215/)**

##### Projects here will be listed in reverse chronological order

## Project 5: Track and Field Scouting Tool
The goal of this project is to create scouting reports for track and field teams using Python automation. As a track and field athlete in community college, I was asked by the coach to work on organizing spreadsheets of possible future recruits. I was tasked with searching for athletes results on *athletic.net* as well as the schools they went to. Looking back, this was a task that the coach would have done had I not offered my skills with excel. It is my hope to offer this finished tool specifically to colleges with limited funding. I have seen first hand how much effort it takes as an underfunded coach, this project will lessen that work load.

1. Web Scraping
* The first step of this project was to identify and extract the relevant data. This was done by inspecting *athletic.net* and learning the html formatting that is used to organize the data. 
* Initially the roadblock that was in place was the requirement of having to log in to access any of the relevant data. For this I turned to *Selenium*. Using key inputs I was able to enter the website and navigate to the desired webpages.
* Next was the issue of extracting the data in a sorted manner. All of the pertinent information is tagged as anchor links with limited differentiation. To work around this, I passed on using *bs4* and elected to extract the whole page, parse it as a string using regex.
* Through this method I was able to create lists containing event, place, grade/age, athleteId, name, mark, school/club, and schoolId/clubId.
* This was tested across multiple districts and states, checking for any variance in the website, event type, or anything unforeseen.

2. Data Storage and Processing
* Next I will store this data using SQL and write a program to compare the high school data to college data, beginning the report process.

## Project 4: Exploring Covid Data with SQL (Plan to revisit)
The goal of this project was to practice using SQL while gaining understanding of what Covid was doing on a global scale. 

1. My original intent was to use MySQL to run all of my exploratory queries. The importing of my covid.csv was moving at 20 entries a minute and I had 150,000 entries. I found that there are a group of packages that allow you to run SQL queries in R. Using _queryparser_ and _tidyquery_ I was able to run my queries.
2. The exploration of the data can be found *[here](https://github.com/JamesWheeler4/James_Portfolio/blob/main/covid_project_final_20220113.pdf)*. I summarize the findings that interested me at the bottom of the report. The reliability of the data was seen to be mediocre. It would make sense that during a pandemic, there would likely be challenges with collecting universally formatted data on a global scale.
3. In the future I would like to graph some of the insights I've found. I'm particularly interested in seeing what the pattern of daily cases to daily deaths looks like. How does the relationship between the slope of an infection spike relate to the slope of the following death spike? How much does this relationship vary between variants? All things I'm curious about!

## Project 3: Harvest Project
The goal of this project was to create a product that will allow farmers to track multiple metrics with ease. My plan is to construct a relational database with MySQL that will flow into a Tableau dashboard. Though not currently part of this project, I am formatting the database to allow simple data entry by employees in different roles. 

1. I started by making a *[plan](https://docs.google.com/document/d/1YyngyRyTgFPxvGVLCq6RIbK8hzeYZ-8hVMB1OoWBJCQ/edit?usp=sharing)* for what I wanted available of the dashboard.  Next I organized the tables that would make up my database and *[visualized](https://docs.google.com/spreadsheets/d/1PRz3RgTxUNtSMZVTSvkq5MRsYyyzI8XInMlv0Mt_sxc/edit?usp=sharing)* how they would connect to one another. Having a plan, I was ready to move forward to MySQL and start building the database.
2. Establishing the database for the *[MySQL Project](harvest_project_mysql.md)* went smoothly. I entered test data so I could see the functions of the relations once completed. Next connected the tables via primary keys and foreign keys.
3. I began writing and testing *[queries](https://docs.google.com/document/d/1dWfXSUgsX9NtvqmmeN4tWFAJD69o_n2yAJJpXa8sw44/edit?usp=sharing)* to output the metrics that will be used in Tableau. Once confirming values from direct SQL outputs, I started to translate these metrics to calculated value equations in Tableau. The outcome of these can be seen in this *[visualization](https://github.com/JamesWheeler4/James_Portfolio/blob/main/Images/Harvest_dashboard_2021.PNG)* which is updated live from the'harvest_project' MySQL database that I had created.
4. I will not currently be moving forward with the web development necessary to build the front end data entry of this project. I believe that I've structured the database to easily accept the addition of simple data entry. 

## Project 2: Revising Project 1 with Python and Tableau
Having a foundation in R, moving to Python was not too challenging. Also having completed a project already, it was much easier to plan the trajectory of my data processing.

1. I started in Jupyter Notebooks by setting up my environment. I then uploaded, organized, and cleaned my data. Using Seaborn, I used pairplots and heatmaps to prospect for connections within my data. This entire process can be seen in this *[notebook](https://www.kaggle.com/jameswheelerda/bellabeatv2-083021)*.
2. Next I turned to Tableau. After uploading my data, I made multiple graphs depicting the relation of nightly sleep to minutes spent sedentary and in varied levels of activity. Once those were complete I created corresponding correlation coefficients and filter sets. I added in total steps relative to nightly sleep as well. Finally I put it all together in a dashboard that will show the relational change between the data sets. Here is the *[dashboard](https://public.tableau.com/app/profile/james.wheeler2559/viz/Bellabeat083021/EffectsofSleeponDailyMovement_1)*.

Having worked with this data before, the goal of this project was to see if I could find and present the same findings in a more professional way. I am proud of the end product, it has given me inspiration for project 3.

## Project 1: Case study for Bellabeat
As a final project for completing the Google Data Analytics Certificate, I was tasked with completing a case study. Having history within the fitness industry I chose to work with Bellabeat, a wellness company focused on fitness wearables. The project went as follows.

1. I was given a list of tasks to complete, requests from my primary stakeholders, and a data set to use. I condensed all of the given information into a mock *[project proposal](https://docs.google.com/document/d/1ToHGRn7pGlIVNgqHWGRJtbXiU3p2nxm36pNbNm4VwLQ/edit?usp=sharing)*.
2. Moving the dataset into Rstudio where I processed and started to look into the data. The notebook of my journey through the data can be found in this *[notebook](https://www.kaggle.com/jameswheelerda/bellabeat-capstone-080321)*. Summatively, I found correlations between time spent sleeping and time sedentary as well as a distribution of when the participants were most active and the corresponding activity intensity.
3. The deliverable that I completed for this project was in the form of a *[Google slides presentation](https://docs.google.com/presentation/d/17OLot-w2_zf2OD6mtz9Lg54_LiBtoin-LBGneXZw2ck/edit?usp=sharinghttps://docs.google.com/presentation/d/17OLot-w2_zf2OD6mtz9Lg54_LiBtoin-LBGneXZw2ck/edit?usp=sharing)*. In this presentation I briefly explain the business tasks and the dataset used, being sure to mention some of the context of the dataset. Next, I used visualizations and talking points to explain my findings. Finally I concluded with a summary and suggestions for Bellabeats moving forward.

This project, being my first, held a lot of learning lessons. I was proud of the end product but not so much the process in which I got there. To remedy this, I chose to redo the processing and analysis portion of the project with Python and Tableau.



### Certifications Completed
1. [Google Data Analytics](https://coursera.org/share/2ab12b15d95d4fe4b8a58abb081c97d8)
* Foundations: Data, Data, Everywhere
* Ask Questions to Make Data-Driven Decisions
* Prepare Data for Exploration
* Process Data from Dirty to Clean
* Analyze Data to Answer Questions
* Share Data Through the Art of Visualization
* Data Analysis with R Programming
* Google Data Analytics Captstone: Complete a Case Study

2. Python for Everybody Specialization via University of Michigan
* [Programming for Everybody (Getting Started with Python)](https://coursera.org/share/69ad88d8c472cff0430d9da8401a2cf7)
* [Python Data Structures](https://coursera.org/share/9107466a97373be0895126fc96c63ed4)
* [Using Python to Access Web Data](https://coursera.org/share/e9e2b286bfd8906ef01e23955fba0d88)
* Using Databases with Python (In Progress)

### Courses Completed

1. [Exploratory Data Analysis With Python and Pandas](https://coursera.org/share/6ea3066fddf24857dfb9311d40dcaa64)

2. [Introduction to Relational Database and SQL](https://coursera.org/share/7afa2e3edff48e22a268adb858b1c918)

3. [Intermediate Relational Database and SQL](https://coursera.org/share/bd63629d0f008caf04f7c020c543e31b)
