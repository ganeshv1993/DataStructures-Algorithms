def binary_search(arr, l, h, ele):
    length=len(arr[l:h])
    print arr[l:h]
    mid=l+((h-l)/2)
    print mid, arr[mid]
    if arr[mid]==ele:
        return mid
    elif length==1:
        return None
    elif ele<arr[mid]:
        return binary_search(arr, l, mid, ele)
    else:
        return binary_search(arr, mid, h, ele)

arr=[1,2,3,4,5,6,7,8]
pos = binary_search(arr, 0, len(arr), 4)
if pos==None:
    print "Not found"
else:
    print "Found at pos", pos