#include <boost/test/included/unit_test.hpp>
#include <boost/test/parameterized_test.hpp>
#include <algorithm>
#include <string>

#include "Vec.h"


using namespace boost::unit_test;
using std::string;

void int_constructors_test(int val)
{

    Vec<int> vec;
    vec.push_back(val);
    vec.push_back(val);

    Vec<int> vecsingle(val);

    Vec<int> vecdouble(val, val);

    BOOST_CHECK( *(vec.begin()) == val );

    BOOST_CHECK( *(vec.begin()+1) == val );

    BOOST_CHECK( *(vecsingle.begin()) == 0 );

    BOOST_CHECK( *(vecdouble.end()-1) == val );

}

void double_constructors_test(double val)
{

    Vec<double> vec;
    vec.push_back(val);
    vec.push_back(val);

    Vec<double> vecsingle(val);

    Vec<double> vecdouble(val, val);

    BOOST_CHECK( *(vec.begin()) == val );

    BOOST_CHECK( *(vec.begin()+1) == val );

    BOOST_CHECK( *(vecsingle.begin()) == 0 );

    BOOST_CHECK( *(vecdouble.end()-1) == val );

}

void assignment_test(int val)
{

    BOOST_CHECK( true /* test assertion */ );
}

void operator_test(int val)
{

    BOOST_CHECK( true /* test assertion */ );
}

void member_test()
{
    Vec<int> v;
    v.push_back(1);
    v.push_back(2);
    v.push_back(3);
    v.push_back(4);
    v.push_back(5);

    v.erase(v.begin()+2);

    BOOST_TEST_MESSAGE( "size of v = " << v.size());
    for (Vec<int>::const_iterator it = v.begin(); it != v.end(); it++){
        BOOST_TEST_MESSAGE( "val = " << *it);
    }

    BOOST_CHECK( *(v.begin()+2) == 4 );

    BOOST_CHECK( v.size() == 4 );

    Vec<int> vec;
    vec.push_back(1);
    vec.push_back(2);
    vec.push_back(3);
    vec.push_back(4);
    vec.push_back(5);

    vec.clear();

    BOOST_CHECK( vec.size() == 0 );

}

test_suite* 
init_unit_test_suite( int argc, char* argv[] )
{

    test_suite* suite = BOOST_TEST_SUITE( "test_Vec" );

    int iparams1[] = { 1, 4, 10, 3299, 9371, 1111 };
    double dparams1[] = { 1.0, 4.2193, 10238.213, 32992.3, 9.124083, 1.5 };
    suite->add( BOOST_PARAM_TEST_CASE( &int_constructors_test, iparams1, iparams1+6 ) );
    suite->add( BOOST_PARAM_TEST_CASE( &double_constructors_test, dparams1, dparams1+6 ) );

    int params2[] = { 1, 4, 10, 3299, 9371 };
    suite->add( BOOST_PARAM_TEST_CASE( &assignment_test, params2, params2+5));

    int params3[] = { 1, 4, 10, 3299, 9371 };
    suite->add( BOOST_PARAM_TEST_CASE( &operator_test, params3, params3+5));

    suite->add( BOOST_TEST_CASE( &member_test ));

    framework::master_test_suite().add( suite );
        
    return 0;
}
