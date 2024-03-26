
#The cumulative sum of an array at index i is defined as the sum of all elements of the array from index 0 to index i.
#The positive cumulative sum of an array is a list of only those cumulative sums which are positive.
class Solution:
	def getPositiveCumulativeSum(self, arr: List[int]) -> List[int]:
		# add your logic here
		# sum variable to keep track of all the elements
		n=len(arr)
		if n==1:
                  return [x for x in arr if x>0]
		sum1=[0]*n
		sum1[0]=arr[0]
		
		
		for i in range(1,n):
			sum1[i]=sum1[i-1]+arr[i]
		
		return [x for x in sum1 if x>0]
			
		
