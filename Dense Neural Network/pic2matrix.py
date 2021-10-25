import numpy as np
from random import randint

#this version also randomizes the order of the training examples
import os
from PIL import Image

inputs=((1,1),(0,0),(1,0),(0,1))
outputs=((0,),(0,),(1,),(1,))

rand_list = list()

#random examples with duplications
for i in range(100):
    q = randint(0,3)
    rand_list.append(q)

#every example only one time
for i in range(lenght_of_examples):
    q = randint(0,lenght_of_examples)
    if q not in rand_list: rand_list.append(q)

    
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


# reform a numpy array of the original shape
arr2 = np.asarray(vector).reshape(shape)

# make a PIL image
img2 = Image.fromarray(arr2, 'RGBA')
img2.show()
