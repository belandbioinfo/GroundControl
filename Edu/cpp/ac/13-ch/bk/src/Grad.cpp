// Class Grad

#include <iostream>
#include <algorithm>
#include "Grad.h"

using std::min;
using std::istream;
using std::endl;
using std::cerr;


Grad::Grad(std::istream& is)
{ 
    read(is); 
    //cerr << "Grad::Grad(istream&)" << endl;
}

double Grad::grade() const {
    // return dubs
    return min(Core::grade(), thesis);
}

istream& Grad::read(istream& in) {
    read_common(in);
    in >> thesis;
    read_hw(in, homework);
    return in;
}
