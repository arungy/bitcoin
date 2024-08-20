// https://www.geeksforgeeks.org/multithreading-in-cpp/
// https://iamsorush.com/posts/cpp-std-thread/

#include <iostream>
#include <thread>

using namespace std;
using std::this_thread::sleep_for;
using std::chrono::seconds;

void print_ftn(int x) 
{
    cout << "print_fun: ";
    for (int i = 0; i < x; i++) {
        cout << i << " "; 
    }
    cout << endl;
    
    sleep_for(seconds(15));
}

class thread_obj {
public:
    void operator()(int x) {
        cout << "Class function: ";
         for (int i = x; i < x + x; i++) {
            cout << i << " ";
         }
         cout << endl;
    }
};

int main() 
{
    cout << "Main thread run independently" << endl;
    
    thread t1(print_ftn, 100);
    thread t2(thread_obj(), 100);
    
    cout << "printing from main thread after launching threads..." << endl;
    
    t1.join();
    t2.join();


    unsigned int n = std::thread::hardware_concurrency();   
    std::cout << n << " concurrent threads are supported.\n";
    
    return 0;
}