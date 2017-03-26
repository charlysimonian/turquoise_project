from sklearn.base import BaseEstimator
from sklearn.ensemble import RandomForestClassifier
import pickle

from sklearn.svm import LinearSVC
from sklearn.calibration import CalibratedClassifierCV


class Classifier(BaseEstimator):
    def __init__(self):
        pass

    def fit(self, X, y):
	estimator = RandomForestClassifier(n_estimators=225, criterion='gini', max_depth=140, min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features='auto', max_leaf_nodes=None, min_impurity_split=1e-07, bootstrap=True, oob_score=False, n_jobs=1, random_state=None, verbose=0, warm_start=False, class_weight=None)
	self.clf =  CalibratedClassifierCV(base_estimator=estimator, method='sigmoid', cv=5)
	self.clf.fit(X, y)

    def predict(self, X):
        return self.clf.predict(X)

    def predict_proba(self, X):
        return self.clf.predict_proba(X) # The classes are in the order of the labels returned by get_classes
        
    def get_classes(self):
        return self.clf.classes_
        
    def save(self, path="./"):
        pickle.dump(self, open(path + '_model.pickle', "w"))

    def load(self, path="./"):
        self = pickle.load(open(path + '_model.pickle'))
        return self
