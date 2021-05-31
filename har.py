import os
import sys
from tasks.human_activity_recognition.load_data import load_dataset
from tasks.human_activity_recognition.evaluate import evaluate_model, summarize_results
from tasks.human_activity_recognition.models import cnn_params, cnn
from tasks.project_configuration.configuration import config_data

print("Python version: {}".format(sys.version))
print("Version info: {}".format(sys.version_info))


def run_experiment(config):
    """
    run an experiment
    Args:
        config:

    Returns:

    """
    # load data
    trainX, trainy, testX, testy = load_dataset(main_app_path)
    n_timesteps, n_features, n_outputs = cnn_params(trainX, trainy)
    model = cnn(n_timesteps, n_features, n_outputs)
    # repeat experiment
    scores = []
    for r in range(config["repeats"]):
        score = evaluate_model(config, model, trainX, trainy, testX, testy)
        score = score * 100.0
        print('>#%d: %.3f' % (r + 1, score))
        scores.append(score)
    # summarize results
    summarize_results(scores)


if __name__ == '__main__':
    main_app_path = os.getcwd()
    config_data = config_data()
    print(config_data)
    print(main_app_path)
    # run the experiment
    run_experiment(config_data)
