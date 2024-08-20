
#include <iostream>
#include <thread>

using namespace std;

class base {
public:
    base() {
        cout << "base constructor" << endl;
    }
    ~base() {
        cout << "base destructor" << endl;
    }
    
    virtual void show() {
        cout << "function in base::show()" << endl;
    }
};

class derived : public base{
public:
    derived() {
        cout << "derived constructor" << endl;
    }
    ~derived() {
        cout << "derived destructor" << endl;
    }
    
    void show() {
        cout << "function in derived::show()" << endl;
    }
};


int main() 
{
    base b;
    derived d;
    
    cout << endl;
    base *bptr = &b;
    bptr->show();
    
    bptr = &d;
    bptr->show();
    
    cout << endl;
    
    derived *dptr;
    //dptr = &b;      /* compilation error: base object cannot be assigned to derived pointer */
    //dptr->show();
    
    dptr = &d;
    dptr->show();
    
    cout << endl;
    
    return 0;
}