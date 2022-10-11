def binsea(nums,k):
    r=len(nums)-1
    l=0
    while l<=r:
        #print(l,r)
        mid = (l + r) // 2
        #print(mid)
        if k==nums[mid]:
            return mid
        elif k<nums[mid]:
            r=mid-1
        else:
            l=mid+1

nums=[1,5,7,9,23,45,78,89,100,109]
print(binsea(nums,7))