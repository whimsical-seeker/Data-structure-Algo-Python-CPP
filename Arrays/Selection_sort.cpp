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
int i=0;
while (i<n)
{

         for (int j=i+1;j<n;j++)
         {
            if (arr[j]<arr[i])
                    {
                    temp=arr[i];
                    arr[i]=arr[j];
                    arr[j]=temp;

                    }
         }
         for(int k=0;k<n;k++)
{
        cout<<arr[k]<<"\t";
}
cout<<endl;
cout.flush();
i+=1;

}

return 0;

}