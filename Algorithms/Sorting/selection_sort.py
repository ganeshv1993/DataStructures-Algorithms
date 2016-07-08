def selection_sort(arr):
    for i in range(len(arr)):
        min_ind=i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[min_ind]:
                min_ind=j
        arr[i],arr[min_ind]=arr[min_ind],arr[i]
    print arr

arr=[3,2,4,5,1,2]
selection_sort(arr)