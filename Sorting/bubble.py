def bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j+1]<arr[j]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

arr=[9,5,2,4,3,1]
bubble(arr)
print(arr)