class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:       
    
                    #nums=[0,2,3,4,6,8,9]# [0,1,2,4,5,7] #
                    n=len(nums)
                    if n<1:
                        return nums
                    pres_ind=0
                    last_ind=-1
                    l1=[]
                    i=1
                    while i<n: #for i in range(1,n):
                        #print(nums[i])
                        if nums[i]-nums[i-1]==1:
                          #  print("here")
                            last_ind=i
                        
                        
                        else:
                               # print("l1")
                                if last_ind==-1:
                                        l1.append(str(nums[pres_ind]))
                                else:
                                    l1.append(str(nums[pres_ind])+"->"+str(nums[last_ind]))
                                
                                pres_ind=i
                                last_ind=-1
                        i+=1
                    if pres_ind!=-1:
                            if last_ind==-1:
                                        l1.append(str(nums[pres_ind]))
                            else:
                                    l1.append(str(nums[pres_ind])+"->"+str(nums[last_ind]))
                    return l1
