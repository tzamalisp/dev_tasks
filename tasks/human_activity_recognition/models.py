import tensorflow as tf


def cnn_params(train_X, train_y):
    """

    Args:
        train_X:
        train_y:

    Returns:

    """
    n_timesteps, n_features, n_outputs = train_X.shape[1], train_X.shape[2], train_y.shape[1]
    return n_timesteps, n_features, n_outputs


def cnn(n_timesteps, n_features, n_outputs):
    """

    Args:
        n_timesteps:
        n_features:
        n_outputs:

    Returns:

    """
    model = tf.keras.models.Sequential()
    model.add(
        tf.keras.layers.Conv1D(filters=64, kernel_size=3, activation='relu', input_shape=(n_timesteps, n_features)))
    model.add(tf.keras.layers.Conv1D(filters=64, kernel_size=3, activation='relu'))
    model.add(tf.keras.layers.Dropout(0.5))
    model.add(tf.keras.layers.MaxPooling1D(pool_size=2))
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(100, activation='relu'))
    model.add(tf.keras.layers.Dense(n_outputs, activation='softmax'))

    return model
