def binarySearch(arr, toFind):
    i ,j=0, len(arr)-1

    while i<=j:

        mid = (i+j)//2

        if arr[mid] == toFind:
            return "Yes"
        elif arr[mid] < toFind:
            i=mid+1
        else:
            j=mid-1

    return "No"


arr = [1,2,3,4,5,6,7,8,9]
toFind = 10
print(binarySearch(arr, toFind))