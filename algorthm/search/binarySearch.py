def binarySearch(lys, val,steps=True):
    if steps:
        print("\nLearning mode is True, Give last parameter as False if you want to change")
        print("\n Startng Binary Search \n")
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        print("first= ",first,"last = ",last,"index = ",index)
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    return index