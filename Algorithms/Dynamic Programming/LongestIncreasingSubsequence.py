def LIS(seq):
    l=len(seq)
    arr=[1]*l
    for i in xrange(1,l):
        if seq[i]>seq[i-1]:
            arr[i]=arr[i-1]+1
    m=max(arr)
    ind=arr.index(m)
    return(m, ind)

seq=[1,3,4,2,5,6,7,4]
#arr=[1,2,3,1,2,3,4,1]
lis_len,ind =LIS(seq)
print lis_len, seq[ind-3:ind+1]