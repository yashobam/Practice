#include <bits/stdc++.h>

using namespace std;

int main(){
	int TC;
	cin>>TC;
	while(TC--){
		int N,Q,num;
		cin>>N>>Q;
		vector<int> even;
		vector<int> odd;
		while(N--){
			cin>>num;
			if (num%2==0){
				even.push_back(num);
			}
			else{
				odd.push_back(num);
			}
		sort(even.begin(),even.end());
		sort(odd.begin(),odd.end());
		}
		
	}
		
	
}