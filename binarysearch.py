#import random

def CheckForCutoffIndex(array, target, Midpoint):
    #check right
    LeftCutoffPoint = RightCutoffPoint = 0
    for index in range(Midpoint, len(array) - 1):

        if array[index] != target:
            RightCutoffPoint = index - 1
            break

    #check left

    for index in range(Midpoint, 0, -1):

        if array[index] != target:
            LeftCutoffPoint = index + 1
            break
    
    return RightCutoffPoint, LeftCutoffPoint

def search(array, target):
    print(array)
    if len(array) <= 1:
        return array
    
    Midpoint = len(array) // 2
    Median = array[Midpoint]
    SubArray = []

    if target > Median:
        RightHalf = array[Midpoint:] #Get the right half
        SubArray = RightHalf
    elif target < Median:
        LeftHalf = array[:Midpoint]
        SubArray = LeftHalf
    else:
        RightCutoffPoint, LeftCutoffPoint = CheckForCutoffIndex(array, target, Midpoint)
        SubArray = array[LeftCutoffPoint:(RightCutoffPoint + 1)]
        return SubArray
    return search(SubArray, target)

#array = []
"""
for i in range(1,100):
    array.append(random.randint(1,200))
"""
#array = [1,2,5,6,7,8,9,10,11,11,11,11,11,44,44,44,44,44,44,44,44,44,100,102,103,400]
#target = 44

#print(search(array,target))