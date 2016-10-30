#include <iostream>
#include <vector>
#include <sstream>
#include <iomanip>
#include "sequentialsquares.h"


using std::cout;
using std::cin;
using std::endl;
using std::vector;
using std::stringstream;
using std::setw;

int main(){

    cout << "Please enter the bound for the largest square: " << endl;
    int bound;
    cin >> bound;

    vector<double> squares = computeSequentialSquares(bound);

    // compute column1 width
    stringstream ss;
    ss << bound;
    int c1width = ss.str().size();

    // compute column2 width
    int lastsquare = squares.back();
    ss.str("");
    ss << lastsquare;
    int c2width = ss.str().size();

    // var to hold largest known column2
    

    // begin building output
    for (vector<double>::size_type i = 0; 
            i != squares.size(); i++) {
        cout << "| " << setw(c1width) << i ; 
        cout << "| " << setw(c2width) << squares.at(i) << "|" << endl;
        
    }

    return 0;

}
