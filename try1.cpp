#include<bits/stdc++.h>
using namespace std;

int n, k;
int q[100]; //so khach toi da tren xe k
int p[100]; // so khach tren xe k
int x[100]; // cac diem da di
int y[100];
int d = 0;
int d_min = 2147483647;
int s = 0;
bool v[100];
int c[100][100];

bool check() {
	
}

void solve() {
	a[k] = n - sum;
	for (int i=1; i<=k; i++) {
		cout << a[i] << " ";
	}
	cout <<endl;
	TRY_Y(1, 1);
}

void TRY_X(int t) {

}

bool check(int a, int i) {
	if (v[i] == true) {
		return false;
	}
	return true;
}

void TRY_Y(int a) {
	for (int i = y[a-1]+1; i<=2*n; i++) {
		if check_Y(a, i) {
			
		}
	}
}

int main() {
	cin >> n >>k;
	for (int i=1; i<=k; i++) {
		cin >> q[i];
	}
	for (int i=0; i<=2*n; i++) {
		for (int j=0; j<=2*n; j++) {
			cin >> c[i][j];
		}
	}
	TRY_X(1);
	return 0;
}
