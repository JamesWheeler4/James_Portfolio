'''
The goal of this project is to scrape data from Athletic.net
Likely taking the stats of the top100 in a given event. Start with Javelin
Next I will compare those to the NWACC conference marks, noting if anyone would score points
Make sure to graph the past yearly best marks to see progression
This process will be repeated for all events, then to Cross Country
'''

'''
The following goal will be to gather data from NWACC athletes with highschool data
Then using ML try to create a projection of how athletes improve when going to different schools
This could indicate considerations for coaching as well as where recuiting is weak
Additionally, it might be made more clear what events show more improvement in college
'''

'''
Next:
Write each report as a csv (using index 1 and today's date)
    SHOULD TRY NEXT
Add them to sql to compare?
Future:
 - tie into SQL
    - store list of all schools
    - requires iterating through list of url numbers
    - using google api to find locations
    - check if google has api for distance calculations
- for those that are point positive, generate write-ups on past performance
    - could be graphic representations and printed markdowns
'''

'''
----------Log----------  HOUR COUNT 41
2022/02/17 2hr - Created MarkComp Function, Working on SQL import

2022/02/19 2hr - Modified Def to return df, Writing to CSV within Defs
                Modified Def: dropped grade transfer
                Wrote to CSV and combined into large file sorted by times (APTest)

2022/02/21 5hr - Split Def into 2 different outputs, Track{name} and Field{name}
                Exploring Pandas pivot tables, Started a scoring and sorting algorithm
                
2022/02/23 10hr - Finished toptenfinal() and placed in APDef2 
                Created collection function for meet results for college finals
                Modified college collect to drop DNS or FOUL
                Created topglob(), bug fixed, completed
                Finished comparison 
 
                Extract points from team and calculate possible increases
                    Scoring for Ties needs to be sorted out (split the difference)
                # Remove California
                Work on distance API
                    Each athletes location is on their main page
                        Go to the athletes link and return location
                        Check out SQLite to see if creating multiple tables is a good option
                Might do custom athlete reports
                
                Possibly use DASH to create a web display to report the data
                    This could drill down to athlete performance
                        Predict (ML) what their next data will be
'''

