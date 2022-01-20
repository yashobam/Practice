//#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
	string str;
	getline(cin,str);
	string word;
	for(int i=0;i<str.size();i++){
		if (str[i] == ' '){
			cout<<word<<"\n";
			word="";
			continue;
		}
		else if(i==str.size()-1){
			str[i]=str[i]-32;
			word.push_back(str[i]);
			cout<<word<<"\n";
			break;
		}

		str[i]=str[i]-32;
		word.push_back(str[i]);
		 
	}

}