from DenseNeuralNetwork_5 import *
from random import randint


nn = NeuralNetwork(2,75,1, layers = 7)


inputs=((1,1),(0,0),(1,0),(0,1))
outputs=((0,),(0,),(1,),(1,))

rand_list = list()
for i in range(10000):
    q = randint(0,3)
    rand_list.append(q)
q = 0
for i in rand_list:
    arr    = np.array((inputs[i],))
    target = np.array((outputs[i],))

    #record the shape to be able to convert it back later
    shape = arr.shape

    # make a 1-dimensional view of arr
    flat_arr = arr.ravel()

    # convert it to a matrix
    vector = np.matrix(flat_arr)

    #convert it in to a collom matrix
    vector = np.transpose(vector)

    #add all the vector in to a single matrix (broadcasting)
    if q == 0:
        a = vector
        t = target
    else:
        a = np.concatenate((a,vector), axis=1)
        t = np.concatenate((t,target), axis=1)
    q += 1
inputs = np.asarray(a)
targets = np.asarray(t)


def train(i=1, timed = False):
    if timed == True:
        import time
        beg_time = time.time()
    for i in range(int(i*10000)):
        nn.train(inputs, targets)
    res()
    if timed == True:
        end_time = time.time()
        total_time = end_time -beg_time
        print('total time:',total_time)
        print('time per training iteration:',total_time/(i*10000))
        


def res():
    print('1,0',nn.predict((1,0)))
    print('0,1',nn.predict((0,1)))
    print('1,1',nn.predict((1,1)))
    print('0,0',nn.predict((0,0)))
#train(1)
nn.info()

# outputs.print()
# targets.print()
# error.print()
