import random
from matplotlib import pyplot


def simulate(flip_number, h_probability):
    count = 0
    point_list = []
    for i in range(1, flip_number):
        if random.random() < h_probability:
            count += 1
        point_list.append(count)


    pyplot.title('H Probability = ' + str(h_probability))
    print('Number of heads at the End: ' + str(count))

    pyplot.plot(range(1, flip_number), point_list)
    pyplot.axis([0, 1000, 0, 1000])


simulate(1000, 0.7)
pyplot.show()

