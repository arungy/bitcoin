//
// compilation: g++ cpp_array_ex6.cpp --std=c++11
//

#include <iostream>
#include <array>

int main(void)
{
    constexpr std::size_t xy = 4;

    using Cell = std::array<unsigned char, 8>;

    std::array<Cell, xy * xy> board;

    board.fill({ {0xE2, 0x96, 0x84, 0xE2, 0x096, 0x80, 0, 0}});  // "▄▀";

    for (std::size_t count{}; Cell c: board) {
        std::cout << c.data() << ((++count % xy) ? "" : "\n");
    }

    return 0;
}