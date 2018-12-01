#include <iostream>
#include <vector>
#include <fstream>
#include <cstring>
#include <sstream>
#include <ctime>
#include <cstdlib>
#include "quickfind.h"
#include "quickunion.h"
#include "improvement.h"

using namespace std;


int main(){
	ofstream outputfile;
	outputfile.open("result.txt");
	string s1 = "500_10000_", s2 = "5000_100000_";
	string inputfilename1, inputfilename2;
	for(int i = 0; i < 5; i++){
		int size, x, y;
		clock_t cl;
		vector<int> vec;
		vector<int> weight;
		vector<int> choice_x;
		vector<int> choice_y;
		ostringstream temp;
		temp << i;
		inputfilename1 = s1 + temp.str() + ".txt";
		inputfilename2 = s2 + temp.str() + ".txt";
		ifstream in1;
		in1.open(inputfilename1.c_str());
		in1 >> size;
		vec = generate_QF(size);
		while(in1 >> x >> y){
			choice_x.push_back(x);
			choice_y.push_back(y);
		}
		/////////////Quick Find///////////////////////////////////////////
		cl = clock();
		for(int j = 0; j < choice_x.size(); j++)
			union_QF(vec, choice_x[j], choice_y[j]);
		cl = clock() - cl;
		outputfile <<"Quick Find Time for " + inputfilename1 + ":"<<cl/(double)CLOCKS_PER_SEC<<"\n";
		/////////////Quick Union////////////////////////////////
		vec = generate_QF(size);
		cl = clock();
		for(int j = 0; j < choice_x.size(); j++)
			union_QU(vec, choice_x[j], choice_y[j]);
		cl = clock() - cl;
		outputfile <<"Quick Union Time for " + inputfilename1 + ":"<<cl/(double)CLOCKS_PER_SEC<<"\n";
		/////////////Weighted Union/////////////////////////////////////
		vec = generate_QF(size);
		weight = generateweight_IM(size);
		cl = clock();
		for(int j = 0; j < choice_x.size(); j++)
			weighted_union(vec, weight, choice_x[j], choice_y[j]);
		cl = clock() - cl;
		outputfile <<"Weighted Union Time for " + inputfilename1 + ":"<<cl/(double)CLOCKS_PER_SEC<<"\n";
		////////////Path Compression///////////////////////////////////
		vec = generate_QF(size);
		weight = generateweight_IM(size);
		cl = clock();
		for(int j = 0; j < choice_x.size(); j++)
			pathcompression(vec, weight, choice_x[j], choice_y[j]);
		cl = clock() - cl;
		outputfile <<"Path Compression Time for " + inputfilename1 + ":"<<cl/(double)CLOCKS_PER_SEC<<"\n";
		in1.close();
		
		ifstream in2;
		in2.open(inputfilename2.c_str());
		in2 >> size;
		vector<int> choice_x1;
		vector<int> choice_y1;
		vec = generate_QF(size);
		while(in2 >> x >> y){
			choice_x1.push_back(x);
			choice_y1.push_back(y);
		}
		/////////////Quick Find///////////////////////////////////////////
		cl = clock();
		for(int j = 0; j < choice_x1.size(); j++)
			union_QF(vec, choice_x1[j], choice_y1[j]);
		cl = clock() - cl;
		outputfile <<"Quick Find Time for " + inputfilename2 + ":"<<cl/(double)CLOCKS_PER_SEC<<"\n";
		/////////////Quick Union////////////////////////////////
		vec = generate_QF(size);
		cl = clock();
		for(int j = 0; j < choice_x1.size(); j++)
			union_QU(vec, choice_x1[j], choice_y1[j]);
		cl = clock() - cl;
		outputfile <<"Quick Union Time for " + inputfilename2 + ":"<<cl/(double)CLOCKS_PER_SEC<<"\n";
		/////////////Weighted Union/////////////////////////////////////
		vec = generate_QF(size);
		weight = generateweight_IM(size);
		cl = clock();
		for(int j = 0; j < choice_x1.size(); j++)
			weighted_union(vec, weight, choice_x1[j], choice_y1[j]);
		cl = clock() - cl;
		outputfile <<"Weighted Union Time for " + inputfilename2 + ":"<<cl/(double)CLOCKS_PER_SEC<<"\n";
		////////////Path Compression///////////////////////////////////
		vec = generate_QF(size);
		weight = generateweight_IM(size);
		cl = clock();
		for(int j = 0; j < choice_x1.size(); j++)
			pathcompression(vec, weight, choice_x1[j], choice_y1[j]);
		cl = clock() - cl;
		outputfile <<"Path Compression Time for " + inputfilename2 + ":"<<cl/(double)CLOCKS_PER_SEC<<"\n";
		in2.close();
		cout<<CLOCKS_PER_SEC<<"\n";
	}
	outputfile.close();
	return 0;
}
