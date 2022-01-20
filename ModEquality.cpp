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
		set <long long int> keys;
		long long int num,mi,count;
		mi=2e9;
		count=0;
		for (long long int i=0; i<N;i++){
			cin>>num;
			game[num]++;
			keys.insert(num);
			mi=min(mi,num);
			count++;
		}
		long long int sum=0;
		if (keys.upper_bound(mi)!=keys.end()){
			if (*keys.upper_bound(mi)<=mi*2){
				sum=count;
			}
			else{
				sum=count-game[mi];
			}
		}
		else{
			sum=0;
		}
		cout<<sum<<"\n";
	}
}