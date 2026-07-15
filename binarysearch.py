import random
import time

def search(array, target):
    time.sleep(1)
    print(array)
    if len(array) <= 1:
        return array
    
    Midpoint = len(array) // 2
    Median = array[Midpoint]
    SubArray = []

    if target > Median:
        RightHalf = array[Median:] #Get the right half
        SubArray = RightHalf
    elif target < Median:
        LeftHalf = array[:Median]
        SubArray = LeftHalf
    else:
        SubArray = []
        #Implement code to check both left and right and find the indexes until the value != target so we find this range and then return that

    return search(SubArray, target)

array = []

for i in range(1,100):
    array.append(random.randint(1,200))

target = random.randint(1,200)

print(search(array,target))