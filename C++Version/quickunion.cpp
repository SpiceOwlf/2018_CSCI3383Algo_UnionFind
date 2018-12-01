#include <vector>

using namespace std;

int findroot_QU(vector<int> vec, int x){
	int ans = x;
	while (ans != vec[ans])
		ans = vec[ans];
	return ans;
}

int connected_QU(vector<int> vec, int x, int y){
	return (findroot_QU(vec, x) == findroot_QU(vec, y));
}

void union_QU(vector<int> &vec, int x, int y){
	int root_x = findroot_QU(vec, x);
	int root_y = findroot_QU(vec, y);
	vec[root_x] = root_y;
}
