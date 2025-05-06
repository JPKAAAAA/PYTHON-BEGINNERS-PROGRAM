import random

def randomArrayGenerator():
    arr=[]
    for i in range(10):
        arr.append(random.randint(0, 99)+1)
    return arr