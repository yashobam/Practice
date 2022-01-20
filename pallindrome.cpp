#include <iostream>
using namespace std;

int main() {
	string word;
	cin>>word;
	int length=word.size();
	//cout<<length;
	string Reverse;
	for (int i=length-1;i>=0;i--){
		Reverse.push_back(word[i]);
	}
	cout<<word<<" "<<Reverse<<"\n";
	if(word==Reverse)
		cout<<"It is a Pallindrome";
	else
		cout<<"It is not a Pallindrome";

}