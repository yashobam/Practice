#include <bits/stdc++.h>

using namespace std;
long long int GCD(long long int x, long long int y){
	if (y==0){
		return x;
	}
	return GCD(y,x%y);
}

int main(){
	int TC;
	cin>>TC;
	while(TC--){
		long long int X,Y;
		cin>>X>>Y;
		if (GCD(X,Y)>1){
			cout<<0<<"\n";
		}
		else{
			if (GCD(X+1,Y)>1 ||GCD(X,Y+1)>1){
				cout<<1<<"\n";
			}
			else{
				cout<<2<<"\n";
			}
		}
	}
		
	
}