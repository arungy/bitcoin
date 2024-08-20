//
// compilation: g++ cpp_array_ex4.cpp --std=c++17
//

#include <iostream>
#include <array>
#include <algorithm>
//#include <iomanip>

int main(void)
{
    std::cout << std::boolalpha;

    std::array<int, 0> empty;

    std::cout << "1) "
              << (empty.begin()  == empty.end())  << ' '
              << (empty.cbegin() == empty.cend()) << '\n';
    //*(empty.begin()) = 4;     //undefined behaviour

    std::array<int, 4> numbers {5, 2, 3, 4};
    std::cout << "2) "
              << (numbers.begin()  == numbers.end())  << ' '
              << (numbers.cbegin() == numbers.cend()) << '\n'
              << "3) "
              << *numbers.begin() << ' '
              << *numbers.cbegin() << '\n';
              
    *numbers.begin() = 1;
    std::cout << "4) " << *numbers.begin() << '\n';

    //*numbers.cbegin() = 42;
    std::cout << "5) ";
    std::for_each(numbers.cbegin(), numbers.cend(), [](int x) {
        std::cout << x << ' ';
    });
    std::cout <<'\n';

    constexpr std::array constants {'A', 'B', 'C'};        //constexpr is supported in C++17
    static_assert(constants.begin()  != constants.end()); 
    static_assert(constants.cbegin() != constants.cend()); 
    static_assert(*constants.begin()  == 'A'); 
    static_assert(*constants.cbegin() == 'A'); 
    //*constants.begin() = 'Z';
    
    return 0;
}