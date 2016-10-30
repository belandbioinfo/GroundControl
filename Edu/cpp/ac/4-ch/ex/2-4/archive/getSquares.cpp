#include <iostream>
#include <vector>
#include "boundedsquares.h"

using std::cout;
using std::cin;
using std::endline;
using std::vector;

int main(){

    cout << "Please enter a positive integer number you wish to compute squares for: " << endl;
    int number; 
    cin >> number;

    cout << "Please enter the bound for the largest square: " << endl;
    int bound;
    cin >> bound;

    vector<int> squares = computeBoundedSquares(bound, number);

    cout << "Computed Squares = " << squares << endl;

    return 0;

}
