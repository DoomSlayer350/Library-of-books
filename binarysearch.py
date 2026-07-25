#import random
from book import Book

def CheckForCutoffIndex(array, target, Midpoint):

    LeftCutoffPoint = RightCutoffPoint = 0

    for index in range(Midpoint, len(array), 1): #check right
        if index == len(array) - 1 and (array[index]).PlaceInAlphabet == target:
            RightCutoffPoint = index
            break
        if (array[index]).PlaceInAlphabet != target or index == len(array) - 1:
            RightCutoffPoint = index - 1
            break

    for index in range(Midpoint, -1, -1): #check left
        if index == 0 and (array[index]).PlaceInAlphabet == target:
            LeftCutoffPoint = index
            break
        if (array[index]).PlaceInAlphabet != target:
            LeftCutoffPoint = index + 1
            break
    return RightCutoffPoint, LeftCutoffPoint

def SmallestArraySearch(array, target): #For when it reaches an array where len(array) = 1 or 2
    if len(array) == 1:
        return 0
    if len(array) == 2:
        if array[0].PlaceInAlphabet == target:
            return 0
        if array[1].PlaceInAlphabet == target:
            return 1

def search(array, target, CurrentIndex=0):

    if type(array) is dict:
        array = list(array.values())

    if len(array) <= 1:
        return array
    
    Midpoint = len(array) // 2
    Median = array[Midpoint]
    SubArray = []

    if CurrentIndex == 0: #The current index in the original array
        CurrentIndex = Midpoint

    if target > Median.PlaceInAlphabet:
        RightHalf = array[Midpoint:] #Get the right half
        SubArray = RightHalf
        CurrentIndex = CurrentIndex + len(SubArray) // 2
    elif target < Median.PlaceInAlphabet:
        LeftHalf = array[:Midpoint]
        SubArray = LeftHalf
        CurrentIndex = CurrentIndex - (len(SubArray) - len(SubArray) // 2)
    else:
        if Midpoint == 1 or Midpoint == 0:
            IndexFound = SmallestArraySearch(array, target)
            return [array[IndexFound]], CurrentIndex
        RightCutoffPoint, LeftCutoffPoint = CheckForCutoffIndex(array, target, Midpoint)
        CurrentIndexOffsetFromStart = Midpoint - LeftCutoffPoint
        CurrentIndex = CurrentIndex - CurrentIndexOffsetFromStart
        SubArray = array[LeftCutoffPoint:(RightCutoffPoint + 1)]
        return SubArray, CurrentIndex
    return search(SubArray, target, CurrentIndex)

#array = []
"""
for i in range(1,100):
    array.append(random.randint(1,200))
"""
#array = [1,2,5,6,7,8,9,10,11,11,11,11,11,44,44,44,44,44,44,44,44,44,100,102,103,400]
#target = 44

#print(search(array,target))