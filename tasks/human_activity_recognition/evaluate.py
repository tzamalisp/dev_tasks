import numpy as np


def evaluate_model(config, model, trainX, trainy, testX, testy):
    """
    fit and evaluate a model
    Args:
        config:
        model:
        trainX:
        trainy:
        testX:
        testy:

    Returns:

    """
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    # fit network
    model.fit(trainX, trainy,
              epochs=config["epochs"],
              batch_size=config["batch_size"],
              verbose=config["verbose"]
              )
    # evaluate model
    _, accuracy = model.evaluate(testX, testy,
                                 batch_size=config["batch_size"],
                                 verbose=config["verbose"])
    return accuracy


def summarize_results(scores):
    """
    summarize scores
    Args:
        scores:

    Returns:

    """
    print(scores)
    m, s = np.mean(scores), np.std(scores)
    print('Accuracy: %.3f%% (+/-%.3f)' % (m, s))
