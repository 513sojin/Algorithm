#include <iostream>
#include <string.h>
#include <algorithm>
#include <vector>
#define MAX 25

using namespace std;

int w, h, num, cnt;
int graNum[MAX];
bool visited[MAX][MAX];
int graph[MAX][MAX];
int dw[4] = { 1,0,-1,0};
int dh[4] = { 0,1,0,-1};
vector<int> vec;

void dfs(int h, int w) {
	cnt++;
	visited[h][w] = true;
	for (int i = 0; i < 4; i++) {
		int nh = h + dh[i];
		int nw = w + dw[i];
		if (0 <= nw && 0 <= nh && nw < num && nh < num) {
			if (graph[nh][nw] && !visited[nh][nw]) {
				visited[nh][nw] = true;
				dfs(nh, nw);
			}
		}
	}
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	memset(visited, false, sizeof(visited));
	cin >> num;

	for (int i = 0; i < num; i++) {
		string temp;
		cin >> temp;
		for (int j = 0; j < num; j++) {
			graph[i][j] = temp[j] - '0';
		}
	}

	for (int i = 0; i < num; i++) {
		for (int j = 0; j < num; j++) {
			if (graph[i][j] && !visited[i][j]) {
				cnt = 0;
				dfs(i, j);
				vec.push_back(cnt);
			}
		}
	}
	cout << vec.size()<<'\n';
	sort(vec.begin(), vec.end());

	for (int i = 0; i < vec.size(); i++) {
		cout << vec[i] << '\n';
	}
	
}