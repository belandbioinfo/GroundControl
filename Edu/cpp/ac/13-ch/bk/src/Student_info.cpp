#include <iostream>
#include <stdexcept>
#include "Student_info.h"
#include "Grad.h"

using std::istream;
using std::runtime_error;

// Class Student_info

// Copy and Assignment

Student_info::Student_info(const Student_info& s): cp(0) {

    if (s.cp) cp = s.cp->clone();
}

Student_info& Student_info::operator=(const Student_info& rhs) {
    if (&rhs != this) {
        delete cp;
        if (rhs.cp)
            cp = rhs.cp->clone();
        else 
            cp = 0;
    }

    return *this;
}

istream& Student_info::read(istream& is) {
    delete cp;

    char ch;
    is >> ch;

    std::cerr << "Checking type of student to dynamically bind" << std::endl;

    if (ch == 'U') {
        cp = new Core(is);
    } else if (ch == 'G') {
        cp = new Grad(is);
    } else if (ch == std::char_traits<char>::eof() || ch == std::EOF) 
    {
        std::cerr << "Finished reading file, Met EOF" << std::endl;
    }
    else
    {
        std::cerr << ch << std::endl;
        throw runtime_error("Detected grades record without 'U' or 'G' Prefix");
    }

    return is;
}

