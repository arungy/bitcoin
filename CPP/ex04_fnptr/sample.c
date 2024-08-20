#include <stdio.h>
#include <string.h>

void reverse_str(char *str)
{
    int len = strlen(str) - 1;
    int i = 0;

    printf("Size of %s : %d \n", str, len);

    for (i = 0; i <= (len/2); i++) {
        char t       = str[i];
        str[i]       = str[len - i];
        str[len - i] = t;
    }
}

void printStr(char *str)
{
    int len = strlen(str);

    if (len > 1)
        printf("%s\n", str);
}


int main()
{
    char str[64] = "I am hero Madam";

    void (*fnptr) (char*) = NULL;

    printf("Str: %s\n", str);

    //string reversal
    reverse_str(str);

    printf("Rev Str: %s\n", str);

    //function pointer
    fnptr = printStr;
    fnptr("Calling Function Pointer");

    return 0;
}