//Finding a sub pair based on the sum value
//An unordered map is used with array values as the index/key and the array index is assigned to map as the value
//Python dictionary could be implemented using hashing

#include<iostream>
#include<unordered_map>
using namespace std;

void find_pair(int arr[],int n,int target)
{
      unordered_map<int,int> map;
      for (int i=0;i<n;i++)

      {
                if (map.find(target-arr[i])!=map.end())
                {
                        cout<<"Pair found ("<<arr[map[target-arr[i]]]<<","<<arr[i]<<")";
                        return;
                }

            map[arr[i]]=i;

      }
     

      cout<<"Pair not found";


}


int main()
{
   int arr[]={2,1,4,3,7,8,0};
   int target=7;
   int n=sizeof(arr);
   cout<<"n:"<<n;
   find_pair(arr,n,target);
   return 0;
   

}