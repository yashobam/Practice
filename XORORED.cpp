#include <bits/stdc++.h>

using namespace std;

int main(){
	int TC;
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	cin>>TC;
	while(TC--){
		long long int N;
		cin>>N;
		long long int num,bin=0,binnot=0;

		for (long long int i=0; i<N;i++){
			cin>>num;
			bin=bin|num;
			binnot=binnot|(~num);
		}
		cout<<bin<<" "<<(bin&binnot)<<"\n";
	}
}