#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""


"""

from sys import argv
from sklearn.base import BaseEstimator
from zDataManager import DataManager #The class provided by binome 1
# Note: if zDataManager is not ready, use the mother class DataManager
from sklearn.decomposition import PCA
from sklearn.ensemble import ExtraTreesClassifier
import numpy as np

class Preprocessor(BaseEstimator):
    def __init__(self):
        self.transformer = PCA(n_components=2)

    def fit(self, X, y=None):
        return self.transformer.fit(X, y)

    def fit_transform(self, X, y=None):
        
        
        #create an array where irrelevant ata have been deleted
		Data = data_test # supposing that it's the file where data test are

		std = np.std([tree.feature_importances_ for tree in Data.estimators_], axis=0) # Standard deviation
		avg = np.mean(Data)

		min_max_scaler = prepocesing.MinMaxScaler(feature_range=avg - 1.996 * std, avg + 1.996 * std)
		Data_scaled = min_max_scaler.fit_transform(Data)

        #normalize datas
        X = preprocessing.normalize(X, norm='l2')
        
        #Select best features 
        X_train = data.drop('target', axis=1).values 
        y_train = data['target'].values
        
        goodFeaturessorted = []

        model = ExtraTreesClassifier()
        model.fit(X_train, y_train)
        features = model.feature_importances_
        std = np.std([tree.feature_importances_ for tree in features.estimators_], axis=0)
        goodFeaturessorted = (-features).argsort()[:-20] # indexes of 20 best features sorted from best one to worst one of the array
        
        #create an array with good features 
        Xf=[]
        for i in range(X.__len__()):
            for y in range(goodFeaturessorted.__len__()):
                if i== goodFeaturessorted[y]: 
                    Xf.append(X[i])
        
        
                  
        return X
        

    def transform(self, X, y=None):
        return self.transformer.transform(X)

if __name__=="__main__":
    # We can use this to run this file as a script and test the Preprocessor
    if len(argv)==1: # Use the default input and output directories if no arguments are provided
        input_dir = "../public_data"
        output_dir = "../res"
    else:
        input_dir = argv[1]
        output_dir = argv[2];

    basename = 'lothlorian'
    D = DataManager(basename, input_dir) # Load data
    print("*** Original data ***")
    print D

    Prepro = Preprocessor()

    # Preprocess on the data and load it back into D
    D.data['X_train'] = Prepro.fit_transform(D.data['X_train'], D.data['Y_train'])
    D.data['X_valid'] = Prepro.transform(D.data['X_valid'])
    D.data['X_test'] = Prepro.transform(D.data['X_test'])

    # Here show something that proves that the preprocessing worked fine
    print("*** Transformed data ***")
    print D

