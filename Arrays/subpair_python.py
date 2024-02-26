#Python implementation using dictionaries.

def find_pairs(arr,target):

        map_dict={}
        n=len(arr)
        for i in range(0,n):
                if target-arr[i] in map_dict:
                        print("pair found:",arr[i],(target-arr[i]))

                        return 0
                else:
                        map_dict[arr[i]]=i
        
        print("Pair not found")

        
        return 0


if __name__=="__main__":

        arr=[2,1,4,3,7,8,0]
        target=7
        find_pairs(arr,target)
