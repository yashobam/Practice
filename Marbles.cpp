#include <bits/stdc++.h>
//#include <iostream>

using namespace std;

//map <tuple<long long int,long long int>,long long int> memo;
/*
long long int binfac(long long int n,long long int r){
	if (r>n){
		return 0;
	}
	if (r==0||r==n){
		return 1;
	}
	tuple<long long int,long long int> a=make_tuple(r,n);
	if (memo.find(a)!=memo.end()){
		return memo[a];
	}
	else{
		memo[a]= binfac(n-1,r-1)+binfac(n-1,r);
		return memo[a];
	}
}
*/
/*long long int nCr(long long int n,long long int r){
	return 
}*/
int main(){
	int TC;
	cin>>TC;
	while(TC--){
		int k,n;
		cin>>n>>k;
		//long long int a;
		long long int a=1;
		n--;
		k--;
		if (k>n/2){
			k=n-k;
		}

		for(int i=0;i<k;i++){
			a*=n;
			a/=i+1;
			n--;
		}
		//a=binfac(n-1,k-1);
		cout<<a<<"\n";
	}
}