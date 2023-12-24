def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]  # choose pivot element

    leftarr = quicksort([i for i in arr if i < pivot])
    midarr = [i for i in arr if i == pivot]
    rightarr = quicksort([i for i in arr if i > pivot])

    return leftarr + midarr + rightarr


arr = [2, 3, 34, 54, 20, 8, 5, 1]
print(quicksort(arr))
