//Question link==https://practice.geeksforgeeks.org/problems/find-missing-and-repeating2512/

// { Driver Code Starts
#include <bits/stdc++.h>

using namespace std;

 // } Driver Code Ends
class Solution{
public:
    int *findTwoElement(int *a, int n)
    {
        int x = 0;
        
        for(int i = 0 ; i < n ; i++)
        x ^= a[i];
        
        for(int i = 1 ; i <= n ; i++)
        x ^= i;
        
        int st = (x & -x);
        
        int x1 = 0 , x2 = 0;
        
        for(int i = 0 ; i < n ; i++)
        {
            if((st & a[i]))  x1 ^= a[i];
            
            else  x2 ^= a[i];
        }
        
        for(int i = 1 ; i <= n ; i++)
        {
            if((st & i))  x1 ^= i;
            
            else  x2 ^= i;
        }
        
        for(int i = 0 ; i < n ; i++)
        if(x2 == a[i])
        {
            swap(x1 , x2);
            
            break;
        }
        
        int* ans = new int[2];  ans[0] = x1 , ans[1] = x2;
        
        return ans;
    }
};

// { Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        int a[n];
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        Solution ob;
        auto ans = ob.findTwoElement(a, n);
        cout << ans[0] << " " << ans[1] << "\n";
    }
    return 0;
}  // } Driver Code Ends
