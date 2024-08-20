#include <stdio.h>

int main()
{
    /*
        In computing, endianness is the order or sequence of bytes
        of a word of digital data in computer storage. Endianness
        is primarily expressed as big-endian or little-endian.

        A big-endian system stores the most significant byte of a
        word at the smallest memory address and the least significant
        byte at the largest memory address.
    */

    unsigned int v = 0x76543210;
    char *c = (char *) &v;

    if (0x10 == (*c)) {
        printf("Little Endian\n");
    } else {
        printf("Big Endian\n");
    }
    
    printf("%x\n", c);
    printf("%x\n", ++c);

    return 0;
}