
#include <iostream>
#include <vector>
#include <list>

using namespace std;

int main()
{
    vector<string> str{"one", "two", "three", "four"};
    for (auto &s : str) {
        cout << s << " ";
    }
    cout << "\n";
    
    //copy iterator
    vector<string> cp_vect(make_move_iterator(str.begin()), make_move_iterator(str.end()));
    
    for (auto &s : cp_vect) {
        cout << s << " ";
    }
    cout << "\n";
    
    for (auto &s : str) {
        cout << s << " ";
    }
    cout << "\n";
    
    vector<string> newstr{"eleven", "tweleve"};
    newstr.assign(cp_vect.begin(), cp_vect.end());
    for (auto &s : newstr) {
        cout << s << " ";
    }
    cout << "\n";
    
    return 0;
}
