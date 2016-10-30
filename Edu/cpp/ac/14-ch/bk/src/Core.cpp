// Class core

#include <iostream>
#include <string>
#include "Core.h"
#include "grade.h"

using std::istream;
using std::string;
using std::vector;
using std::endl;
using std::cerr;

// default constructor of core
Core::Core(): midterm(0), final(0) { };

// build a core from an istream
Core::Core(istream& is) 
{ 
    read(is); 
    //cerr << "Core::Core(istream&)" << endl;
}

string Core::name() const { return n_; }

double Core::grade() const {
    return ::grade(midterm, final, homework);
}

istream& Core::read_common(istream& in) {
    // read and store the student's name and exam grades
    in >> n_ >> midterm >> final;
    return in;
}

istream& Core::read(istream& in) {
    read_common(in);
    read_hw(in, homework);
    return in;
}

istream& Core::read_hw(istream& in, vector<double>& hw) {
    if (in) {
        hw.clear();
        
        double x;
        while (in >> x)
        {
            hw.push_back(x);
            CountHomework();
        }
        
        in.clear();
    }
    return in;
} 

bool Core::IsMissingHomework() const
{

    if (homeworkcount_ >= 6)
        return false;
    else 
        return true;
}
