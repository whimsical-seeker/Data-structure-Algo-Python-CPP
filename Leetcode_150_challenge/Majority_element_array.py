#Given an array nums of size n, return the majority element.

#The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict_t=Counter(nums)
        n=len(nums)
        mid=(n/2).__ceil__()
        print("mid:",mid)
        
        dict_t={k:v for k,v in dict_t.items()  if v>=mid}
      #  print(dict_t)
        #key_value = int(dict_t.keys().pop()) #print(dict_t.keys())
        for k,v in enumerate(dict_t):
       #     print(k)
            return(v)
        #return  dict_t.keys()
                

         