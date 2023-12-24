def selection_sort(arr):
    for i in range(len(arr)):
        print("break")
        for j in range(len(arr)-i-1):
            mini=arr[0]
            ind=0;
            if arr[j+1] < mini:
                mini=arr[j+1]
                ind=j+1
            # print(mini, end=' ')
            arr[0],arr[ind]=mini,arr[0]
            arr.indexof()
            print(arr)

arr=[9,5,2,4,1]
print(selection_sort(arr))
# print(arr)