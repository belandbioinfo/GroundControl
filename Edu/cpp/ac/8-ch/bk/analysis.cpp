// source file for the median function
#include <algorithm>
#include <stdexcept>
#include <vector>
#include <iostream>
#include <string>
#include "grade.h"

using std::domain_error;    
using std::sort;
using std::vector;
using std::endl;
using std::string;
using std::ostream;

// compute the median of a vector<double>
double median(vector<double> vec) {
    typedef vector<double>::size_type vec_sz;
    vec_sz size = vec.size();
    if (size == 0)
        throw domain_error("median of an empty vector");
    
    sort(vec.begin(), vec.end());

    vec_sz mid = size/2;

    return size % 2 == 0 ? (vec[mid] + vec[mid-1]) / 2 : vec[mid];
}

double optimistic_median(const Student_info& s){
    vector<double> nonzero;
    remove_copy(s.homework.begin(), s.homework.end(),
            back_inserter(nonzero), 0);
    if (nonzero.empty())
        return grade(s.midterm, s.final, 0);
    else
        return grade(s.midterm, s.final, median(nonzero));
}

double median_analysis(const vector<Student_info>& student){
    vector<double> grades;

    transform(student.begin(), student.end(),
            back_inserter(grades), grade_aux);
    return median(grades);
}

double average_analysis(const vector<Student_info>& students){
    vector<double> grades;

    transform(students.begin(), students.end(),
            back_inserter(grades), average_grade);
    return median(grades);
}

double optimistic_median_analysis(const vector<Student_info>& students){
    vector<double> grades;

    transform(students.begin(), students.end(),
            back_inserter(grades), optimistic_median);
    return median(grades);
}

void write_analysis(ostream& out, const string& name,
       double analysis(const vector<Student_info>&),
       const vector<Student_info>& did,
       const vector<Student_info>& didnt){
    out << name << ": median(did) = " << analysis(did) <<
        ", median(didnt) = " << analysis(didnt) << endl;
}
