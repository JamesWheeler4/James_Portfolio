## Project 6: Track and Field Machine Learning

The goal of this project was to create a track and field ‘PR’ prediction tool utilizing machine learning and the data collected in project 5. This tool would be able to predict an athlete's next best mark based on their current top marks with a high degree of accuracy. I spent most of my time working with Keras and Tkinter in the completion of this project. Along the way, I created and tested ML models, expanded my testing data, tweaked the models to be <1% average error, and created a GUI that allows a user to work with the tool easily.

### **Data prep**
1. Pulling from the data collected in Project 5, I initially extracted and arranged marks from athletes with over 10 marks in a given event. This returned less results than expected.
2. I retooled the script to allow me to enter a desired mark count. I settled on four marks as it delivered a considerable sample size while still allowing for three training points and one test point.
3. The script I wrote to create these datasets can be found [here](https://github.com/JamesWheeler4/James_Portfolio/blob/main/Proj_6%20Track%20and%20Field%20ML/python/ML_Prep.py).

### **Building Model and Beginning Training**
1. Using the Keras library, I build a straightforward base model to test different parameters. This took the form of a three layer (input, hidden, output) neural network.
2. I started testing various different approaches of changing the size of the input data set (9 points, 5 points, 3 points), exploring discrete vs. categorical outputs, changing the size and number of hidden layers, and experimenting with various activation functions. 
3. When balancing accuracy and speed across track events, I found that four hidden layers of 64 nodes using the “relu” activation function produced models that met goal of a MAE that was less that 1% of the events mark average.
4. In this script you can see the establishing of average error for each dataset, division of the test and training data, normalizing function, model creation, and testing of the given dataset which could be saved if the model performed within the desired range. The script can be found  [here](https://github.com/JamesWheeler4/James_Portfolio/blob/main/Proj_6%20Track%20and%20Field%20ML/python/ML_LinReg_Track.py).

### **Expanding Datasets**
1. Working with limited data available to the set, I wanted to test the model with larger datasets to see if I would be able to get consistent results regardless of size. I created a script that would expand my existing datasets.
2. The script is created in a way that through the modification of the “multiple” variable, you can choose how many output entries are created from each input entry. I chose a multiple of 10 which turns a 300 entry dataset into a 3300 entry dataset while maintaining similar characteristics and qualities.
3. To avoid feeding the model repeated datasets I introduced a jitter that randomly ranged within +/- 0.5% for each given point, resorting the points as needed to retain formatting. 
4. In this script you can see the creation of my jitterBug function, processing the multiplication of the data, and saving the data as a new .csv. The script can be found [here](https://github.com/JamesWheeler4/James_Portfolio/blob/main/Proj_6%20Track%20and%20Field%20ML/python/ML_Data_Fab.py).

### **Creating GUI and Calling Models**
1. These saved models aren’t very useful sitting as files so I created a GUI that allows a user to select an event and enter an athlete's top marks. The model for the selected event is called forward and the marks are passed through the model, returning what would likely be the athlete’s next PR.
2. Starting with the GUI, I planned a rough structure, created the appropriate labels, entries and buttons, and experimented with placement. 
3. Adding function to the buttons and entries required gathering event names and normalizing factors for each dataset. This allowed the model to ingest data the same way it had been trained. Having these dictionaries paired to their respective locations, it's possible to pass entries through the model which returns a prediction.
4. To increase accessibility, I provide a calculator that allows a user to convert minutes/seconds to seconds which the model takes in. Likewise, if the outputs are over 70 seconds, they are provided in both second and minute/second formats.
5. The script that runs this GUI can be found [here](https://github.com/JamesWheeler4/James_Portfolio/blob/main/Proj_6%20Track%20and%20Field%20ML/python/ML_Tracki_GUI.py) and a image of the GUI can be found [here](https://github.com/JamesWheeler4/James_Portfolio/blob/main/Proj_6%20Track%20and%20Field%20ML/images/ML_Track_GUI.png).

