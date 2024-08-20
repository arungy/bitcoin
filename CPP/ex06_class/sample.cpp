
#include <iostream>

using namespace std;

class Base {

public:
    Base()
    {
        cout << "Base :: Constructor" << endl;
    }

    ~Base()
    {
        cout << "Base :: Destructor" << endl;
    }

    Base(int bv)
    {
        cout << "Base :: Constructor with Init" << endl;

        b = bv;
    }

    void print();

protected:
    int b;
};

void Base::print()
{
    cout << "Base b: " << b << endl;
}


class Derived : public Base {

public:
    Derived()
    {
        cout << "Derived :: Constructor" << endl;
    }
    ~Derived()
    {
        cout << "Derived :: Destructor" << endl;
    }

    Derived(int bv, int dv):Base(bv)
    {
        cout << "Derived :: Constructor with Init" << endl;
        d = dv;
    }

    void print()
    {
        Base::print();
        cout << "b: " << b << endl;
        cout << "d: " << d << endl;
    }

protected:
    int d;
};


int main()
{
        int val = 0;

        cout << "Enter the number: " ;
        cin >> val;

        Base b(val);
        b.print();
        cout << endl;

        Derived d(1, 2);
        d.print();

        return 0;
}