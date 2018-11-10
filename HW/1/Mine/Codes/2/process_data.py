import numpy
import pandas


def find_class_probabilities(data_train):
    p_a = 0.0
    p_b = 0.0

    n_a = 0.0
    n_b = 0.0

    for p in range(1600):
        if data_train.values[p, 1593] == 1:
            n_a += 1.0
            p_a += 1.0
        elif data_train.values[p, 1593] == -1:
            p_b += 1.0
            n_b += 1.0

    p_a = p_a / 1600
    p_b = p_b / 1600

    return p_a, n_a, p_b, n_b


def calculate_probabilities(data_train, data_test):
    probability_test_a = numpy.empty((400, 1593))
    probability_test_b = numpy.empty((400, 1593))
    result = numpy.empty(400)

    for person in range(400):

        probability_temp_a = numpy.math.log(probability_a)
        probability_temp_b = numpy.math.log(probability_b)

        for question in range(1593):

            point = data_test.values[person, question]

            number_temp_a = 0.0
            number_temp_b = 0.0

            for points in range(1600):
                if data_train.values[points, question] == point:
                    if data_train.values[points, 1593] == 1:
                        number_temp_a += 1.0
                    else:
                        number_temp_b += 1.0

            if number_temp_a == 0.0:
                probability_test_a[person][question] = 1.0 / number_a + 1.0
            else:
                probability_test_a[person][question] = number_temp_a / number_a
            if number_temp_b == 0.0:
                probability_test_b[person][question] = 1.0 / number_b + 1.0
            else:
                probability_test_b[person][question] = number_temp_b / number_b

            probability_temp_a += numpy.math.log(probability_test_a[person][question])
            probability_temp_b += numpy.math.log(probability_test_b[person][question])

        if probability_temp_a > probability_temp_b:
            result[person] = 1
        else:
            result[person] = -1
        print("person " + str(person + 1) + " is " + str(int(result[person])))

    return result


data_set_train = pandas.read_csv('train.csv', header=None)
data_set_test = pandas.read_csv('test.csv', header=None)

probability_a, number_a, probability_b, number_b = find_class_probabilities(data_set_train)
result_probability = calculate_probabilities(data_set_train, data_set_test)

fault = 0
correct = 0
for i in range(400):
    if result_probability[i] == data_set_test.values[i, 1593]:
        correct += 1
    else:
        fault += 1

print(str(correct) + " items are classified True and " + str(fault) + "items are classified False")
print("So our accuracy is " + str(float(correct) / 400.0))

