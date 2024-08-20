//
// compilation: g++ cpp_array_ex6.cpp --std=c++11
//

#include <iostream>
#include <array>

const char* seperate(unsigned long long int n)
{
    static char buf[64];

    int i{sizeof(buf) - 1}, j{};

    buf[i] = '\0';

    do {
        buf[--i] = '0' + (n % 10);
        if (j++ % 3 == 2){
            buf[--i] = '\'';
        }
    } while (n /= 10);
    
    return buf + i + (buf[i] == '\'' ? 1 : 0);
}

int main(void)
{
    std::array<char, 102> s;

    std::cout <<"Max size of the 'array' is " << seperate(s.max_size()) << "\n";
    std::cout <<"Max size: "  << s.max_size() << "\n";

    return 0;
}