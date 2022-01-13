# Portfolio
## James Wheeler 
**[Resume](https://docs.google.com/document/d/1pCTnupASnwYF3G4kDYsw9GDeExo4WH1TxFwKv5RCZyY/edit?usp=sharing)** - 
**[LinkedIn](https://www.linkedin.com/in/james-wheeler-85115b215/)** - **[Certification](https://coursera.org/share/2ab12b15d95d4fe4b8a58abb081c97d8)**

##### Projects here will be listed in reverse chronological order


## Project 4: Exploring Covid Data with SQL
The goal of this project was to practice using SQL while gaining understanding of what Covid was doing on a global scale. 

1. My original intent was to use MySQL to run all of my exploratory queries. The importing of my covid.csv was moving at 20 entries a minute and I had 150,000 entries. I found that there are a group of packages that allow you to run SQL queries in R. Using _queryparser_ and _tidyquery_ I was able to run my queries.
2. The exploration of the data can be found *[here}(

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

### Courses Completed
1. [Google Data Analytics](
https://www.coursera.org/account/accomplishments/specialization/certificate/X79PFW94QH2W)
* Foundations: Data, Data, Everywhere
* Ask Questions to Make Data-Driven Decisions
* Prepare Data for Exploration
* Process Data from Dirty to Clean
* Analyze Data to Answer Questions
* Share Data Through the Art of Visualization
* Data Analysis with R Programming
* Google Data Analytics Captstone: Complete a Case Study

2. [Exploratory Data Analysis With Python and Pandas](
https://www.coursera.org/account/accomplishments/certificate/WUH4D5767JUQ)

3. [Introduction to Relational Database and SQL](
https://www.coursera.org/account/accomplishments/certificate/XDMZTUBPHVW5)

4. [Intermediate Relational Database and SQL](
https://www.coursera.org/account/accomplishments/certificate/9RNLUCLS9KDT)
