#include "wordbank.h"
#include <iostream>
#include <vector>
#include <string>


using std::cin;
using std::cout;
using std::vector;
using std::istream;
using std::string;

int main(){
    vector<string> words;
    vector<string>::size_type numwords = 0;

    read(cin, words);
        
    numwords = words.size();

    cout << numwords << std::endl;
    
}
