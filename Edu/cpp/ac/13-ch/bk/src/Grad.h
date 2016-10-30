#ifndef GUARD_Grad_h
#define GUARD_Grad_h

#include <iostream>
#include "Core.h"

class Grad: public Core {
public:
    // default constructor of Grad
    Grad(): thesis(0) { };
    
    // build a Grad from an istream
    Grad(std::istream&);

    //Grad();
    //Grad(std::istream&);
    double grade() const;
    std::istream& read(std::istream&);
protected:
    Grad* clone() const { return new Grad(*this); }
private:
    double thesis;
};

#endif
