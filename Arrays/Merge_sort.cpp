#include<iostream>

using namespace std;

// Merge function to merge two sorted arrays
void merge(int arr[], int l, int m, int r) {
    int temp[100]; // Storing in temporary array
    int i = l;
    int k = l; // Initialize k with l instead of 0
    int j = m + 1;

    while (i <= m && j <= r) {
        if (arr[i] < arr[j]) {
            temp[k++] = arr[i++];
        } else {
            temp[k++] = arr[j++];
        }
    }

    while (i <= m) {
        temp[k++] = arr[i++];
    }
    while (j <= r) {
        temp[k++] = arr[j++];
    }

    // Copy elements from temp back to arr
    for (int i = l; i < k; i++) {
        arr[i] = temp[i];
    }
}

// Iterative Merge Sort function to sort the array
void merge_sort(int arr[], int l, int r)
{
        if (l<r)
        {
            int m=l+(r-l)/2;

            merge_sort(arr,l,m);
            merge_sort(arr,m+1,r);
            merge(arr,l,m,r);
        }

}


int main() {
    int arr[] = { 38, 27, 43, 3, 9, 82, 10 };
    int size = sizeof(arr) / sizeof(arr[0]);
    cout << "Original array:" << endl;
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    merge_sort(arr, 0,size-1);
    cout << "Sorted array:" << endl;
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    return 0;
}