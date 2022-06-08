#include<bits/stdc++.h>
using namespace std;

const int N = 200;

int n, k;
int d_min = 2147483647; //Quang duong nho nhat
int d = 0; //tong quang duong hien tai
int p = 0; //so hanh khach ten xe
int c[N][N]; //ma tran khoang cach
bool v[N]; //danh dau diem da di qua
int x[N];
int cmin = 2147483647;

int main() {
	cin >>n >>k;
	for (int i = 0; i < 2*n; i++) {
		for (int j = 0; j < 2*n; j++) {
			cin >> c[i][j];
			if (i!=j)
		}
	}
	
	return 0;
}
