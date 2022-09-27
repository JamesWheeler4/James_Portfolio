import re
from tkinter import *
from tkinter import ttk
import customtkinter as ctk
import pandas
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import glob

path = r'C:\Users\15037\PycharmProjects\PythonForEveryone\AthleticProject\Track_ML_Models'
glob = glob.glob(path + '\*')


root = Tk()

# Description at top
desc_top = Label(root, justify=LEFT, anchor="w", text=('This tool can be used to predict the next PR of a given highschool track and field athlete'))
desc_top.grid(sticky=W, row=0, columnspan=5, padx=10, pady=5)
desc_second = Label(root, justify=LEFT, anchor="w", text=('Please enter a given athletes event followed by their top marks in seconds (highest(L) to lowest(R))'))
desc_second.grid(sticky=W, row=1, columnspan=5, padx=10, pady=5)


# Event selector
def show():
    event_blank.config(text=clicked.get())


options = ['Male 100m',
    'Male 110mh',
    'Male 200m',
    'Male 300mh',
    'Male 400m',
    'Male 800m',
    'Male 1500m',
    'Male 1600m',
    'Male 3000m',
    'Male 3200m',
    'Female 100m',
    'Female 100mh',
    'Female 200m',
    'Female 300mh',
    'Female 400m',
    'Female 800m',
    'Female 1500m',
    'Female 1600m',
    'Female 3000m',
    'Female 3200m',
    ]

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set("Male 100m")

# Create Dropdown menu
drop = OptionMenu( root , clicked , *options )
drop.grid(row=2, column=1, padx=10, pady=5)

button = Button(root, text="Enter Event", command=show)
button.grid(row=2, column=3, padx=10, pady=5)


event_label = Label(root, text='Event Selected:')
event_label.grid(row=4, column=0, padx=10, pady=5)
event_blank = Label(root, text =" ")
event_blank.grid(row=4, column=1, padx=10, pady=5)

prediction_label = Label(root, text='Predition:')
prediction_label.grid(row=5, column=0, padx=10, pady=5)
prediction_blank = Label(root, text=' ')
prediction_blank.grid(row=5, column=1, padx=10, pady=5)


# Mark input
entry_1 = Entry(root)
entry_1.grid(row=3, column=0, padx=10, pady=5)
entry_2 = Entry(root)
entry_2.grid(row=3, column=1, padx=10, pady=5)
entry_3 = Entry(root)
entry_3.grid(row=3, column=2, padx=10, pady=5)

# Normalizing factors
male_norms = {'100m': 19.21,
    '110mh': 19.68,
    '1500m': 324.7,
    '1600m': 350.9,
    '200m': 33.92,
    '3000m': 676.13,
    '300mh': 47.7,
    '3200m': 640.02,
    '400m': 80.9,
    '800m': 165.63}

female_norms = {'100mh': 19.0,
    '100m': 17.21,
    '1500m': 322.5,
    '1600m': 333.58,
    '200m': 33.39,
    '3000m': 670.51,
    '300mh': 52.65,
    '3200m': 716.81,
    '400m': 82.64,
    '800m': 169.77}

# Intaking event and outputting prediction
def myClick():
    gender = clicked.get().split(' ')[0]
    event = clicked.get().split(' ')[1]
    if gender == 'Male':
        normer = male_norms.get(event)
    else:
        normer = female_norms.get(event)
    print(gender, event, normer)
    cols = ['m2', 'm3', 'm4']
    df = pandas.DataFrame(columns=cols)
    df.loc[0] = [float(entry_1.get())/normer, float(entry_2.get())/normer, float(entry_3.get())/normer]
    print(df)
    for files in glob:
        events = files.split('_')[2:]
        file_gender = events[0][7:]
        file_event = events[1]
        if file_gender == gender and file_event == event:
            file = files
    print(file)
    reconstructed_model = keras.models.load_model(file)
    predictions = reconstructed_model.predict(df)
    prediction = round(float(predictions[0][0]), 2)
    if prediction < 70:
        predition_blank = Label(root, text=f"{prediction} Seconds")
        predition_blank.grid(row=5, column=1, padx=10, pady=5)
    else:
        prediction_minutes = int(prediction/60)
        prediction_seconds = round(prediction%60, 2)
        predition_blank = Label(root, text=f"{prediction} Seconds or {prediction_minutes} Minute(s) and {prediction_seconds} Seconds")
        predition_blank.grid(row=5, column=1, columnspan=2, padx=10, pady=5)

myButton = Button(root, text='Enter Marks', command=myClick)
myButton.grid(row=3, column=3, padx=10, pady=5)


# Minute to Seconds converter

def msCalc():
    seconds = (float(entry_minute.get())*60) + float(entry_second.get())
    print(seconds)
    calc_return = Label(root, text=seconds)
    calc_return.grid(row=9, column=3, padx=10, pady=5)

calc_label = Label(root, justify=LEFT, anchor="w", text=('Covert minutes and seconds to seconds here:'))
calc_label.grid(sticky=W, row=7, columnspan=2, padx=10, pady=5)

minute_label = Label(root, justify=LEFT, anchor="w", text=('Minutes:'))
minute_label.grid(row=8, column=0, padx=10, pady=5)
entry_minute = Entry(root)
entry_minute.grid(row=8, column=1, padx=10, pady=5)

second_label = Label(root, justify=LEFT, anchor="w", text=('Seconds:'))
second_label.grid(row=9, column=0, padx=10, pady=5)
entry_second = Entry(root)
entry_second.grid(row=9, column=1, padx=10, pady=5)

calc_button = Button(root, text='Calculate', command=msCalc)
calc_button.grid(row=9, column=3, padx=10, pady=5)

return_label = Label(root, text="Total Seconds:")
return_label.grid(row=8, column=2, padx=10, pady=5)
return_fill = Label(root, text=" ")
return_fill.grid(row=8, column=3, padx=10, pady=5)


root.mainloop()
