import random

def merge(LeftHalf, RightHalf):

    LeftIndex = RightIndex = 0
    Result = []

    while LeftIndex < len(LeftHalf) and RightIndex < len(RightHalf): #We're finding at what point in the 2 lists does the left side <= right side
        if LeftHalf[LeftIndex] < RightHalf[RightIndex]:
            Result.append(LeftHalf[LeftIndex])
            LeftIndex += 1
        else:
            Result.append(RightHalf[RightIndex])
            RightIndex += 1

    Result.extend(LeftHalf[LeftIndex:])
    Result.extend(RightHalf[RightIndex:])
    return Result


def MergeSort(array):

    if len(array) <= 1:
        return array
    
    Midpoint = len(array) // 2
    LeftHalf = array[:Midpoint]
    RightHalf = array[Midpoint:]

    SortedLeftHalf = MergeSort(LeftHalf)
    SortedRightHalf = MergeSort(RightHalf)
    return merge(SortedLeftHalf, SortedRightHalf)


array = []

"""
for i in range(1,200,1):
    array.append(random.randint(1,100))
"""
    
print(MergeSort(array))
