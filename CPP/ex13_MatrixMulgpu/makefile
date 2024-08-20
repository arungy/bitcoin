CU_APPS=matrixMul 		
		
C_APPS=

all: ${C_APPS} ${CU_APPS}

%: %.cu
	nvcc -O3 -arch=sm_62 -o $@ $<
%: %.c
	gcc -O2 -std=c99 -o $@ $<
clean:
	rm -f ${CU_APPS} ${C_APPS}
