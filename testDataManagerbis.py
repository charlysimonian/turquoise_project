import random
import DataManager

input_dir = "../public_data"
basename = 'Lothlorian'

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
            '''
            create a new test object with random attributes and sets the
            corresponding arrays of not null features
            '''
            featuresList = []
            meanValues = []
            manager = DataManager(basename, input_dir)
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
            zDataManager
            '''
            if len(self.featuresList) - self.notNullCount() != nullCount:
                print("error in testFeaturesNotNull the method setNullFeatures in class zDataManager need improvements")
                
        def testFeaturesNotNull2(self, number):
            '''
            this method tests the setNotNullFeatures method from 
            zDataManager for number examples
            '''
            manager = DataManager(basename, input_dir)
            for i in range (number):
                self = testDataManager([], [], manager, True)
                self.testFeaturesNotNull(self.zeroValuesCount(self.meanValues))

print("\nObject 1 : \n")

manager = DataManager(basename, input_dir)
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