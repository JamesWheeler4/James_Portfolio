import pandas as pd
import numpy as np
import tensorflow as tf
import glob
import os
from tensorflow import keras
from tensorflow.keras import layers

# Collecting data
path_10 = r'C:\...\AthleticProject\ML_data\Top_10_Marks'
path_6 = r'C:\...\AthleticProject\ML_data\Top_6_Marks'
path_4 = r'C:\...\AthleticProject\ML_data\Top_4_Marks'
path_multi = r'C:\...\AthleticProject\ML_data_multi_track_2'

glob_10 = glob.glob(path_10 + '\*.csv')
glob_6 = glob.glob(path_6 + '\*.csv')
glob_4 = glob.glob(path_4 + '\*.csv')
glob_multi = glob.glob(path_multi + '\*.csv')

redo_list = []
comp_list = []
# to_do = ['Male_']

# Creating and training model for each event
for x in glob_multi:

    # Pulling Data
    df = pd.read_csv(f'{x}')

    # Setting name for each loop
    names = x.split('2')[1].split('_')
    gender = names[0]
    name = gender[1:]+'_'+names[1]
    # print(name)

    # Allows for narrowing down which events are being processed
    # if name not in to_do:
    #     print('skipped', name)
    #     continue

    # Setting the MAE goal of within 1% of the average mark
    df_avg = df['m1'].mean()
    goal_mae = df['m1'].mean()*.01

    # Shuffle data inplace
    np.random.shuffle(df.values)

    # Splitting data into training and testing dataframes
    train_df = df.sample(frac=0.8, random_state=0)
    test_df = df.drop(train_df.index)

    # Removing athlete_id
    train_labels = train_df.pop('m1')
    test_labels = test_df.pop('m1')

    # Creating normalized data so each data point is between 0 and 1
    normer = df['m1'].max()
    def norm(x):
        return (x / normer)
    normed_train_df = norm(train_df)
    normed_test_df = norm(test_df)

    # Creating the model
    def build_model():
        model = keras.Sequential([
            layers.Dense(64, activation=tf.nn.relu, input_shape=[len(train_df.keys())]),
            layers.Dense(64, activation=tf.nn.relu),
            layers.Dense(64, activation=tf.nn.relu),
            layers.Dense(64, activation=tf.nn.relu),
            layers.Dense(1)
        ])

        optimizer = tf.keras.optimizers.RMSprop(0.001)

        model.compile(loss='mse',
                      optimizer=optimizer,
                      metrics=['mae', 'mse'])
        return model

    model = build_model()

    # model.summary()

    # example_batch = normed_train_df[:10]
    # example_result = model.predict(example_batch)
    # print('Example Results', x)
    # print(example_result)

    # Creates visual of training occurring
    class PrintDot(keras.callbacks.Callback):
        def on_epoch_end(self, epoch, logs):
            if epoch % 100 == 0: print('')
            print('.', end='')

    # Setting max epochs
    EPOCHS = 1000


    current_mae = 101
    calc_mae = 100
    loop_cnt = 0
    print(name, f'Goal:{goal_mae}')
    while calc_mae > goal_mae or loop_cnt < 10:  # retraining until model creates criteria
        # Prevents training into frivolous cycles
        early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=10)

        # history = model.fit(
        #     normed_train_df, train_labels,
        #     epochs=EPOCHS, validation_split=0.2, verbose=0,
        #     callbacks=[early_stop, PrintDot()])

        loss, mae, mse = model.evaluate(normed_test_df, test_labels, verbose=0)

        calc_mae = float('{:5.2f}'.format(mae))
        # print('testing: ', goal_mae - calc_mae)
        loop_cnt += 1
        print('Loop:', loop_cnt)
        if calc_mae < current_mae:  # Saving best model over course of training
            current_mae = calc_mae
            print('Model updated: ', current_mae)
            # model.save(f'.\Track_ML_Models\{name}_LinReg_Model')  # Engage when training

        if loop_cnt > 500:  # Set a max number of training repetitions
            print('Breaking out')
            dif = goal_mae - current_mae
            items = (name, f'Goal:{goal_mae}', f'Actual:{current_mae}', f'Difference: {dif}')
            redo_list.append(items)  # Collects events that didn't meet the criteria
            break
    dif = goal_mae - current_mae
    items_comp = (name, f'Goal:{goal_mae}', f'Actual:{current_mae}', f'Difference: {dif}')
    comp_list.append(items_comp)  # Collects the events that are completed and their information

    # 'Testing set MAE: {:5.2f}'.format(mae),
    print(x.split('_')[-3:])
    print('Saved: ', current_mae, 'Goal MAE: ', goal_mae)
    # input('next?')
    continue

# Printing summary of models created
print('Redo List:')
for y in redo_list:
    print(y)
print('Completed List:')
for c in comp_list:
    print(c)

