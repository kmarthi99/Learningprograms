def oddocc(A):
    if A!=[]:
        hashh={}
        for i in A:
            hashh[i]=(hashh.get(i,0))+1

        for i in hashh:
            if hashh[i]%2 == 1:
                return i

A=[9,3,9,3,9,3,9]
print(oddocc(A))