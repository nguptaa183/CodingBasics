def insertionSort(arr):
    first = arr[0]
    for i in range(len(arr)-1):
        while arr[i+1] < first:
            arr[i+1], arr[i] = arr[i], arr[i+1]
            first = arr[i+1]
    return arr

arr = [3, 2, 34, 54, 20, 8, 5, 1]
print(insertionSort(arr))