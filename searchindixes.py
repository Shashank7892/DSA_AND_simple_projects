def targets(nums,target):
    l=[]
    nums.sort()
    print(nums)
    lo,hi=0,len(nums)-1
    while lo<=hi:
        mid=(lo+hi)//2
        guess=nums[mid]
        if nums[mid]==target:
            if mid-1>=0 and nums[mid-1]==target:
                l.append(mid)
                hi=mid-1
            else:
                l.append(mid)    
                return l
        elif nums[mid]>target:
                hi=mid-1
        else:
                lo=mid+1
    

nums=[1,2,5,2,3]
target=2
print(targets(nums,target))