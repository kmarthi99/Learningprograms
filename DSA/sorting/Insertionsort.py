def inssor(nums):
    for i in range(1,len(nums)):
        print("iteration",i)
        while nums[i]<nums[i-1] and i>0:
            #swap
            print ("swap",nums[i-1],nums[i])
            nums[i],nums[i-1]=nums[i-1],nums[i]
            print(i)
            print(nums)
            i-=1

nums=[5,100,99,56,78,6,75,12,90,4,3]
inssor(nums)
print(nums)
