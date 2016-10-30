#include <math.h>
#include <vector>
#include "boundedsquares.h"

using std::vector;
using std::pow;

int square = 0;
vector<int> computedsquares;

vector<int> computeBoundedSquares(int bound, int number) {
    square = pow(number, 2);
    while ( square < bound) {
       computedsquares.push_back(square); 
       square = pow(square, 2);

    }
    
    return computedsquares;
}
