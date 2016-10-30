#include <algorithm>
#include <iomanip>
#include <ios>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
#include "grade.h"
#include "Student_info.h"

using std::cin;
using std::setprecision;
using std::cout;
using std::domain_error;    
using std::runtime_error;
using std::streamsize;
using std::endl;
using std::string;
using std::max;
using std::vector;

int main() {
    vector<Student_info*> students;
    Student_info* record;
    string::size_type maxlen = 0;
    string homework_message; 

    // read and store all the student's data
    // Invariant: students contains all the student records read so far
    //            maxlen contains the length of the longest name in students
    try { 
        //while (new Student_info()->read(cin)) {
        while (cin) {
            record = new Student_info();
            record->read(cin);
            // find length of longest name
            maxlen = max(maxlen, record->name().size());
            students.push_back(record);
        }
    } catch (runtime_error e) {
        cout << e.what() << endl;
    }

    // alphabetize the student records
    sort(students.begin(), students.end(), Student_info::compare);

    // write the names and grades
    for (vector<Student_info>::size_type i = 0;
            i != students.size(); ++i) {
        // write the name, padded on the right to maxlen + 1 characters
        cout << students[i]->name()
             << string(maxlen + 1 - students[i]->name().size(), ' ');


        // compute and write the grade
        try {
            double final_grade = students[i]->grade();
            streamsize prec = cout.precision();
            cout << setprecision(3) << final_grade
                 << setprecision(prec);


        } catch (domain_error e) {
            cout << e.what() << endl;
        }

        // write out if the student finished all homework or not
        if (students[i]->IsMissingHomework())
            homework_message = " Student Did Not Finish All Homework!!!";
        else 
            homework_message = " Student Finished All Homework!!!";

        cout << homework_message << endl;

    }
    return 0;
}
