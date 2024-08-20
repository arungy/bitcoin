
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    std::vector<int> vect {1, 3, 5, 7};
    
    std::vector<int> empty;
    
    
    cout << "size of vect: " << vect.size() << "\n";
    cout << "Original value: ";
    for (int v : vect) {
        cout << v << " ";
    }
    cout << "\n";
    
    vect.front() = -1;
    vect.back() = 999;
    
    cout << "Modified value: ";
    for (int v : vect) {
        cout << v << " ";
    }
    cout << "\n";
    
    // empty.front() = 0;  //when empty vector is access via front()/back() throws seg fault error
    
    return 0;
}
