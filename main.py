import random
import numpy as np
import Calculations


class Reader:
    def get_values(self, array):                        #gets class and attribute values
        att_values = []
        classes = []
        for i in range(len(array)):
            if array[i][-1] not in classes:             #if class is not already in the array, add it
                classes.append(array[i][-1])
        for i in range(len(array)):
            for j in range(len(array[0])):
                if array[i][j] not in att_values:       #creates an array of all possible values in data
                    att_values.append(array[i][j])
        for i in range(len(classes)):
            att_values.remove(classes[i])               #removes class names leaving possible attribute values and '?'
        if '?' in att_values:
            att_values.remove('?')                      #removes '?' leaving an array of possible attribute values

        if (len(att_values)) > 2:                       #if the data is not binary, discretize the data
            array = self.discretize(array)
            att_values = [1, 0]
        self.missing(array, att_values, classes)

    def discretize(self, array):                    #discretized into two bins so all data is binary
        mean = array[:,:-1].astype(np.float)
        mean = np.mean(mean, axis=0)
        for i in range(len(array[0]) - 1):
            for j in range(len(array)):
                if int(array[j][i]) > mean[i]:
                    array[j][i] = 1
                else:
                    array[j][i] = 0
        return array


    def missing(self, array, att_values, classes):
        print(type(array))
        print(len(array))
        for i in range(len(array)):
            for j in range(len(array[0])):
                if array[i][j] == "?":
                    decision = random.choice(att_values)
                    array[i][j] = decision
        print('as given')
        self.cross_validation(array, classes, att_values)
        self.shuffle(array, classes, att_values)



    def shuffle(self, array, classes, att_values):
        print('shuffled')
        shuffle_num = int((len(array[0]) - 1) * .1)
        if shuffle_num == 0:
            shuffle_num = 1
        for i in range(shuffle_num):
            shuffle = random.randint(0, len(array[0]) - 1)
            np.random.shuffle(array[:,shuffle])

        self.cross_validation(array, classes, att_values)

    def cross_validation(self, array, classes, att_values):
        np.random.shuffle(array)
        end = int(len(array)/10)
        start = 0
        for i in range(10):
            test = array[start:end,0:len(array[0])]             #check out the training sets and how they are concating
            train1 = array[0:start,0:len(array[0])]
            train2 = array[end:len(array),0:len(array[0])]
            train = np.concatenate((train1, train2))
            Calculations.Calculations(test, train, classes, att_values)
            start += int(len(array)/10)
            end += int(len(array)/10)








    def __init__(self, fname, class_pos):
        file = open(fname, 'r')
        array = np.array([line.strip('\n').split(',') for line in file.readlines()])    #creates an array of data split by commas and lines
        if class_pos != -1:                                                             #if the class is not in the last column, the data is flipped so it is
            array = np.flip(array, 1)
        self.get_values(array)

def main():
    vote = Reader('house-votes-84.data', 0)
    bean = Reader('soybean-small.data', -1)

if __name__ == "__main__":
    main()
