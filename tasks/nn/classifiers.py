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
from tensorflow.keras.wrappers.scikit_learn import RandomizedSearchCV, KerasClassifier

from scipy.stats import reciprocal
from sklearn.model_selection import Randomized, GridSearchCV


def build_model(config):
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


def keras_classifier(config, model, grid_mode="randomized"):
    keras.backend.clear_session()
    keras_clf = KerasClassifier(build_fn=create_model)
    model.set_params(**clf_params)
    print("Classifier Parameters:\n", model.get_params())
    if grid_mode == "randomized":
        clf = RandomizedSearchCV(keras_clf,
                                 param_distribs,
                                 n_iter=10,
                                 cv=3,
                                 verbose=2)
    elif grid_mode == "gridsearch":
        clf = GridSearchCV(keras_clf, param_distribs,
                           cv=3,
                           verbose=2)
