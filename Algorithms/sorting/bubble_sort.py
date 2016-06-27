#Python implementation of bubble sort

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr


array=[1,2,3,2,1]
result=bubble_sort(array)
print result