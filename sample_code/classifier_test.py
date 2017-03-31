from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.cross_validation import StratifiedShuffleSplit
import libscores
from libscores import bac_metric
from libscores import auc_metric
from libscores import f1_metric
from libscores import binarize_predictions


#Directly predicts the (categorical) class labels
y_predict = clf.predict(X_train)
print 'Training accuracy = ', accuracy_score(y_train, y_predict)
class_labels = clf.get_classes()
print 'Class labels=', class_labels

confusion_matrix = confusion_matrix(y_train, y_predict, class_labels)
print 'Confusion matrix [known in lines, predicted in columns]=\n', confusion_matrix

balance_classification_rate = 1/2 * ( float(confusion_matrix[1,1])/float(confusion_matrix[0,1] + confusion_matrix[1,1]) ) + ( float(confusion_matrix[0,0])/float(confusion_matrix[0,0] + confusion_matrix[1,0]))
print 'Balance Classification Rate = ', balance_classification_rate




# This is just an example of k-fold cross-validation
skf = StratifiedShuffleSplit(y_train, n_iter=10, test_size=0.5, random_state=61, )
i=0
for idx_t, idx_v in skf:
    i=i+1
    Xtr = X_train[idx_t]
    Ytr = y_train[idx_t]
    Xva = X_train[idx_v]
    Yva = y_train[idx_v]
    clf = Classifier()
    clf.fit(Xtr, Ytr)
    Y_predict = clf.predict(Xva)
    print 'Fold', i, 'validation accuracy = ', accuracy_score(Y_predict, Yva)



# We use binary classification!
Y_train, C = libscores.onehot(y_train)
print 'Dimensions Y_train=', Y_train.shape, 'Class labels=', C
assert((class_labels==C).all()) # Just to make sure the labels of the classifier are in the right order
# Note: if all went well, you should recover public_data/lothlorian_train.solution
# You had it all along, but to show you some nice plots we loaded the data as a data frame so we lost it!


# Predicts probabilities, a matrix patnum x classnum
# As solution, you must use Y_train, not y_train
y_predict_proba = clf.predict_proba(X_train)

y_predict = binarize_predictions(y_predict_proba, task='binary.classification')

print 'Training balanced accuracy = ', bac_metric(Y_train, y_predict, task='binary.classification')
print 'Training AUC = ', auc_metric(Y_train, y_predict, task='binary.classification')
print 'Training F1 measure = ', f1_metric(Y_train, y_predict, task='binary.classification')