// String implementation


#include <iostream>
#include <cstring>
#include "Str.h"

using std::istream;
using std::ostream;

ostream& operator<<(ostream& os, const Str& s) {
    for (Str::size_type i = 0; i != s.size(); ++i)
        os << s[i];
    return os;
}

istream& operator>>(istream& is, Str& s) {
    
    // obliterate existing values(s)
    s.data.clear();

    // read and discard leading whitespace
    char c;
    while (is.get(c) && isspace(c))
        ;   // nothing to do, except testing the condition
    // if still something to read, do so until next whitespace character
    if (is) {
        do s.data.push_back(c);
        while (is.get(c) && !isspace(c));

        // if we read whitespace, then put it back on the stream
        if (is)
            is.unget();
    }
    return is;
}

Str operator+(const Str& s, const Str& t) {
    Str ret = s; 
    ret += t
    return ret;
}
