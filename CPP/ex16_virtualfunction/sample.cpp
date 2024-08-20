
#include <iostream>
#include <cstring>

using namespace std;

class base
{
    public:
    virtual void print()
    {
        cout << "Base class print()" << endl;
    }

    void show()
    {
        cout << "Base class show()" << endl;
    }
};


class derived1: public base
{
    public:
    void print()
    {
        cout << "Derived1 class print()" << endl;
    }

    void show()
    {
        cout << "Derived1 class show()" << endl;
    }
};


int main()
{
    base *ptr = NULL;

    derived1 dobj;
    ptr = &dobj;

    ptr->print();       //binded at run time due to virtual function
    ptr->show();        //binded at compile time

    return 0;
}
