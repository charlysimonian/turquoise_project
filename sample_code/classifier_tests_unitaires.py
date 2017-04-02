from classifier import Classifier

clf = Classifier();

X =  {{4,	4,	4,	4},
      {4,	4	, 4,  4},
      {2,	2,	2,  2}}
      
Y  =  {0,0,1}

clf.fit(X,Y)
assert clf.predict({2,	2,	2,  2}) == 1
assert clf.predict({2,	4,	2,  2}) == 1
assert clf.predict({2,	4,	4,  4}) == 0
assert clf.predict({0,	0,	0,  0}) == 1
