#Bubblesort
def bubsort(arr):
    n=len(arr)
    while n>1:
        print(n)
        for i in range(n-1):
            if arr[i]>arr[i+1]:
                #swap
                arr[i],arr[i+1]=arr[i+1],arr[i]
                print("swappedelements",arr[i],arr[i+1])
        n-=1
        print(arr)


arr=[5,100,99,56,78,6,75,12,90,4,3]
bubsort(arr)
print("finalarray",arr)