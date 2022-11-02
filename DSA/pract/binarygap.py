def binarygap(N):
    binary_gap=max_gap=0
    binary_flag=False
    while N!=0:
        binary=N%2
        print("b",binary)
        if binary==1:
            if binary_flag == False:
                binary_flag = True  #flag enabled
            print("flag reset")
            print(max_gap,binary_gap)
            if max_gap < binary_gap:
                max_gap=binary_gap
            binary_gap=0

        else:
            if binary_flag:
                binary_gap+=1
        N=N//2
        print(N)
    return  max_gap

print(binarygap(1041))

