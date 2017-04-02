# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import random
import sys
sys.path.insert(0, 'C:\Program Files (x86)\pythonxy\doc\Libraries\seaborn-0.7.1\seaborn-0.7.1')
import seaborn as sns; sns.set()
sys.path.insert(0, 'C:\Program Files (x86)\pythonxy\doc\Libraries\pandas')
import pandas as pd

class DataManager():
    
		def setNotNullFeatures(self, featuresList, meanValues):
			'''save null features in a list as attribute'''
			featuresNotNull = []
			for i in range (len(meanValues)) :
				if meanValues[i] != 0 :
					featuresNotNull.append(featuresList[i])
			self.notNullFeatures = featuresNotNull
			
		
		def toDF(self, set_name,data):
			''' Change a given data subset to a data Panda's frame.
				set_name is 'train', 'valid' or 'test'.'''
			DF = pd.DataFrame(data)         
			return DF
			
			
		def ShowScatter(self, data, set_name):
			'''Show scatter plots'''
			DF = self.toDF(set_name, data)
			ax = DF.plot(style=".", title = set_name)
			ax.set_xlabel("x label")
			ax.set_ylabel("y label")
   
		def CreateRandomData(self, number):
			'''Create a list filled with random integers'''
			tab = []
			for i in range (number):
				tab.append(random.randint(1, 100))
			return tab

class testDataManager:
        
        '''
        this class has differents methods useful to test the differents
        methods from the zDataManager class
        '''        
        
        def __init__(self, featuresList, meanValues, zDataManager, randomize):
            '''
            construct a new test object with 2 arrays and one array 
            with the null features from zDataManager class
            '''
            if randomize:
                self.randomize()
            else:
                self.featuresList = featuresList
                self.meanValues = meanValues
                self.notNullFeatures = zDataManager.notNullFeatures
            
        def randomize(self):
            featuresList = []
            meanValues = []
            manager = DataManager()
            rand1 = random.randint(1, 10)
            for i in range (rand1+1):
                rand2 = random.randint(0, 2)
                featuresList.append(i)
                meanValues.append(rand2)
            manager.setNotNullFeatures(featuresList, meanValues)
            self.featuresList = featuresList
            self.meanValues = meanValues
            self.notNullFeatures = manager.notNullFeatures
            
        def printDatas(self):
            '''print the differents attributes in this class'''
            print("list of features : ")
            print(self.featuresList)
            print("mean values for each features : ")
            print(self.meanValues)
            print("list of features with mean values not at 0 : ")
            print(self.notNullFeatures)
            
        def zeroValuesCount(self, tab):
            '''return the number of zero values in an array of numbers'''
            count = 0
            for i in tab:
                if i == 0:
                    count+=1
            return count
            
        def notNullCount(self):
            '''
            return the size of the array which contains the null features 
            list
            '''
            '''
            important thing : the object need to bee instanciated before 
            using this method
            '''
            return len(self.notNullFeatures)
        
        def testFeaturesNotNull(self, nullCount):
            '''
            this method tests the setNotNullFeatures method from 
            zDataManager for one example
            '''
            if len(self.featuresList) - self.notNullCount() != nullCount:
                print("error in testFeaturesNotNull the method setNullFeatures in class zDataManager need improvements")
                
        def testFeaturesNotNull2(self, number):
            '''
            this method tests the setNotNullFeatures method from 
            zDataManager for number examples
            '''
            manager = DataManager()
            for i in range (number):
                self = testDataManager([], [], manager, True)
                self.testFeaturesNotNull(self.zeroValuesCount(self.meanValues))
	
        def testScatterPlot(self, data):
            manager = DataManager()
            print("test to create a scatter plot")
            manager.ShowScatter(data, "test")
			
			

print("\nObject 1 : \n")
manager = DataManager()
featuresList = [0, 1, 2]
meanValues = [2, 9, 0]
manager.setNotNullFeatures(featuresList, meanValues)

test1 = testDataManager(featuresList, meanValues, manager, False)
test1.printDatas()
test1.testFeaturesNotNull(test1.zeroValuesCount(test1.meanValues))

print("\nObject 2 (random) : \n")
test2 = testDataManager([], [], manager, True)
test2.printDatas()
test2.testFeaturesNotNull(test2.zeroValuesCount(test2.meanValues))

number = 100000
print("applying now testFeaturesNotNull on", number, "objects")
test1.testFeaturesNotNull2(number)


test3 = testDataManager(featuresList, meanValues, manager, False)
number = 100
data = manager.CreateRandomData(number)
test3.testScatterPlot(data)
