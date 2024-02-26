
#Deals with the extracting sub arrays where sum is zero and  values are continuous

def insert_values(d,k,v):
    d.setdefault(k,[]).append(v)


def print_sublist(arr,n):

    d={}
    insert_values(d,0,-1)
    total=0
    for i in range(0,n):
        print("d:",d)
        total+=arr[i]

        if total in d:
            lt_indices=d.get(total)

            for j in lt_indices:
                 print("Sublist indices are",(j+1,i))
        insert_values(d,total,i)
    return 0


if __name__=='__main__':

    arr=[10,3,-4,5,2,3,-2,9,-6]

    n=len(arr)

    print_sublist(arr,n)
