#PLEASE WRITE THE GITHUB URL BELOW!
#

import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing  import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score


def load_dataset(dataset_path):
    data_df = pd.read_csv(dataset_path)
    return data_df

def dataset_stat(dataset_df):
    features_size = dataset_df.shape[1]
    _target = data_df.groupby("target").size()
    return features_size - 1, _target[0], _target[1]

def split_dataset(dataset_df, testset_size):
    x = dataset_df.drop(columns='target', axis=1)
    y = dataset_df["target"]
    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=testset_size, random_state=2)
    return X_train, X_test, Y_train, Y_test

def decision_tree_train_test(x_train, x_test, y_train, y_test):
    dt_cls = DecisionTreeClassifier()
    dt_cls.fit(x_train, y_train)

    acc = accuracy_score(y_test, dt_cls.predict(x_test))
    prec = precision_score(y_test, dt_cls.predict(x_test))
    recall = recall_score(y_test, dt_cls.predict(x_test))
    return acc, prec, recall

def random_forest_train_test(x_train, x_test, y_train, y_test):
    rf_cls = RandomForestClassifier()
    rf_cls.fit(x_train, y_train)

    acc = accuracy_score(y_test, rf_cls.predict(x_test))
    prec = precision_score(y_test, rf_cls.predict(x_test))
    recall = recall_score(y_test, rf_cls.predict(x_test))
    return acc, prec, recall

def svm_train_test(x_train, x_test, y_train, y_test):
    svm_pipe = make_pipeline(
      StandardScaler(),
      SVC()
    )
    svm_pipe.fit(x_train, y_train)

    acc = accuracy_score(y_test, svm_pipe.predict(x_test))
    prec = precision_score(y_test, svm_pipe.predict(x_test))
    recall = recall_score(y_test, svm_pipe.predict(x_test))
    return acc, prec, recall

def print_performances(acc, prec, recall):
	print ("Accuracy: ", acc)
	print ("Precision: ", prec)
	print ("Recall: ", recall)


if __name__ == '__main__':
    data_path = sys.argv[1]
    data_df = load_dataset(data_path)

    n_feats, n_class0, n_class1 = dataset_stat(data_df)
    print ("Number of features: ", n_feats)
    print ("Number of class 0 data entries: ", n_class0)
    print ("Number of class 1 data entries: ", n_class1)

    print ("\nSplitting the dataset with the test size of ", float(sys.argv[2]))
    x_train, x_test, y_train, y_test = split_dataset(data_df, float(sys.argv[2]))

    acc, prec, recall = decision_tree_train_test(x_train, x_test, y_train, y_test)
    print ("\nDecision Tree Performances")
    print_performances(acc, prec, recall)

    acc, prec, recall = random_forest_train_test(x_train, x_test, y_train, y_test)
    print ("\nRandom Forest Performances")
    print_performances(acc, prec, recall)

    acc, prec, recall = svm_train_test(x_train, x_test, y_train, y_test)
    print ("\nSVM Performances")
    print_performances(acc, prec, recall)