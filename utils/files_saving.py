import os
import matplotlib.pyplot as plt
# plot pretty figures
import matplotlib as mpl
mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)


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


def save_fig(config, section_id, fig_id, tight_layout=True, fig_extension="png", resolution=300):
    paths = save_paths(config=config,section_id=section_id)
    path = os.path.join(paths["path_images"], fig_id + "." + fig_extension)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)
