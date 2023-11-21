//print_date.cpp

#include <iostream>
#include <ctime>
using namespace std;

int main()
{
	time_t t_;
	struct tm *ti;

	time(&t_);
	ti = localtime(&t_);

	cout << "now date & time is: " << asctime(ti); 

	return 0;
}
