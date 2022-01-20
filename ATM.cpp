//#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main(){
	long cash;
	double balance;
	cin >> cash >> balance;
	
	if (balance-cash>0 && cash%5==0){
		balance-=cash+0.50;
	}
	cout<<balance;
}