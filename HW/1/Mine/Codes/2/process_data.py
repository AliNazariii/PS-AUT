import numpy
import pandas

data_set_train = pandas.read_csv('train.csv', header=None)
data_set_test = pandas.read_csv('test.csv', header=None)

sum_columns = data_set_train.sum(0)
probability = numpy.empty((1600, 1593))

for i in range(1593):
    for j in range(1600):
        probability[j][i] = data_set_train.values[j, i] / float(sum_columns[i])


print(probability[0][6])
