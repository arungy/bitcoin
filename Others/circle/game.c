#include <stdlib.h>
#include <locale.h>
#include <stdio.h>
#include <wchar.h>
#include <graphics.h>

int main(void)
{
    setlocale(LC_ALL, "");
    fwide(stdout, 1);

    wprintf(L"🞨🞩🞪🞫🞬🞭🞮 🞉🞈🞇🞆🞅\n");
    
    char seq[16][3] = {
      "1 ", "2 ", "3 ", "4 ",
      "5 ", "6 ", "7 ", "8 ",
      "9 ", "10", "11", "12",
      "13", "14", "15", "  ",
    };

    wprintf(L"+------+------+------+------+\n");
    wprintf(L"|      |      |      |      |\n");
    wprintf(L"|  %s  |  %s  |  %s  |  %s  |\n", seq[0], seq[1], seq[2], seq[3]);
    wprintf(L"|      |      |      |      |\n");
    wprintf(L"+------+------+------+------+\n");
    wprintf(L"|      |      |      |      |\n");
    wprintf(L"|  %s  |  %s  |  %s  |  %s  |\n", seq[4], seq[5], seq[6], seq[7]);    
    wprintf(L"|      |      |      |      |\n");    
    wprintf(L"+------+------+------+------+\n");
    wprintf(L"|      |      |      |      |\n");
    wprintf(L"|  %s  |  %s  |  %s  |  %s  |\n", seq[8], seq[9], seq[10], seq[11]);
    wprintf(L"|      |      |      |      |\n");
    wprintf(L"+------+------+------+------+\n");
    wprintf(L"|      |      |      |      |\n");
    wprintf(L"|  %s  |  %s  |  %s  |  %s  |\n", seq[12], seq[13], seq[14], seq[15]);    
    wprintf(L"|      |      |      |      |\n");    
    wprintf(L"+------+------+------+------+\n");

    return EXIT_SUCCESS;
}