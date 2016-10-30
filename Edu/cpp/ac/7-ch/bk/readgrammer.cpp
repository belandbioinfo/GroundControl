#include <vector>
#include <string>
#include <iostream>
#include <map>
#include "grammer.h"
#include "readgrammer.h"
#include "split.h"

using std::vector;
using std::istream;
using std::string;

Grammer read_grammer(istream& in){
    Grammer ret;
    string line;

    while (getline(in, line)) {


        // read the input
        vector<string> entry = split(line);

        if (!entry.empty())
            // use the category to store the associated rule
            ret[entry[0]].push_back(
                    Rule(entry.begin() + 1, entry.end()));
    }
    return ret;
}
