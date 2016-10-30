#ifndef GUARD_analysis_h
#define GUARD_analysis_h

// analysis.h
#include <vector>
#include <iostream>
#include <string>
#include "Student_info.h"

double median(std::vector<double>);
double optimistic_median(const Student_info&);
double median_analysis(const std::vector<Student_info>&);
double average_analysis(const std::vector<Student_info>&);
double optimistic_median_analysis(const std::vector<Student_info>&);
void write_analysis(std::ostream&, const std::string&,
       double analysis(const std::vector<Student_info>&),
       const std::vector<Student_info>&,
       const std::vector<Student_info>&);

#endif

