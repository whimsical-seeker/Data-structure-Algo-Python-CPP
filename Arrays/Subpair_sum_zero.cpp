//Traverse the array and maintain the sum of elements seen so far. If the sum is seen before 
//Python dictionary could be implemented using hashing

#include<iostream>
#include<unordered_set>
using namespace std;

bool zeros_sub_array(int arr[],int n)
{
      unordered_set<int> set; // A set is created to track the sum of sub arrays so far
      set.insert(0);
      int sum=0;
      for (int i=0;i<n;i++)

      {
            sum+=arr[i];    


                if (set.find(sum)!=set.end())
                {

                        return true;
                }

        
            set.insert(sum);

      }
     

      //cout<<"Pair not found";
   return false;

}


int main()
{
  int arr[]={3,4,-7,0,9,1,-1};
  int n=sizeof(arr);

 zeros_sub_array(arr,n)? cout<<"sub_array_zero_sum_exists":cout<<"sub_array_zero_sum_does_not_exist"; 

}

