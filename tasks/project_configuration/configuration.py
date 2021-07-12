import os
import yaml


def config_data(path_to_file=None, file_name="config"):
    """
    Load the configuration data from the relevant yaml file.

    Args:
        path_to_file: (str) The path to the file. Default: "<package_dir>/tasks/project_configuration.config.yaml
        file_name: (str) The name of the yaml configuration file that is stored. It must be inside the
        "project_configuration" directory. Default: "config.yaml"

    Returns:
        A dictionary that contains the configuration data from the yaml file.
    """
    if path_to_file is None:
        path = os.path.join(os.getcwd(), "tasks", "project_configuration")
    else:
        path = path_to_file
    if file_name is not None:
        file_name = file_name
    try:
        with open(os.path.join(path, f"{file_name}.yaml")) as fp:
            data = yaml.load(fp, Loader=yaml.FullLoader)
            if isinstance(data, dict):
                return data
            else:
                raise Exception("ERROR: The configuration data is not in proper dictionary format.")
    except ImportError:
        print("ERROR: could not import yaml module")
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
