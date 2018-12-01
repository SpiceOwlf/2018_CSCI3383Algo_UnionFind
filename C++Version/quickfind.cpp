#include <vector>

using namespace std;

vector<int> generate_QF(int N){
	vector<int> ans;
	for(int i = 0; i < N; i++)
		ans.push_back(i);
	return ans;
}

int connected_QF(vector<int> vec, int x, int y){
	return (vec[x] == vec[y]);
}

void union_QF(vector<int> &vec, int x, int y){
	int x_id = vec[x];
	int y_id = vec[y];
	if(x_id != y_id){
		for(int i = 0; i < vec.size(); i++){
			if(vec[i] == x_id)
				vec[i] = y_id;
		}
	}
}
