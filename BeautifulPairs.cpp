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
		map <long long int,long long int> game;
		long long int num;
		long long int n=0;
		for (long long int i=0; i<N;i++){
			cin>>num;
			game[num]++;
			n++;
		}
		long long int sum=0;
		for(auto i=game.begin();i!=game.end();i++){
			long long int key,val;
			key=i->first;
			val=i->second;
			sum+=val*(n-val);
		}
		cout<<sum<<"\n";
	}
}