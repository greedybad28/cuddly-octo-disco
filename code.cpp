#include <iostream>
using namespace std;
int factorial(int n)
{
    int i,fact=1;
    for(i=1;i<=n;i++)
    {
        fact=fact*i;
    }
    return fact;
}   
int main()
{
    int n,r,nCr;
        cout<<"Enter the value of n and r for finding nCr";
        cin>>n>>r;
        if(n>=r && r>=0)
        {
            nCr = factorial(n)/(factorial(r)*factorial(n-r));
        }
        cout<<"nCr="<<nCr;
        return 0;
}

