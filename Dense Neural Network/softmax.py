import numpy as np


def softmax(input):
    #if type(input) != np.array:
    inp = np.asarray(input)
    inp = np.exp(inp)
    sums = np.sum(inp)
    output = inp/sums
    return output


if __name__ == '__main__' :
    a = np.array([(0,)])
    print(softmax(a))
