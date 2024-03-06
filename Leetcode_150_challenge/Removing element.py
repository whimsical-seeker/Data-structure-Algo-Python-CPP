
""""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
       #Handling edge cases

        e=len(nums)-1
        s=0

        if not nums or (len(nums)==1 and nums[0]==val):
            return 0

        if (len(nums)==1 and nums[0]!=val):
            return 1
        while s!=e and e>0 and s<e:
                #print("n",nums)
                #print("s",s)
                #print("e",e)
                if nums[s]==val:
                    if nums[e]==val:
                        e-=1
                    else:
                        temp=nums[s]
                        nums[s]=nums[e]
                        nums[e]=temp
                      #  print("n_mod",nums)
                        s+=1
                        e-=1
                    
                else:
                    s+=1

        try:
            return nums.index(val)  # Try to find the index of val in nums
        except ValueError:
            return len(nums)  #