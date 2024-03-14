import copy
class Solution:
    def isHappy(self, n: int) -> bool:

            if n>1 and n<4:
                return False
            temp=sum([pow(int(x),2) for x in list(str(n))])
            sum_exists=set()
            sum_exists.add(temp)
            while temp!=1:
                 temp=sum([pow(int(x),2) for x in list(str(temp))])
             
                 if temp==1:
                    return True
                 if temp in sum_exists:
                       return False
                 sum_exists.add(temp)
            
            return False if temp!=1 else True
            
                    
