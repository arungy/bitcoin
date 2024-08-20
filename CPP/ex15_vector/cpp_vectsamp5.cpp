
#include <iostream>
#include <vector>
#include <list>

#include <algorithm>

using namespace std;

bool _predicate(const int &element) {
    return (element >= 3 && element <= 5);
}

int main()
{
    vector<string> str{"one", "two", "three", "four", "two", "five"};
    for (auto &s : str) {
        cout << s << " ";
    }
    cout << "\n";
    
    //delete an element
    //str.pop_back();
    //str.clear();
    //str.erase(str.begin() + 2);
    
    //str.erase(str.begin() + 1, str.end() - 1);
    str.erase(remove(str.begin(), str.end(), "two"), str.end());
    
    for (auto &s : str) {
        cout << s << " ";
    }
    cout << "\n";
    
    
    vector<int> n{1, 2, 3, 4, 5, 6};
    //n.erase(remove_if(n.begin(), n.end(), _predicate), n.end());
    n.erase(remove_if(n.begin(), n.end(), 
                        [](auto &element) {return (element >= 3 && element <= 5);} ), n.end());
        
    for (auto &v : n) {
        cout << v << " ";
    }
    cout << "\n";
    
    //delete element by condition
    vector<int> v{-1, 0, 1, 2, 3, 4, 5, 6};
    
    typedef vector<int>::reverse_iterator rev_itr;
    rev_itr it = v.rbegin();
    
    while (it != v.rend()) {
        int value = *it;
        if (value) {
            ++it;
            it = rev_itr(v.erase(it.base()));
        } else {
            ++it;
        }
    }
    for (auto &val : v) {
        cout << val << " ";
    }
    cout << "\n";

    
    
    
    return 0;
}
