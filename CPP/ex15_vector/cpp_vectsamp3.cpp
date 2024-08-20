
#include <iostream>
#include <vector>
#include <list>

using namespace std;

int main()
{
    vector<int> v {5, 10, 15, 20};
    
    //v.reserve(6);
    for (auto &val : v) {
        cout << val << " ";
    }
    cout << "\n";
    
    vector<int> v1 {3, 6};
    for (auto &val : v1) {
        cout << val << " ";
    }
    cout << "\n";
    
    vector<int> v2 (3, 6);
    for (auto &val : v2) {
        cout << val << " ";
    }
    cout << "\n";
    
    vector<int> v3 (4, 0);
    for (auto &val : v3) {
        cout << val << " ";
    }
    cout << "\n";
    
    //copy & moving vectors
    vector<int> cv(v);
    for (auto &val : cv) {
        cout << val << " ";
    }
    cout << "\n";
    
    for (auto &val : v) {
        cout << val << " ";
    }
    cout << "\n";

    //moving vectors
    vector<int> cv1(move(v1));
    for (auto &val : cv1) {
        cout << val << " ";
    }
    cout << "\n";
    
    for (auto &val : v1) {      //it won't print anything, since its moved.
        cout << val << " ";
    }
    cout << "\n";
    
    //intiaiizing partical vector elements
    vector<int> pv(v.begin(), v.begin() + 2);
    for (auto &val : pv) {      //it won't print anything, since its moved.
        cout << val << " ";
    }
    cout << "\n";
    
    //intialize list
    list<int> lt{11, 22, 33, 44, 55};
    vector<int> listvect(lt.begin(), lt.end());
    for (auto &val : listvect) {      //it won't print anything, since its moved.
        cout << val << " ";
    }
    cout << "\n";
    
    return 0;
}
