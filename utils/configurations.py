import os
import yaml


def config_data(tool_path=None, config_file_path="config.yaml"):
    """
    Load the configuration data from the relevant yaml file.

    Args:
        tool_path: (str) The path of the main tool script.
        config_file_path: (str) The name of the yaml configuration file that is stored. It must be inside the
        "configuration" directory. Default: "configuration.yaml"

    Returns:
        A dictionary that contains the configuration data from the yaml file.
    """
    if tool_path is not None and config_file_path == "config.yaml":
        path = os.path.join(tool_path, "configuration", config_file_path)
    else:
        path = config_file_path
    try:
        with open(path) as file:
            # The FullLoader parameter handles the conversion from YAML
            # scalar values to Python the dictionary format
            data = yaml.load(file, Loader=yaml.FullLoader)
    except Exception as e:
        print("Cannot load the yaml file: {}".format(e))
        raise

    return data
