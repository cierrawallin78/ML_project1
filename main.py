import random
import numpy as np
import Calculations


class Reader:
    def get_values(self, array, class_pos):
        att_values = []
        classes = []
        for i in range(len(array)):
            if array[i][class_pos] not in classes:
                classes.append(array[i][class_pos])
        for i in range(len(array)):
            for j in range(len(array[0])):
                if array[i][j] not in att_values:
                    att_values.append(array[i][j])
        for i in range(len(classes)):
            att_values.remove(classes[i])
        att_values.remove('?')
        self.missing(array, class_pos, att_values, classes)

    def missing(self, array, class_pos, att_values, classes):
        for i in range(len(array)):
            for j in range(len(array[0])):
                if array[i][j] == "?":
                    decision = random.choice(att_values)
                    array[i][j] = decision
        self.shuffle(array, class_pos, att_values, classes)
        Calculations.Calculations(array, class_pos, classes)

    def shuffle(self, array, class_pos, att_values, classes):
        

    def __init__(self, fname, class_pos):
        file = open(fname, 'r')
        array = np.array([line.strip('\n').split(',') for line in file.readlines()])
        self.get_values(array, class_pos)

def main():
    vote = Reader('house-votes-84.data', 0)

if __name__ == "__main__":
    main()
