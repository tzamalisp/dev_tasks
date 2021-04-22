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


def save_paths(config, section_id):
    """
    Make the save paths
    Args:
        config: The configuration file.
        section_id: The ID name of the section where to save the data.
    Returns:
        Dictionary with the save paths.
    """
    if config["path_app_saving"] is None:
        path_main_saving_dir = os.getcwd()
    else:
        path_main_saving_dir = config["path_app_saving"]
    # where to save the images
    path_images = os.path.join(path_main_saving_dir, "images", section_id)
    os.makedirs(path_images, exist_ok=True)

    return {
        "path_images": path_images
    }
