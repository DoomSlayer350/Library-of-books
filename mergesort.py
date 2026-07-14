def merge(LeftHalf, RightHalf):

    LeftIndex = RightIndex = 0
    Result = []

    if len(LeftHalf) <= 1 and len(RightHalf) <= 1: #if they are lists with 1 element
        if LeftHalf[0] <= RightHalf[0]:
            Result.extend(LeftHalf)
            Result.extend(RightHalf)
            return Result
        
        Result.extend(RightHalf)
        Result.extend(LeftHalf)
        return Result

    while LeftIndex < len(LeftHalf) and RightIndex < len(RightHalf): #We're finding at what point in the 2 lists does the left side <= right side
        if LeftHalf[LeftIndex] <= RightHalf[RightIndex]:
            LeftIndex += 1
        elif LeftHalf[LeftIndex] > RightHalf[RightIndex]:
            RightIndex += 1
    Result.extend(LeftHalf[LeftIndex:])
    Result.extend(RightHalf[:RightIndex]) # At those 2 indexes merge the 2 lists
    return Result


def MergeSort(array):

    if len(array) <= 1:
        return array
    
    Midpoint = len(array) // 2
    LeftHalf = array[:Midpoint]
    RightHalf = array[Midpoint:]

    SortedLeftHalf = MergeSort(LeftHalf)
    SortedRightHalf = MergeSort(RightHalf)
    print(SortedLeftHalf, SortedRightHalf)
    print(merge(SortedLeftHalf, SortedRightHalf))
    return merge(SortedLeftHalf, SortedRightHalf)


array = [5,6,1,2,4,3,7]

"""
testleft = [1,2,3]
testright = [3,4,5]
merge(testleft, testright)
"""
    
MergeSort(array)
