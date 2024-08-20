
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> v;
    int sum {0};
    
    for (int i = 0; i < 10; i++) {
        v.push_back(i + 1);
    }
    
    cout << v.empty() << endl;
    
    while (!v.empty()) {
        sum += v.back();
        v.pop_back();
    }
    
    cout << "Sum of 1 to 10 is " << sum << endl;
    
    for (auto val:v) {
        cout << val << ",";
    }
    
    return 0;
}
