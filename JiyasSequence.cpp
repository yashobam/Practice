//#include <iostream>
#include <bits/stdc++.h>

using namespace std;
int multiply(int arr[],int n){
	int multi=1;
	for(int i=0;i<n;i++){
		multi*=arr[i];
	}
	return multi;
}
int main() {
	int T;
	cin>>T;
	
	for(int i=1;i<=T;i++){
		int n;
		cin>>n;
		int arr[n];
		for(int j=1;j<=n;j++){
			cin>>arr[j-1];
		}

		int dig=multiply(arr,n)%10;

		if (dig==2 || dig==3 || dig==5){
			cout<<"YES"<<"\n";
		}
		else{
			cout<<"NO"<<"\n";
		}

	}

}
