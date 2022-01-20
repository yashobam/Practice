//#include <bits/stdc++.h>
#include <iostream>

using namespace std;

long long int term[100000000];

long long int allbot(long long int num){
	if (num>=(num/2+num/3+num/4)){
		return num;
	}
	if(num>100000000){
		return allbot(num/2)+allbot(num/3)+allbot(num/4);
	}
	else if (term[num]!=0){
		return term[num];
	}
	else{
		term[num]=allbot(num/2)+allbot(num/3)+allbot(num/4);
		return term[num];
	}
	//return max(num,(num/2+num/3+num/4));

}

int main(){
	long long int num;
	while(cin>>num){
		cout<<allbot(num)<<"\n";
	}
}
