import os
import yaml


def load_yaml(path_to_file=None, file_name=None):
    """
    Args:
        path_to_file: Path to the file.
        file_name: Yhe file name.
    Returns:
        The configuration data loaded from the template.
    """
    if path_to_file is None:
        path_to_file = os.path.join(os.getcwd(), "project_configuration")
    else:
        path_to_file = path_to_file
    if file_name is None:
        file_name = "config"
    else:
        file_name = file_name
    try:
        with open(os.path.join(path_to_file, f"{file_name}.yaml")) as fp:
            config_data = yaml.load(fp, Loader=yaml.FullLoader)
            if isinstance(config_data, dict):
                return config_data
            else:
                return None
    except ImportError:
        print("WARNING: could not import yaml module")
        return None
