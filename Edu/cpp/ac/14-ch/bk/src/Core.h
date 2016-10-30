#ifndef GUARD_Core_h
#define GUARD_Core_h

#include <iostream>
#include <string>
#include <vector>
#include <string>

class Core {
public:
    // Constructors and Destructors
    Core();
    Core(std::istream&);
    virtual ~Core() { }

    // Public Interface
    friend class Student_info;
    std::string name() const;
    virtual double grade() const;
    virtual std::istream& read(std::istream&);
    bool IsMissingHomework() const;
protected:
    virtual Core* clone() const { return new Core(*this); }
    virtual void CountHomework() { ++homeworkcount_; }
    std::istream& read_common(std::istream&);
    std::istream& read_hw(std::istream&, std::vector<double>&);

    double midterm, final;
    std::vector<double> homework;
    int homeworkcount_;
private:
    std::string n_;
};

#endif
