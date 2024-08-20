#include <stdio.h>

int main()
{
	// enable 15th position
	// https://en.wikipedia.org/wiki/Bitwise_operations_in_C

	int flag1 = 0x0000000F;
	int flag2 = ((flag1 & 0xFFFFFFFF) | (1 << 15));         // enable 15th bit
	int flag3 = ((flag2 & 0xFFFFFFFF) ^ (1 << 4));          // toggling 4th bit

    int tooglebit = ((flag3 & 0xFFFFFFFF) ^ (1 << 4));      // toggling 4th bit

	int clearbit = ((flag2 & 0xFFFFFFFF) & (~(1 << 15)));   // clearing 15th bit

	printf("flag2: 0x%08x\n", flag2);
	printf("flag3: 0x%08x\n", flag3);
    printf("toogle the flag3 value: 0x%08x\n", tooglebit);
    printf("clearbit: 0x%08x\n", clearbit);

	return 0;
}