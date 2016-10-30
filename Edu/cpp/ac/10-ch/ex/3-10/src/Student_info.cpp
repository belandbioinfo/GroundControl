// source file for Student_info-related functions

#include <algorithm>
#include <iostream>
#include "Student_info.h"
#include "grade.h"

using std::istream; using std::vector;

// Constructors
Student_info::Student_info(): midterm(0), final(0) { }
Student_info::Student_info(istream& is) { Student_info::read(is); }

bool compare(const Student_info& x, const Student_info& y) {
    return x.name() < y.name();
}

double Student_info::grade() const {
    return ::grade(midterm, final, homework); 
}

istream& Student_info::read(istream& in) {
    // read and store the student's name and midterm and final exam grades
    in >> n >> midterm >> final;

    read_hw(in, homework);  // read and store all the student's homework grades
    return in;
}

// read homework grades from an input stream into a vector<double>
istream& read_hw(istream& in, vector<double>& hw) {
    if (in) {
        // get rid of previous contents
        hw.clear();

        // read homework grades
        double x;
        while (in >> x)
            hw.push_back(x);

        // clear the stream so that input will work for the next student
        in.clear();
    }
    return in;
} 
