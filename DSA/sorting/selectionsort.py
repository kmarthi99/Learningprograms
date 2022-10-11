def selsor(arr):
    for i in range(len(arr)-1):
        print("iii",i+1)
        index=i
        for j in range(i+1,len(arr)):
            #print("k",arr[j], sel)
            if arr[index]>arr[j]:
                index=j

        arr[i],arr[index]=arr[index],arr[i]
        print("selection",arr[index])




arr=[999, -97, -9, -2, 0, 11, 45, 88, 747]
selsor(arr)
print("finalarray",arr)