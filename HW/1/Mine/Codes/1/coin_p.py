import random
from matplotlib import pyplot


def simulate(flip_number, h_probability):
    count = 0
    point_list = []
    for i in range(1, flip_number):
        if random.random() < h_probability:
            count += 1
        point_list.append(count)
        if i == 50 or i == 100 or i == 500 or i == 1000:
            print('Number of heads in round ' + str(i) + ' = ' + str(count))

    pyplot.title('H Probability = ' + str(h_probability))
    print('Number of heads at the End: ' + str(count))

    pyplot.plot(range(1, flip_number), point_list)
    pyplot.axis([0, 1000, 0, 1000])


simulate(1000, 0.7)
pyplot.show()

