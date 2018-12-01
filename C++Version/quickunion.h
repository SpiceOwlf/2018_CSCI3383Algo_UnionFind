#ifndef QUICKUNION_H
#define QUICKUNION_H

#include <vector>

using namespace std;

int findroot_QU(vector<int> vec, int x);

int connected_QU(vector<int> vec, int x, int y);

void union_QU(vector<int> &vec, int x, int y);

#endif
