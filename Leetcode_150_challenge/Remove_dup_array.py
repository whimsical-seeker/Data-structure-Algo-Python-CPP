class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
       
        s=1
        e=len(nums)
        if e==1:
            return 1
        c_val=nums[0]
        while s<len(nums):
              #  print("s:",s)
               # print("c_val",c_val)
               # print(nums)
                if c_val<nums[s]:
                    c_val=nums[s]
                    s+=1
                else:
                    nums.pop(s)
        if len(nums)>1 and nums[-1]==nums[-2]:
            nums.pop(-1)
              
        return len(nums)  