//#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(){
	int TC;
	cin>>TC;
	while(TC--){
		int A,B,C;
		cin>>A>>B>>C;
		if (A+B+C==1 || A+B+C==2){
			cout<<1<<"\n";
		}
		else{
			cout<<0<<"\n";
		}
	}
		
	
}