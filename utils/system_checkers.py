import logging


def check_system_compatibility():
    """
    Check the system's libraries compatibility.
    Returns:

    """
    check_python()
    check_sklearn()
    check_tf()


def check_python():
    """
    Checks the Python version. Python ≥3.6 is required
    Returns:

    """
    import sys
    assert sys.version_info >= (3, 6)
    print(">> Python is compatible.")


def check_sklearn():
    """
    Checks the scikit-learn version. scikit-learn ≥0.20 is required.
    Returns:

    """
    import sklearn
    assert sklearn.__version__ >= "0.20"
    print(">> scikit-learn is compatible.")


def check_tf():
    """
    Checks the TensorFlow version. TensorFlow ≥2.0 is required.
    Returns:

    """
    import tensorflow as tf
    from tensorflow import keras
    assert tf.__version__ >= "2.0"
    if not tf.config.list_physical_devices('GPU'):
        print(">> No GPU is detected. LSTMs and CNNs can be very slow without a GPU. A GPU usage is recommended.")
    else:
        print(">> GPU usage is detected.")
    print(">> TensorFlow is compatible.")
