def zeros_sub_array(arr,n):

    se=set()
    se.add(0)
    total=0
    for i in range(0,n):
            total+=arr[i]

            if total in se:
                  return True
            
            else:
                  se.add(total)
    return False




if __name__=='__main__':
  arr=[3,4,-7,0,9,1,-1]
  n=len(arr)
  result=zeros_sub_array(arr,n)
  print(result)
  
