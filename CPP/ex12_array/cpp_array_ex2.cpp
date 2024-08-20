//
// compilation: g++ cpp_array_ex2.cpp --std=c++11
//

#include <iostream>
#include <array>

int main(void)
{
    std::array<char, 5> letters {'a', 'e', 'i', 'o', 'u'};
    
    if (!letters.empty()) {
        std::cout << "The first character is " << letters.front() << "\n";
        std::cout << "The last character is " << letters.back() << "\n";
    }
            
    return 0;
}