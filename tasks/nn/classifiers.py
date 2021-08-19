import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Activation
from numpy import reciprocal
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV


def build_model():
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', input_shape=(28, 28, 1)))
    model.add(BatchNormalization())
    model.add(MaxPooling2D((2, 2)))
    model.add(Flatten())
    model.add(Dense(100, activation='relu', kernel_initializer='he_uniform'))
    model.add(BatchNormalization())
    model.add(Dense(10, activation='softmax'))

    model.compile(loss="sparse_categorical_crossentropy",
                  optimizer="sgd",
                  metrics=["accuracy"])

    return model


def keras_classifier(config, clf_params, param_grid, grid_mode="randomized"):
    keras_clf = KerasClassifier(build_fn=build_model)
    keras_clf.set_params(**clf_params)
    print("Classifier Parameters:\n", keras_clf.get_params())
    if grid_mode == "randomized":
        clf = RandomizedSearchCV(estimator=keras_clf,
                                 param_distributions=param_grid,
                                 n_iter=config["rndm_search"]["n_iter"],
                                 cv=config["tuning_train"]["cv"],
                                 verbose=config["tuning_train"]["verbose"])
    elif grid_mode == "gridsearch":
        clf = GridSearchCV(estimator=keras_clf,
                           param_grid=param_grid,
                           cv=config["tuning_train"]["cv"],
                           verbose=config["tuning_train"]["verbose"])
    else:
        print("Please define a valid Fine-tuning algorithm.")
        raise Exception

    return clf



