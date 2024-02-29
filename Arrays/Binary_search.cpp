//Finding a sub pair based on the sum value
//The array is sorted in ascending order and indices are assigned to track the position from lower and higher end


#include<iostream>
#include<cmath>

using namespace std;

int binary_search(int arr[],int n,int target)
{
      //sort(arr,arr+n);
      int low=0;
      int high=n-1;
      int rounded_mid = std::ceil(static_cast<double>(low + high) / 2);
      cout<<rounded_mid<<endl;
    //  if (target<arr[rounded_mid])
     // { high=rounded_mid;}
    ///else { low=rounded_mid;}

  while ((high-low)>1)
  {
    if (target<arr[rounded_mid])
      { high=rounded_mid;}
    else if  (target>arr[rounded_mid]) { low=rounded_mid;}
    else {cout<<"Found_element: "<<rounded_mid<<"\t"<< arr[rounded_mid];
    return 0;}
    rounded_mid = std::ceil(static_cast<double>(low + high) / 2);

  }

cout<<"The element is not found";
return 0;

}


int main()
{
   int arr[]={2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97};
   int target=79;
   int n=sizeof(arr)/sizeof(arr[0]);
   cout<<"n:"<<n<<endl;
   binary_search(arr,n,target);
   return 0;
   

}