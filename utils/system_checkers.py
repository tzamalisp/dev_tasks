def check_python_version():
    """
    Checks the Python version. Python ≥3.6 is required
    Returns:

    """
    import sys
    assert sys.version_info >= (3, 6)


def check_sklearn_version():
    """
    Checks the scikit-learn version. scikit-learn ≥0.20 is required.
    Returns:

    """
    import sklearn
    assert sklearn.__version__ >= "0.20"


def check_tf_version():
    """
    Checks the TensorFlow version. TensorFlow ≥2.0 is required.
    Returns:

    """
    import tensorflow as tf
    from tensorflow import keras
    assert tf.__version__ >= "2.0"
    if not tf.config.list_physical_devices('GPU'):
        print("No GPU is detected. LSTMs and CNNs can be very slow without a GPU. A GPU usage is recommended.")
    else:
        print("GPU usage is detected.")