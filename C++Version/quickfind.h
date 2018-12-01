#ifndef QUICKFIND_H
#define QUICKFIND_H

#include <vector>

using namespace std;

vector<int> generate_QF(int N);

int connected_QF(vector<int> vec, int x, int y);

void union_QF(vector<int> &vec, int x, int y);

#endif
