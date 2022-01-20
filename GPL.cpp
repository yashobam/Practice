//#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
	int T;
	cin>>T;
	
	for(int i=1;i<=T;i++){
		int n;
		cin>>n;
		int num;
		cin>>num;
		int sum=0;
		
		int c=0;
		while(num!=0){
			//cout<<(num%10)<<"\n";
			sum+=(num%10)*(pow(2,c));
			num=num/10;
			c+=1;
		}
		cout<<sum<<"\n";
		

	}

}
