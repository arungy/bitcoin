#include <stdio.h>

typedef union {
  int  family_mem;
  char age_father;
  char age_mother;
  char age_child1;
  char age_child2;
} person_data;

typedef struct {
  int  family_mem;
  char age_father;
  char age_mother;
  char age_child1;
  char age_child2;
} person_data_st;

int main()
{
       person_data pd = {0};
		
	   person_data_st pds = {0};
		
        printf("size of person_data union: %d\n", sizeof(pd));
        printf("size of person_data structure: %d\n", sizeof(pds));
		
        //In union, the max size of an element is considered as size 
		//of Union and uses the common memory for all members 
        
		pd.family_mem = 1004;

		pd.age_mother = 30;
		pd.age_child1 = 5;
		pd.age_child2 = 3;
		pd.age_father = 35;		
		
		pds.family_mem = 1004;

		pds.age_mother = 30;
		pds.age_child1 = 5;
		pds.age_child2 = 3;
		pds.age_father = 35;		
		
		printf("family_mem: %d\n", pd.family_mem);
		printf("age_father: %d\n", pd.age_father);
		printf("age_mother: %d\n", pd.age_mother);
		printf("age_child1: %d\n", pd.age_child1);
		printf("age_child2: %d\n", pd.age_child2);
		
		printf("family_mem (st): %d\n", pds.family_mem);
		printf("age_father (st): %d\n", pds.age_father);
		printf("age_mother (st): %d\n", pds.age_mother);
		printf("age_child1 (st): %d\n", pds.age_child1);
		printf("age_child2 (st): %d\n", pds.age_child2);
		
		return 0;
}