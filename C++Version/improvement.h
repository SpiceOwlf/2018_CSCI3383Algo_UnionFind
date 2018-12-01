#ifndef IMPROVEMENT_H
#define IMPROVEMENT_H

#include <vector>

using namespace std;

vector<int> generateweight_IM(int N);

void weighted_union(vector<int> &vec, vector<int> &weight, int x, int y);

void pathcompression(vector<int> &vec, vector<int> &weight, int x, int y);

#endif
