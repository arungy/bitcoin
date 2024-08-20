#include <iostream>
#include <cstring>

using namespace std;

class String {

protected:
        int size;
        char *s;
public:
    String()
    {
        size = 0;
        s = NULL;
    }

    String(const char *str)
    {
        if (str) {
            size = strlen(str) + 1;
            s = new char [size];
            strcpy(s, str);
        }
    }

    ~String()
    {
        if (s) {
            delete [] s;
            s = NULL;
        }
    }

    String(const String &str)
    {
        if (str.s) {
            size = strlen(str.s) + 1;
            s = new char [size];
            strcpy(s, str.s);
        }
    }

    void operator = (const String& str)
    {
        if (s) {
            delete [] s;
            s = NULL;
        }

        if (str.s) {
            size = strlen(str.s) + 1;
            s = new char [size];
            strcpy(s, str.s);
        }
    }

    void update(const char* newstr = NULL)
    {
        if (s) {
            delete [] s;
            s = 0;
        }

        if (newstr) {
            size = strlen(newstr) + 1;
            s = new char [size];
            strcpy(s, newstr);
        }
    }

    void print();
};

void String::print()
{
    if (s) { cout << "string: " << s << endl; }
}

int main()
{
    String s1("First String");
    String s2(s1);

    s1.print();
    s2.print();

    s1.update("First update string");
    s2.update("Second update");

    s1.print();
    s2.print();

    s2 = s1;        //for assignment operator also, we need to provide user-defined copy constructor.

    s1.print();
    s2.print();

    String s3;      //empty string
    s3.print();

    return 0;
}
