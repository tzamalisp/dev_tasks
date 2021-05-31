import os
import matplotlib.pyplot as plt
# plot pretty figures
import matplotlib as mpl
mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)


def save_fig(saving_path, fig_id, tight_layout=True, fig_extension="png", resolution=300):
    path = os.path.join(saving_path, fig_id + "." + fig_extension)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)
