def insertion_sort(arr):
   for i in range(1,len(arr)):
       temp=arr[i]
       j=i
       while(j>0 and arr[j-1]>temp):
           arr[j]=arr[j-1]
           j-=1
       arr[j]=temp
   print arr
arr=[2,3,4,2,5,1,3,7]
insertion_sort(arr)