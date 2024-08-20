//
// compilation: g++ cpp_array_ex1.cpp --std=c++11 -o cpp_array_ex1.exe
//

#include <iostream>
#include <array>
#include <algorithm>
#include <iterator>

using namespace std;

int main(void)
{
    std::array<int, 5> a1 {{1, 3, 2, 5, 4}};
    
    std:array<std::string, 3>  s1 {{"a", "c", std::string("b")}};
    
    cout << "C++ Hello world!" << endl;
    
    std::sort(a1.begin(), a1.end());
    
    for (const auto& a: a1){
        cout << a << endl;
    }
    
    std::sort(s1.begin(), s1.end());
    std::reverse_copy(s1.begin(), s1.end(), std::ostream_iterator<std::string>(std::cout, "\n"));
    
    //[[maybe_unused]] std::array a4{1.0, 2.0, 3.0, 4.0};       //supported in C++17
        
    return 0;
}