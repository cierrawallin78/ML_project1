import random
import numpy as np
import Calculations


class Reader:
    def get_values(self, array):
        att_values = []
        classes = []
        for i in range(len(array)):
            if array[i][-1] not in classes:
                classes.append(array[i][-1])
        for i in range(len(array)):
            for j in range(len(array[0])):
                if array[i][j] not in att_values:
                    att_values.append(array[i][j])
        for i in range(len(classes)):
            att_values.remove(classes[i])
        if '?' in att_values:
            att_values.remove('?')

        if (len(att_values)) > 2:
            array = self.discretize(array)
            att_values = [1, 0]

        self.missing(array, att_values, classes)

    def discretize(self, array):                    #change to how it was done in the notes
        average = [0] * (len(array[0]) - 1)
        for i in range(len(array[0]) - 1):
            for j in range(len(array)):
                average[i] += int(array[j][i])
        for i in range(len(average)):
            average[i] /= len(array)
        for i in range(len(array[0]) - 1):
            for j in range(len(array)):
                if int(array[j][i]) > average[i]:
                    array[j][i] = 1
                else:
                    array[j][i] = 0
        return array


    def missing(self, array, att_values, classes):
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
        training = np.empty([10, len(array), len(array[0])])
        print(training)
        np.random.shuffle(array)
        for i in range(int(len(array)/10)):
            for j in range(len(array[0])):
                training[k][i][j].insert(array[i][j])
        print(training[0])

        Calculations.Calculations(array, classes, att_values)

    def __init__(self, fname, class_pos):
        file = open(fname, 'r')
        array = np.array([line.strip('\n').split(',') for line in file.readlines()])
        if class_pos != -1:
            array = np.flip(array, 1)
        self.get_values(array)

def main():
    vote = Reader('house-votes-84.data', 0)
    bean = Reader('soybean-small.data', -1)

if __name__ == "__main__":
    main()
