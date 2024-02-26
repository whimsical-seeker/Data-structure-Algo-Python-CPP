//Finding a sub pair based on the sum value
//The array is sorted in ascending order and indices are assigned to track the position from lower and higher end


#include<iostream>
#include<algorithm>
using namespace std;

void find_pair(int arr[],int n,int target)
{
      sort(arr,arr+n);
      int low=0;
      int high=n-1;

      while (low<high)
      
      {
                if (arr[low]+arr[high]==target)
               {
                cout<<"Pairs found ("<<arr[low]<<","<<arr[high]<<")";
                return;
               }

      (arr[low]+arr[high]<target)? low++:high--;
      
      
      }

      cout<<"Pair not found";


}


int main()
{
   int arr[]={2,1,4,3,7,8,0};
   int target=5;
   int n=sizeof(arr);
   cout<<"n:"<<n;
   find_pair(arr,n,target);
   return 0;
   

}