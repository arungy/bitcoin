
#include <iostream>
#include <cstring>

using namespace std;

int main()
{
    int word = 0x87654321;

    int newword1 = ((word << 24) & 0xff000000) | ((word >> 24) & 0x000000ff) | (word & 0x00ffff00);

    printf("word: 0x%x \n", word);
    printf("new word: 0x%x \n", newword1);

    return 0;
}