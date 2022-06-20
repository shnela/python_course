from typing import List

import numpy as np
from sklearn import datasets
import pickle
from sklearn.neighbors import KNeighborsClassifier


def reload_pickle_model(knn_model, filename='trained_knn_model.sav'):
    # save the knn_model to disk
    pickle.dump(knn_model, open(filename, 'wb'))
    # load the model from disk
    knn_model_reloaded = pickle.load(open(filename, 'rb'))

    return knn_model_reloaded


def reload_test_data(test_x_data, test_y_data, filename='iris_test_data.csv'):
    common_array = np.c_[test_y_data, test_x_data]  # set test_y_data as first column

    # save as csv file
    np.savetxt(filename, common_array, delimiter=';')
    # and read back
    common_array_reloaded = np.genfromtxt(filename, delimiter=";")

    # split read common array to x and y test data again
    test_y_data_reloaded = common_array_reloaded[:, 0]
    test_x_data_reloaded = common_array_reloaded[:, 1:]

    return test_x_data_reloaded, test_y_data_reloaded


def count_score(test_data: List, prediction: List) -> float:
    """Dummy score standard"""
    assert len(test_data) == len(prediction)
    number_of_equal = sum(1 for test_el, predicted_el in zip(test_data, prediction) if test_el == predicted_el)
    return number_of_equal / len(test_data)


def run_iris_example(use_file=False):
    iris = datasets.load_iris()
    iris_x = iris.data
    iris_y = iris.target
    np.unique(iris_y)

    # Split iris data in train and test data
    # A random permutation, to split the data randomly
    np.random.seed(0)
    indices = np.random.permutation(len(iris_x))
    iris_x_train = iris_x[indices[:-10]]
    iris_y_train = iris_y[indices[:-10]]
    iris_x_test = iris_x[indices[-10:]]
    iris_y_test = iris_y[indices[-10:]]

    # Create and fit a nearest-neighbor classifier
    knn_model = KNeighborsClassifier()
    knn_model.fit(iris_x_train, iris_y_train)

    if use_file:
        knn_model = reload_pickle_model(knn_model)
        iris_x_test, iris_y_test = reload_test_data(iris_x_test, iris_y_test)

    prediction = knn_model.predict(iris_x_test)
    score = count_score(iris_y_test, prediction)
    return score


if __name__ == '__main__':
    score = run_iris_example(use_file=True)
    print(score)
