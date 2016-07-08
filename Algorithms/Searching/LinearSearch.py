#Conventional
def linear_search_1(arr, ele):
    flag=False
    for i in range (0, len(arr)):
        if arr[i]==ele:
            flag=True
            print "Found in pos", i
    if not flag:
        print "Not found"

#The cool python way
def linear_search_2(arr, ele):
    if ele in arr:
        print "Found in pos", arr.index(ele)
    else:
        print "Not found"

arr=[1,2,3,4,5,6]
linear_search_1(arr, 4)
linear_search_2(arr, 4)
linear_search_1(arr, 8)
linear_search_2(arr, 8)




