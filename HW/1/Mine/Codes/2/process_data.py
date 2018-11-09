import pandas

data_set_train = pandas.read_csv('train.csv', header=None)
data_set_test = pandas.read_csv('test.csv', header=None)

print(data_set_train)
