import numpy
import pandas


def find_class_probabilities(data_train):
    p_a = 0.0
    p_b = 0.0

    for p in range(1600):
        if data_train.values[p, 1593] == 1:
            p_a += 1.0
        elif data_train.values[p, 1593] == -1:
            p_b += 1.0

    p_a = p_a / 1600
    p_b = p_b / 1600

    return p_a, p_b


data_set_train = pandas.read_csv('train.csv', header=None)
data_set_test = pandas.read_csv('test.csv', header=None)

# sum_columns = data_set_train.sum(0)
# probability = numpy.empty((1600, 1593))
#
# for i in range(1593):
#     for j in range(1600):
#         probability[j][i] = data_set_train.values[j, i] / float(sum_columns[i])
#
#
# print(probability[0][6])

probability_a, probability_b = find_class_probabilities(data_set_train)

print(probability_a, probability_b)