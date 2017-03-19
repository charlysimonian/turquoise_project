#On va essayer de trouver le meilleur classifieur donc on les importe tous on va entrainer notre 
#modèle avec tous les classifiers possible et comparer leurs perfs 

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis





names = ["Nearest Neighbors", "Linear SVM", "RBF SVM", "Gaussian Process",
         "Decision Tree", "Random Forest", "Neural Net", "AdaBoost",
         "Naive Bayes", "QDA"]

classifiers = [
    KNeighborsClassifier(3),
    SVC(kernel="linear", C=0.025),
    SVC(gamma=2, C=1),
    GaussianProcessClassifier(1.0 * RBF(1.0), warm_start=True),
    DecisionTreeClassifier(max_depth=5),
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
    MLPClassifier(alpha=1),
    AdaBoostClassifier(),
    GaussianNB(),
    QuadraticDiscriminantAnalysis()]

#on selectionne les features et les targets et on echantillonne les features en 
#donnée de tests de valisation et de test.

X_train = data.drop('target', axis=1).values            
y_train = data['target'].values                         
print 'Dimensions X_train=', X_train.shape, 'y_train=', y_train.shape
X_valid = data_io.read_as_df(basename, 'valid').values
X_test = data_io.read_as_df(basename, 'test').values
                           
                           
                           
clf = Classifier()
clf.fit(X_train, y_train)

Y_valid = clf.predict_proba(X_valid)
Y_test = clf.predict_proba(X_test)



#on compare les perfs avec le training accuracy

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
# Directly predicts the (categorical) class labels
y_predict = clf.predict(X_train)
print 'Training accuracy = ', accuracy_score(y_train, y_predict)
class_labels = clf.get_classes()     
print 'Class labels=', class_labels

confusion_matrix = confusion_matrix(y_train, y_predict, class_labels)
print 'Confusion matrix [known in lines, predicted in columns]=\n', confusion_matrix

balance_classification_rate = 1/2 * ( float(confusion_matrix[1,1])/float(confusion_matrix[0,1] + confusion_matrix[1,1]) ) + ( float(confusion_matrix[0,0])/float(confusion_matrix[0,0] + confusion_matrix[1,0]))                              
print 'Balance Classification Rate = ', balance_classification_rate
