def merge(m1,m2):
    res=[]
    m1ptr=0
    m2ptr=0
    while(m1ptr<len(m1)) and (m2ptr<len(m2)):
        if m1[m1ptr]<m2[m2ptr]:
            res.append(m1[m1ptr])
            m1ptr+=1
        else:
            res.append(m2[m2ptr])
            m2ptr+=1
    if m1ptr==len(m1) and m2ptr!=len(m2):
        res+=(m2[m2ptr:])
    elif m1ptr!=len(m1) and m2ptr==len(m2):
        res+=(m1[m1ptr:])
    return res

def merge_sort(arr):
    l=len(arr)
    if l==1:
        return arr
    m1=merge_sort(arr[0:l/2])
    m2=merge_sort(arr[l/2:])
    return merge(m1,m2)


array1=[1,2,3,2,1]
result=merge_sort(array1)
print result