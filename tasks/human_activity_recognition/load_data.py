import os
import pandas as pd
import numpy as np
import tensorflow as tf


# load a single file as a numpy array
def load_file(filepath):
    dataframe = pd.read_csv(filepath, header=None, delim_whitespace=True)
    return dataframe.values


# load a list of files and return as a 3d numpy array
def load_group(filenames, prefix=''):
    print("filenames in load_group:", filenames)
    loaded = list()
    for name in filenames:
        print("loading data:", prefix + name)
        data = load_file(prefix + name)
        loaded.append(data)
    # stack group so that features are the 3rd dimension
    loaded = np.dstack(loaded)
    return loaded


# load a dataset group, such as train or test
def load_dataset_group(main_app_path, group, prefix=''):
    filepath = main_app_path + "/" + "datasets/" + prefix + group + '/Inertial Signals/'
    filepath_y_train = os.path.join(main_app_path, "datasets", prefix + group + '/y_' + group + '.txt')
    print("filepath:", filepath)
    # load all 9 files as a single array
    filenames = list()
    # total acceleration
    filenames += ['total_acc_x_' + group + '.txt', 'total_acc_y_' + group + '.txt', 'total_acc_z_' + group + '.txt']
    # body acceleration
    filenames += ['body_acc_x_' + group + '.txt', 'body_acc_y_' + group + '.txt', 'body_acc_z_' + group + '.txt']
    # body gyroscope
    filenames += ['body_gyro_x_' + group + '.txt', 'body_gyro_y_' + group + '.txt', 'body_gyro_z_' + group + '.txt']
    print("filenames:", filenames)
    # load input data
    X = load_group(filenames=filenames, prefix=filepath)
    # load class output
    y = load_file(filepath=filepath_y_train)
    return X, y


# load the dataset, returns train and test X and y elements
def load_dataset(main_app_path, prefix=''):
    # load all train
    trainX, trainy = load_dataset_group(main_app_path, 'train', prefix + 'UCI HAR Dataset/')
    print(trainX.shape, trainy.shape)
    # load all test
    testX, testy = load_dataset_group(main_app_path, 'test', prefix + 'UCI HAR Dataset/')
    print(testX.shape, testy.shape)
    # zero-offset class values
    trainy = trainy - 1
    testy = testy - 1
    # one hot encode y
    trainy = tf.keras.utils.to_categorical(trainy)
    testy = tf.keras.utils.to_categorical(testy)
    print(trainX.shape, trainy.shape, testX.shape, testy.shape)
    return trainX, trainy, testX, testy
