"""Random data set generator."""
import random
import math

dimension = 1
sampleSize = 12
with open('data.txt', 'w') as data:
    for y in range(sampleSize):
        for x in range(dimension):
            value = math.floor(((random.random() * 100) % 13) - 2) 
            data.write("{} ".format(value))
        data.write("{}\n".format(value * value + 10))
