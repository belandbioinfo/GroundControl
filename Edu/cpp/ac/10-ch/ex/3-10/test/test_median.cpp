#include <boost/test/included/unit_test.hpp>

#include <vector>
#include <algorithm>
#include <iostream>
#include "../src/median.h"


using namespace boost::unit_test;
using std::vector;
using std::cout;
using std::endl;

void test_median_order()
{

    vector<double> orig;
    orig.push_back(4);
    orig.push_back(16);
    orig.push_back(-20);
    orig.push_back(12);
    orig.push_back(100);

    vector<double> copyvec;

    copy(orig.begin(), orig.end(), back_inserter(copyvec));

    double uselessmedian = median(copyvec);

    if (orig == copyvec) {
        // print orig values
        cout << "orig:" << endl;
        for (vector<double>::const_iterator it = orig.begin();
                it != orig.end(); it++)
            cout << *it << " ";
        cout << endl << endl;

        // print copyvec values
        cout << "copyvec:" << endl;
        for (vector<double>::const_iterator it = copyvec.begin();
                it != copyvec.end(); it++)
            cout << *it << " ";
        cout << endl << endl;

        BOOST_CHECK( true /* test assertion */ );
    }
    else
        BOOST_CHECK( false /* test assertion */ );
}

test_suite* init_unit_test_suite( int /*argc*/, char* /*argv*/[] )
{
    framework::master_test_suite().
    add( BOOST_TEST_CASE( &test_median_order ) );
        
    return 0;
}
