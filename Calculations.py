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
        attribute = np.zeros((2, len(count), (len(train[0]) - 1)))
        for i in range(len(train)):
            for j in range(len(train[0])):
                if train[i][j] == att_values[0]:
                    for k in range(len(classes)):
                        if train[i][-1] == classes[k]:
                            attribute[0][k][j] += 1
                elif train[i][j] == att_values[1]:
                    for k in range(len(classes)):
                        if train[i][-1] == classes[k]:
                            attribute[1][k][j] += 1
        for i in range(len(attribute)):
            for j in range(len(attribute[0])):
                for k in range(len(attribute[0][0])):
                    attribute[i][j][k] += 1
                    attribute[i][j][k] /= (count[i] + (len(train[0]) - 1))
        self.classify(attribute, test, q, classes, att_values)

    def classify(self, attribute, test, q, classes, att_values):
        product = np.ones((len(test), len(classes)))
        for i in range(len(test)):
            for j in range(len(classes)):
                for k in range(len(attribute)):
                    if test[i][j] == att_values[0]:
                        product[i][j] *= attribute[0][j][k]
                    elif test[i][j] == att_values[1]:
                        product[i][j] *= attribute[1][j][k]
        for i in range(len(product)):
            for j in range(len(product[0])):
                product[i][j] *= q[j]
        for i in range(len(product)):
            index = np.argmax(product[i])

            print('new')
            print(classes[index])
            print(test[i][-1])
