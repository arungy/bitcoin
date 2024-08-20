
#include <iostream>
#include <vector>
#include <list>

using namespace std;

struct Point {
    double x, y;
    
    Point(double xv, double yv) : x(xv), y(yv) {}
};

int main()
{
    Point p(1.5, 2.8);
    
    vector<Point> vp{p};
    vp.push_back(p);
    vp.emplace_back(1.1, 2.2);
    
    for (auto &v : vp) {
        cout << "x: " << v.x << " ";
        cout << "y: " << v.y << " ";
        cout << "\n";
    }
    
    vector<int> vi {1, 5, 10, 15};
    
    vi.insert(vi.begin() + 1, 3);
    vi.emplace(vi.begin() + 3, 7);
    for (auto const &v: vi) {
        cout << v << " ";
    }
    cout << "\n";
    
    vector<int> ve(7);
    vector<int> v2{3, 6};
    
    ve.insert(ve.begin() + 2, v2.begin(), v2.end());
    for (auto const &t : ve) {
        cout << t << " ";
    }
    cout << "\n";
    
    return 0;
}
