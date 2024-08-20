#include <windows.h>
#include <iostream>
#include <time.h>

using namespace std; 

int main()
{
    wchar_t s1[1024] = {0};
    wchar_t s2[1024] = {0};
    wchar_t *t       = s1;

    time_t curtime = 0;
    HWND handle    = 0;
    int np         = 10;

    while (1) { 
        if ((handle = GetForegroundWindow()) != 0) {

            bool f = wcsncmp(t, (wchar_t*)"\0", 1024) == 0 ? 0 : wcsncmp(s1, t, 1024) != 0 ? 1 : 0;
            if (f) {
                t = s1;
                np == 10 ? (time(&curtime), printf("\n%s", ctime(&curtime)), np = 0) : (np += 1, wprintf(L"%s\n", t));
            } else { 
                t = s2;
            }
            GetWindowText(handle, t, 1024);
        }
        Sleep(150);
    }

}