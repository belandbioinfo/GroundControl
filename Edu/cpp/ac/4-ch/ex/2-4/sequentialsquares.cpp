#include <math.h>
#include <vector>
#include "sequentialsquares.h"

using std::vector;

int number = 0;
int square;
vector<double> computedsquares;

vector<double> computeSequentialSquares(int bound) {
    for (int i = 0; i <= bound; ++i) {
       square = pow(i, 2);
       computedsquares.push_back(square); 

    }
    
    return computedsquares;
}
