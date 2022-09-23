## Project 6: Track and Field Machine Learning

The goal of this project was to create a track and field ‘PR’ prediction tool utilizing machine learning and the data collected in project 5. This tool would be able to predict an athlete's next best mark based on their current top marks with a high degree of accuracy. I spent most of my time working with Keras and Tkinter in the completion of this project. Along the way, I created and tested ML models, expanded my testing data, tweaked the models to be <1% average error, and created a GUI that allows a user to work with the tool easily.

### **Data prep**
1. Pulling from the data collected in Project 5, I initially extracted and arranged marks from athletes with over 10 marks in a given event. This returned less results than expected.
2. I retooled the script to allow me to enter a desired mark count. I settled on four marks as it delivered a considerable sample size while still allowing for three training points and one test point.
3. The script I wrote to create these datasets can be found [here](https://github.com/JamesWheeler4/James_Portfolio/blob/main/Proj_6%20Track%20and%20Field%20ML/python/ML_Prep.py)
