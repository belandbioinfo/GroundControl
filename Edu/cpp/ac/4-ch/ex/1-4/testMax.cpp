#include <math.h>
#include <string>
#include "Student_info.h"
#include <iostream>

int main(){

    std::string::size_type maxlen = 3;
    Student_info s;
    unsigned int maximum = std::max(s.name.size(), maxlen);

    std::cout << maximum << std::endl;

    return 0;
}
