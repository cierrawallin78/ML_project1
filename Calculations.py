import numpy as np

class Calculations:
    def __init__(self, array, class_pos, classes):
        self.q(array, class_pos, classes)

    def q(self, array, class_pos, classes):
        count = [0] * len(classes)
        q = [0] * len(classes)
        n = len(array)
        for i in range(n):
            for j in range(len(classes)):
                if array[i][class_pos] == classes[j]:
                    count[j] += 1

        for i in range (len(q)):
            q[i] = count[i]/n

        self.f(array, count, classes, q)

    def f(self, array, count, classes, q):
        attribute = np.zeros((len(count), (len(array[0]) - 1)))
        for i in range(len(array)):
            for j in range(len(array[0]) - 1):           #fix j range so first value isnt included ex the class column
                if array[i][j + 1] == 'y':                  #change this +1 so that it works if class is at end
                    for k in range(len(classes)):
                        if array[i][0] == classes[k]:
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
        print(product)
        index = product.index(max(product))
        print(classes[index])
