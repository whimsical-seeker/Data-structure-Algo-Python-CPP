//Implementing selection sort with examples

#include<iostream>
using namespace std;

int main()
{
int arr[]={3,1,0,9,8,7,-5};
int temp=0;
int n=sizeof(arr) / sizeof(arr[0]);
for(int i=0;i<n;i++)
{
        cout<<arr[i]<<"\t";
}
cout<<endl;


for (int i=1;i<n;i++)
{
int j=i-1;
cout<<"i:"<<i<<endl;

         while (j>-1)
         {  cout<<"j:"<<j<<endl;
            if (arr[i]<arr[j])
                    {
                    temp=arr[i];
                    arr[i]=arr[j];
                    arr[j]=temp;
                    i=j;
                    }
         j-=1;
       
            for(int k=0;k<n;k++)
{
        cout<<arr[k]<<"\t";
}
cout<<endl;
cout.flush();
         }
      
      

}

return 0;

}