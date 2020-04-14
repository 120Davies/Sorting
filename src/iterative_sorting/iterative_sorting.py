# TO-DO: Complete the selection_sort() function below
arr = [7,3,1,8,9,11]
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest = cur_index
        for x in range(i+1, len(arr)):
            if arr[x] < arr[smallest]:
                smallest = x

        # swap
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest]
        arr[smallest] = temp

    return arr
selection_sort(arr)

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    if arr == []:
        return []
    if min(arr) < 0:
        return 'Cannot deal with negative numbers in count_sort.'
    cntArr = [0] * (max(arr)+1)

    for e in arr:
        cntArr[e] += 1

    index = 0
    for i, e in enumerate(cntArr):
        arr[index:index+e] = [i]*e
        index += e

    return arr


# STRETCH: implement the Count Sort function below
# Maybe later.
def count_sort( arr, maximum=-1 ):

    return arr
