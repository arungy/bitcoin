#include <stdio.h>
#include <string.h>

unsigned int recursive_mul(int val)
{
    if (0 >= val)  {
        return 1;
    }

    return (val * recursive_mul(val - 1));
}


int main()
{
    int num = 10;

    printf("Sum of 0 to %d: %u \n", num, recursive_mul(num));

    printf("100%%");

    return 0;
}