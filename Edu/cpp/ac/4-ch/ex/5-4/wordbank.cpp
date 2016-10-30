#include "wordbank.h"
#include <vector>
#include <iostream>
#include <string>

using std::vector;
using std::istream;
using std::string;

istream& read(istream& is, vector<string>& words){
    if (is){

        string x;
        while (is >> x)
            words.push_back(x);
    }
    return is;

}
