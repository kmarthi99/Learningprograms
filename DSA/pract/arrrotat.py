def arrrot(nums,k):
    if nums!=[]:
        for i in range(k):
            nums.insert(0,nums.pop())
        return nums
nums=[1,3,4,6,8,9]
print(arrrot(nums,3))

