#include <vector>
#include "quickunion.h"

using namespace std;

vector<int> generateweight_IM(int N){
	vector<int> ans;
	for(int i = 0; i < N; i++)
		ans.push_back(1);
	return ans;
}

void weighted_union(vector<int> &vec, vector<int> &weight, int x, int y){
	int root_x = findroot_QU(vec, x);
	int root_y = findroot_QU(vec, y);
	if(weight[root_x] < weight[root_y]){
		vec[root_x] = root_y;
		weight[root_y] += weight[root_x];
	}
	else{
		vec[root_y] = root_x;
		weight[root_x] += weight[root_y];
	}
}

void pathcompression(vector<int> &vec, vector<int> &weight, int x, int y){
	int root_x = x;
	while(root_x != vec[root_x]){
		vec[root_x] = vec[vec[root_x]];
		root_x = vec[root_x];
	}
	int root_y = y;
	while(root_y != vec[root_y]){
		vec[root_y] = vec[vec[root_y]];
		root_y = vec[root_y];
	}
	if(root_x != root_y){
		if(weight[root_x] < weight[root_y]){
			vec[root_x] = root_y;
			weight[root_y] += weight[root_x];
		}
		else{
			vec[root_y] = root_x;
			weight[root_x] += weight[root_y];
		}
	}
}
