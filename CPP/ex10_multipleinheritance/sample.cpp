
#include <iostream>

using namespace std;

class person
{
	int a;
	
	public:
		person() 
		{
			a = 0;
		}
		
		person(int v)
		{
			a = v;
			cout << "Person class" << endl;
		}
};

class faculty : virtual public person
{
	int fa;
	
	public:
		faculty()
		{
			fa = 0;
		}
		
		faculty(int v) : person(v)
		{
			fa = v;
			cout << "Faculty class" << endl;
		}
};

class student : virtual public person
{
	int sa;
	
	public:
		student()
		{
			sa = 0;
		}
		
		student(int v) : person(v)
		{
			sa = v;
			
			cout << "Student class" << endl;
		}
};

class TA : public faculty, public student
{
	int taa;
	public:
		TA()
		{
			taa = 0;
		}
		
		TA(int v): person(v), faculty(v), student(v)
		{
			taa = v;
			
			cout << "TA class" << endl;
		}
};

int main()
{
	TA t(25);
}