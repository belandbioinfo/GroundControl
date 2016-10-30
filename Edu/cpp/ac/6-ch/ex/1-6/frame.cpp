#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using std::vector;
using std::string;
using std::cin;
using std::cout;
using std::max;


string border;
string::size_type maxlen = 0;

string::size_type width(const vector<string>& v){
    for(vector<string>::size_type i = 0; i != v.size(); ++i)
        maxlen = max(maxlen, v[i].size());
    return maxlen;

}

string frameMiddle(const string& s){
   string retstring; 
   retstring = "* " + s + string(maxlen - s.size(), ' ') + " *";
   return retstring;

}

vector<string> frame(const vector<string>& v){
    vector<string> ret;
    maxlen = width(v);
    border = string(maxlen + 4, '*');

    // write the top header
    ret.push_back(border);

//    for (vector<string>::size_type i = 0; i != v.size(); ++i)
//        ret.push_back("* " + v[i] + 
//                string(maxlen - v[i].size(), ' ') + " *");

    transform(v.begin(), v.end(), back_inserter(ret), frameMiddle);
    
    // write the bottom border
    ret.push_back(border);
    return ret;
}

vector<string> vcat(const vector<string>& top,
                    const vector<string>& bottom){
    vector<string> ret = top;

    for (vector<string>::const_iterator it = bottom.begin();
            it != bottom.end(); ++it)
        ret.push_back(*it);
    return ret;
}

vector<string>
hcat(const vector<string>& left, const vector<string>& right){
    vector<string> ret;

    string::size_type width1 = width(left) + 1;

    vector<string>::size_type i = 0, j = 0;

    while (i != left.size() || j != right.size()){
        string s;

        if (i != left.size())
            s = left[i++];

        s += string(width1 - s.size(), ' ');
        if (j != right.size())
            s += right[j++];

        ret.push_back(s);

    }
    return ret;
}

int main(){

    static const string arr[] = {"this is an","example","to","illustrate","framing"};
    vector<string> text (arr, arr+sizeof(arr) / sizeof(arr[0]));


    vector<string> framedtext = frame(text);
   
    vector<string> verttext = vcat(text, framedtext);
    vector<string> horitext = hcat(text, framedtext);

    for (vector<string>::size_type sz = 0; sz != verttext.size(); ++sz)
        cout << verttext[sz] << std::endl;

    for (vector<string>::size_type sz = 0; sz != horitext.size(); ++sz)
        cout << horitext[sz] << std::endl;

    return 0;

}
