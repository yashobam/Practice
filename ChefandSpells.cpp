#include <bits/stdc++.h>

using namespace std;

int main(){
	int TC;
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin>>TC;
	while(TC--){
		long long int x,y,z;
		cin>>x>>y>>z;
		cout<<x+y+z-(min(min(x,y),z))<<"\n";
	}
		
	
}