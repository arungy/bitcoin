//
// compilation: g++ cpp_array_ex6.cpp --std=c++11
//

#include <array>
#include <iostream>

template<class Os, class V> Os& operator<< (Os& os, V& v) 
{
    os << "{";
    for (auto i : v) os << " " << i;
    return os << " } ";
}

int main(void)
{
    std::array<int, 3> a1{1, 2, 3}, a2{4, 5, 6};
    
    std::cout << a1 << a2 << '\n';
    a1.swap(a2);
    std::cout << a1 << a2 << '\n';
    
    return 0;
}