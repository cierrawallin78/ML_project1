import numpy as np

class Calculations:
    def __init__(self, train, test, classes, att_values):
        self.q(train, test, classes, att_values)

    def q(self, train, test, classes, att_values):
        count = [0] * len(classes)
        q = [0] * len(classes)
        n = len(train)
        for i in range(n):
            for j in range(len(classes)):
                if train[i][-1] == classes[j]:
                    count[j] += 1

        for i in range (len(q)):
            q[i] = count[i]/n

        self.f(train, test, count, classes, q, att_values)

    def f(self, train, test, count, classes, q, att_values):
        attribute = np.zeros((len(count), (len(array[0]) - 1)))
        for i in range(len(array)):
            for j in range(len(array[0])):
                if array[i][j] == att_values[0]:        #change here
                    for k in range(len(classes)):
                        if array[i][-1] == classes[k]:
                            attribute[k][j] += 1
        for i in range(len(attribute)):
            for j in range(len(attribute[0])):
                attribute[i][j] += 1
                attribute[i][j] /= (count[i] + (len(array[0]) - 1))
        self.classify(attribute, q, classes)

    def classify(self, attribute, q, classes):
        product = [1] * len(attribute)
        for i in range(len(attribute)):
            for j in range(len(attribute[0])):
                product[i] *= attribute[i][j]
        for i in range(len(product)):
            product[i] *= q[i]
        index = product.index(max(product))
        print(classes[index])
