#include <iostream>
#include <vector>

using std::cout;
using std::vector;
using std::endl;

void addOne(int x){
    cout << "int x = " << x << endl;
    x++;
     
}

void addOneVec(vector<int>* vec){
    for(vector<int>::iterator it = vec->begin();
           it != vec->end(); it++){
        cout << "vec+1 = " << ++(*it) << endl;
    }
}

void testvecfunc(){
    vector<int> testvec;
    testvec.push_back(1);
    testvec.push_back(2);
    testvec.push_back(3);
    testvec.push_back(4);
    testvec.push_back(5);

    for(vector<int>::const_iterator it = testvec.begin();
           it != testvec.end(); it++){
        cout << "testvec at " << &it << " is equal to " << *it << endl;
    }

    addOneVec(&testvec);
}

int main(){
    int testint = 5;
    int* pint;
    pint = &testint;
    cout << "testint = " << testint << endl;
    cout << "pint = " << pint << endl;    
    cout << "&pint = " << &pint << endl;
    //cout << "pint& = " << pint& << endl;
    cout << "*pint = " << *pint << endl;
    //cout << "pint*" << pint* << endl;
    
    addOne(*pint);
    cout << "addOne(int* x) = " << testint << endl; 
    cout << "sizeof int" << sizeof(int) << endl;

    testvecfunc();
    return 0;
}

