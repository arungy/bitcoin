//
// Data Structure Algorithm (Sorting: Insertion)
//
// build: gcc -g -Wall -O ds-sort-insertion.c -o ds-sort-insertion -lm 
//

#include <stdlib.h>
#include <stdio.h>
#include <time.h>

#define ELEMENTS_N      10

int sort_insertion(int data[], int size)
{
  int i = 0;
  
  while (i < size) {
      int j = i + 1;
      while (j < size) {
          if (data[i] > data[j]) {
              int tmp = data[i];
              data[i] = data[j];
              data[j] = tmp;
          }
          j += 1;
      }
      i += 1;
  }
    
  return EXIT_SUCCESS;
}


void get_random_value(int elem[], unsigned int size)
{
    srandom(time(NULL));
    
    for (unsigned int i = 0; i < size; i++) {
        elem[i] = random();
    }
}

void reset_elements(int elem[], unsigned int size)
{
    for (unsigned int i = 0; i < size; i++) {
        elem[i] = 0;
    }
}

int print_elements(int elem[], unsigned int size)
{
    if (size <= 0)
        return EXIT_FAILURE;
    
    printf("Elements are: ");
    for (unsigned int i = 0; i < size; i++) {
        printf("%d, ", elem[i]);
    }
    printf("\n");
    
    return EXIT_SUCCESS;
}

int main(void)
{
    int elem[ELEMENTS_N] = {2, 4, 5, 12, -4, -100, 44, 666, 78, 21};
    
    //get_random_value(elem, ELEMENTS_N);
    
    sort_insertion(elem, ELEMENTS_N);
    
    print_elements(elem, ELEMENTS_N);
    
    return EXIT_SUCCESS;
}