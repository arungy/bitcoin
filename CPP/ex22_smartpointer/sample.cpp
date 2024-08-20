// https://en.cppreference.com/book/intro/smart_pointers

// https://iamsorush.com/posts/weak-pointer-cpp/
// https://www.nextptr.com/question/qa1348405750/dynamic-array-with-stdunique_ptr
// https://www.internalpointers.com/post/beginner-s-look-smart-pointers-modern-c

#include <iostream>
#include <memory>
#include <cstring>

using namespace std;

int main() 
{
    //unique ptr
    std::unique_ptr<int> data = std::make_unique<int> (25);
    std::unique_ptr<int[]> tmp_arr = nullptr;
    
    //the below code is written to check the scope of unqiue pointer.
    { 
        std::unique_ptr<int[]> data_arr = std::make_unique<int[]> (10);
        for (int i = 0; i < 10; i++) {
            data_arr[i] = i;
        }
        
        //unique pointer needs to assign using move() function, otherwise gives compiler error.
        tmp_arr = std::move(data_arr);  
    }
    
    cout << *data << endl;
    
    if (tmp_arr) {
        for (int i = 0; i < 10; i++) {
            cout << tmp_arr[i] << " ";
        }
        cout << endl;
    }
    
    tmp_arr.reset();
    
    //shared ptr
    std::shared_ptr<int> p_val = std::make_shared<int>(0);
    *p_val = 24;
    
    cout << *p_val << endl;
    
    //weak pointer
    
    //weak pointer only observes the memory location, mainly used to aviod circular/chain conflict
    //C++ provies 'expired()' function to check the memory is deallocated or not, so it's advantage
    // w.r.t raw pointers (since it cannot be checked).
    
    std::weak_ptr<int> p_wval(p_val);  
    

    std::shared_ptr<int> v = p_wval.lock();
    
    cout << *v << endl;


    return 0;
}