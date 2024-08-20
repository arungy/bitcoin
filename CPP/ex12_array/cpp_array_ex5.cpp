//
// compilation: g++ cpp_array_ex5.cpp --std=c++17
//

#include <iostream>
#include <array>
#include <algorithm>
#include <string_view>      //string_view is supported in C++17

int main(void)
{
    constexpr std::array<std::string_view, 8>  data = {"▁","▂","▃","▄","▅","▆","▇","█"};
    
    std::array<std::string_view, std::size(data)> revdata;
    
    std::copy(data.begin(), data.end(), revdata.begin());
    
    auto print = [](const std::string_view s) { std::cout << s << " "; };
    
    for_each(data.cbegin(), data.cend(), print);

    std::cout << "\n\n";
    
    for_each(data.crbegin(), data.crend(), print);
    
    return 0;
}