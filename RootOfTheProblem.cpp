#include <bits/stdc++.h>
//#include <iostream>

using namespace std;

int main(){
	int TC;
	cin>>TC;
	while(TC--){
		int N;
		cin>>N
		map <int,int> parents;
		vector <int> children;
		int id,childsum;
		while(N--){
			cin>>id>>childsum;
			if (childsum==0){
				children.push_back(id);
			}
			else{
				parents[id].push_back(childsum);
			}
		}



	}
		
	
}