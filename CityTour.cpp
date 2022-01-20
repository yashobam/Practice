//#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int path(int n,int x,int y){
	if (n==0){
		return 1;
	}
	if ((x==0) && (y==0)){
		return path(n-1,x+1,y)+path(n-1,x-1,y)+path(n-1,x,y+1)+path(n-1,x,y-1);
	}
	else if ((x>0) && (y>0)){
		return path(n-1,x+1,y)+path(n-1,x,y+1);
	}
	else if((x<0) && (y>0)){
		return path(n-1,x-1,y)+path(n-1,x,y+1);
	}
	else if((x>0) && (y<0)){
		return path(n-1,x+1,y)+path(n-1,x,y-1);
	}
	else if((x<0) && (y<0)){
		return path(n-1,x-1,y)+path(n-1,x,y-1);
	}
	else if((x==0) && (y>0)){
		return path(n-1,x+1,y)+path(n-1,x-1,y)+path(n-1,x,y+1);
	}
	else if((x==0) && (y<0)){
		return path(n-1,x+1,y)+path(n-1,x-1,y)+path(n-1,x,y-1);
	}
	else if((x<0) && (y==0)){
		return path(n-1,x,y+1)+path(n-1,x,y-1)+path(n-1,x-1,y);
	}
	else if((x>0) && (y==0)){
		return path(n-1,x,y+1)+path(n-1,x,y-1)+path(n-1,x+1,y);
	} 
}

int main() {
	int T;
	cin>>T;
	
	for(int i=1;i<=T;i++){
		int n;
		cin>>n;
		int ans=path(n,0,0);
		cout<<ans<<"\n";
	}

}


/*
int path(int n,int x,int y,int dist){
	if (n==0){
		return 1;
	}
	if ((abs(x+1)+abs(y))>=dist){
		path(n-1,x+1,y,dist+1);
	}
	else if ((abs(x-1)+abs(y))>=dist)
		path(n-1,x-1,y,dist+1);

	else if ((abs(x)+abs(y+1))>=dist){
		path(n-1,x,y+1,dist+1);
	}
	else if ((abs(x)+abs(y-1))>=dist){
		path(n-1,x,y-1,dist+1);
	}
	
}*/