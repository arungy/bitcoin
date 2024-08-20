	
#include <iostream>
#include <string>

using namespace std;

class base
{
    private:
        int *a1;
        float a2;
        std::string a3;
        
	public:
    base() {
        a1 = NULL;
        a2 = 0.0;
        a3 = "";
    }
    
    void init(int x, float y, std::string z) {
        if (a1 == NULL) {
            a1 = new int;
        }
        
        *a1 = x;
        a2 = y; 
        a3 = z;
    }
    
    ~base(){
        if (a1) {
            delete a1;
            a1 = NULL;
        }
    }
    
	void print()
	{
		if (a1) {
            cout << *a1 << "," << a2 << "," << a3 << endl;
        }
	}
};

int main()
{
	base b[10];
    
    for (int i = 0; i < 10; i++) {
        b[i].init(i + 1, ((i + 1) * 1.55), "test") ;
    }
    
    for (int i = 0; i < 10; i++) {
        b[i].print();
    }
		
	return 0;
}
