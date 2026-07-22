#import random
from book import Book

def CheckForCutoffIndex(array, target, Midpoint):

    LeftCutoffPoint = RightCutoffPoint = 0

    for index in range(Midpoint, len(array)): #check right
        print("Right:",index)
        print(len(array) - 1)
        if (array[index]).PlaceInAlphabet != target or index == len(array) - 1:
            print("Right found")
            RightCutoffPoint = index - 1
            break

    for index in range(Midpoint, -1, -1): #check left
        print("Left:",index)
        if (array[index]).PlaceInAlphabet != target or index == 0:
            print("Left Found")
            LeftCutoffPoint = index + 1
            break
    print(RightCutoffPoint, LeftCutoffPoint)
    return RightCutoffPoint, LeftCutoffPoint

def search(array, target):

    if type(array) is dict:
        array = list(array.values())

    if len(array) <= 1:
        return array
    
    Midpoint = len(array) // 2
    Median = array[Midpoint]
    SubArray = []

    if target > Median.PlaceInAlphabet:
        RightHalf = array[Midpoint:] #Get the right half
        SubArray = RightHalf
    elif target < Median.PlaceInAlphabet:
        LeftHalf = array[:Midpoint]
        SubArray = LeftHalf
    else:
        RightCutoffPoint, LeftCutoffPoint = CheckForCutoffIndex(array, target, Midpoint)
        print(RightCutoffPoint, LeftCutoffPoint)
        for SingleResult in array:
            print(SingleResult.title)
        SubArray = array[LeftCutoffPoint:(RightCutoffPoint + 1)]
        print(SubArray)
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