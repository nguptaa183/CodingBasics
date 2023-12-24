def mergesort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    leftarr = mergesort(arr[:mid])
    rightarr = mergesort(arr[mid:])
    mergedarr = merge(leftarr, rightarr)
    return mergedarr


def merge(leftarr, rightarr):
    i, j = 0, 0
    merged = []
    while i < len(leftarr) and j < len(rightarr):
        if leftarr[i] <= rightarr[j]:
            merged.append(leftarr[i])
            i += 1
        else:
            merged.append(rightarr[j])
            j += 1

    merged.extend(leftarr[i:])
    merged.extend(rightarr[j:])
    return merged


arr = [2, 3, 34, 54, 20, 8, 5, 1]
print(mergesort(arr))
