def mergeSort(list):
    if len(list) <= 1:
        return list
# Find the middle point and devide it
    middle = len(list) // 2
    left_list = list[:middle]
    right_list = list[middle:]

    left_list = mergeSort(left_list)
    right_list = mergeSort(right_list)
    return merge(left_list, right_list)

# Merge the sorted halves
def merge(left_half,right_half):

    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res

