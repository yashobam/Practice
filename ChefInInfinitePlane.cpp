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
		//set <long long int> keys;
		long long int num;

		for (long long int i=0; i<N;i++){
			cin>>num;
			game[num]++;
			//keys.insert(num);
		}
		long long int su=0;

		for(auto i=game.begin();i!=game.end();i++){
			long long int key,val;
			key=i->first;
			val=i->second;
			if (val<key-1){
				su+=val;
			}
			
			else{
				su+=key-1;
			}
		}
		cout<<su<<"\n";
	}
}