#include <bits/stdc++.h>

using namespace std;
vector<long long int> arr;
long long int ma=0;
void recur(long long int p,long long int k,long long int depth){
	auto a=lower_bound(arr.begin()+p+1,arr.end(),arr[p]);

	if (k==0){
		if (a!=arr.end() && *a==arr[p]){
			recur(a-arr.begin(),k,depth+1);
		}
		else{
			ma=max(ma,depth+1);
		}
	}
	else{
		recur(p+1,k-1,depth+1);
		if (a!=arr.end() && *a==arr[p]){
			recur(a-arr.begin(),k,depth+1);
		}
	}
}
int main(){
	int TC;
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	cin>>TC;
	while(TC--){
		long long int N,K;
		cin>>N>>K;
		map <long long int,vector<long long int>> map1;
		vector<long long int> arr;
		long long int num;

		for (long long int i=0; i<N;i++){
			cin>>num;
			arr.push_back(num);
			//map1[num].push_back(i);
		}
		recur(0,K,0);
		arr.clear();
		ma=0;
	}

}
