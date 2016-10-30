#include <vector>
#include <map>
#include <string>
#include "grammer.h"
#include "readgrammer.h"
#include "split.h"

using std::cout;
using std::cin;
using std::vector;
using std::string;
using std::endl;

int main() {
    // generate the sentence
    vector<string> sentence = gen_sentence(read_grammer(cin));
    
    // write the first word if any
    vector<string>::const_iterator it = sentence.begin();
    if (!sentence.empty()) {
        cout << *it;
        ++it;    
    }

    // write the rest of the words, each preceded by a space
    while (it != sentence.end()) {
        cout << " " << *it;
        ++it;
    }

    cout << endl;
    return 0;
}
