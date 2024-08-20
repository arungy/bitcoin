//
// compilation: g++ cpp_array_ex3.cpp --std=c++20
//

#include <iostream>
#include <array>
#include <span>         //supported in C++20

void pointer_func(int *ptr, const int size)
{
    std::cout << "data = ";
    for (int i = 0; i < size; i++) {
        std::cout << ptr[i] << " ";
    }
    std::cout << "\n";
}

void span_func(std::span<const int> ptr2)
{
    std::cout << "data2 = ";
    for (const int e: ptr2) {
        std::cout << e << " ";
    }
    std::cout << "\n";
}

int main(void)
{
    std::array<int, 5> container{1, 2, 3, 4, 5};
    
    if (!container.empty()) {
        pointer_func(container.data(), container.size());
        span_func( {container.data(), container.size()} );
    }
            
    return 0;
}