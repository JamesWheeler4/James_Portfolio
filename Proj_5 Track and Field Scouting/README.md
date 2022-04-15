## Project 5: Track and Field Scouting Tool

#### 95 hours as of 4/13/2022

The goal of this project is to create scouting reports for track and field teams using Python automation. 
As a track and field athlete in community college, I was asked by the coach to work on organizing spreadsheets of possible future recruits. 
I was tasked with searching for athletes results as well as the schools they went to. 
Looking back, this was a task that the coach would have done had I not offered my skills with excel. 
This project is an exercise in identifying a need and creating a program to facilitate a better user experience.

### **Data Storage**

1. When initially testing the viability of this tool, I wrote the data to a list and stored that list as a .csv file to review. This worked at small scale to prove the concept, but it would not scale well.
2. To provide room for growth, I designed and created a SQLite3 database. Using a consistent table structure of 'id' as a primary key and avoiding redundant strings, the database took shape.
3. The most up to date schema for this database can be found [here]()

### **Web Scraping**

1. The first step of this project was to identify and extract the relevant data. This was done by inspecting data source and learning the html formatting that is used to organize the data.
2. Initially the roadblock was having to log in to access any of the relevant data. For this I turned to Selenium. Using key inputs I was able to enter the website and navigate to the desired webpages.
3. Next was the issue of extracting the data in a sorted manner. All of the pertinent information is tagged as anchor links with limited differentiation. To work around this, I passed on using *bs4* and elected to extract the whole page, parse it as a string using regex.
4. Through this method I was able to iterate through parsed segments of the extracted source data. Along the way creating and replacing variables to store using SQLite3.
5. This was tested across multiple districts and states, checking for any variance in the website, event type, or anything unforeseen.
6. I created another gathering function that would parse through a track meet and pull the results. This varied from the first function in that the first pulled all information from one webpage (for each state). This function pulled a small amount of data from over 15 webpages per gender per meet. This variance was required because of how meet data is entered at the college level. College data was extracted using this set of [functions](https://github.com/JamesWheeler4/James_Portfolio/blob/main/Proj_5%20Track%20and%20Field%20scouting%20tool/APCollege.py).



### **Data Storage and Processing**

1. Before storing the data, alterations needed to be made to smooth out future analysis and organization. This was done by normalizing terminology (event names) and units of measurements (all to seconds and meters to hundredths of feet) between high school and college. Additionally to determine ascending or descending rankings, the field events (highest wins) were separated from track events (lowest wins) using a sorting indicator. This process was done in the corresponding functions shown above.
2. Now that necessary comparison data was collected, I wrote each high school state, gender, and event type (track or field) to its own csv. These were placed in gendered folders before being globbed and appended together using this set of [functions](https://github.com/JamesWheeler4/James_Portfolio/blob/main/Proj_5%20Track%20and%20Field%20scouting%20tool/APResults.py). I arranged and renamed the high school columns to the corresponding college format before appending the college meet results onto the high school data set.
3. Once everything was combined and properly formatted, I created a ranking and scoring function that took the top ten athletes in each event scoring the top eight as is done in a traditional championship meet. From this ranking function I returned both the top ten as well as the overall rankings for all levels gathered.

### **Analysis**

1. Initial evaluation of the data showed very clearly that comparing community college results to top ten highschoolers per state was not a reasonable comparison. I will recreate the gathering with more samples and more compatible athletes.
