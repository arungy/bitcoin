
#include <stdio.h>
#include <cuda_runtime_api.h>

#define THREAD_SIZE	(2)

#define MATRIX_A_X		(2 * THREAD_SIZE)
#define MATRIX_A_Y		(1 * THREAD_SIZE)

#define MATRIX_B_X		(1 * THREAD_SIZE)
#define MATRIX_B_Y		(2 * THREAD_SIZE)


void matrixMul_RefC(int A[MATRIX_A_Y][MATRIX_A_X], int B[MATRIX_B_Y][MATRIX_B_X], int C[MATRIX_A_Y][MATRIX_B_X])
{
	//Reset the result buffer
	for (int y = 0; y < MATRIX_A_Y; y++) {
		for (int x = 0; x < MATRIX_B_X; x++)
		{
			C[y][x] = 0;
		}
	}

	//Matrix Multiplication
	for (int z = 0; z < MATRIX_B_X; z++) {
		for (int y = 0; y < MATRIX_A_Y; y++) {
			for (int x = 0; x < MATRIX_A_X; x++) {
				C[z][y] += A[y][x] * B[x][z];
			}
		}
	}

	//Print the result
	printf("Reference Source :: Matrix Multiplication Result (C = A * B): \n");
	for (int y = 0; y < MATRIX_A_Y; y++) {
		for (int x = 0; x < MATRIX_B_X; x++)
		{
			printf("%d ", C[y][x]);
		}
		printf("\n");
	}
}

__global__ void matrixMul_Kernel(int *A, int *B, int *C, int pitchA, int pitchB, int pitchC, int nElem)
{
	int x = blockIdx.x * blockDim.x + threadIdx.x;
	int y = blockIdx.y * blockDim.y + threadIdx.y;

	//Matrix Multiplication
	int cSum = 0;
	for (int k = 0; k < nElem; k++) {
		cSum += A[x * pitchA + k] * B[k * pitchB + y];
	}

	C[y * pitchC + x] = cSum;
}


void matrixMul_CUDA(int A[MATRIX_A_Y][MATRIX_A_X], int B[MATRIX_B_Y][MATRIX_B_X], int C[MATRIX_A_Y][MATRIX_B_X])
{
	cudaError_t error = cudaSuccess;
	cudaDeviceProp deviceProp;	

	int devId = 0;
	if (cudaSuccess != (error = cudaGetDevice(&devId))) {
		printf("cudaGetDevice CUDA Error: %s (code: %d)\n", cudaGetErrorString(error), error);
	}

	if (cudaSuccess != (error = cudaGetDeviceProperties(&deviceProp, devId))) {
		printf("cudaGetDeviceProperties CUDA Error: %s (code: %d)\n", cudaGetErrorString(error), error);
	}

	printf("\nGPU Device %d: \"%s\" with compute capability %d.%d\n", devId, deviceProp.name, deviceProp.major, deviceProp.minor);

	int *d_A = NULL;
	int *d_B = NULL;
	int *d_C = NULL;

	if (cudaSuccess != (error = cudaMalloc((void**)&d_A, (sizeof(int) * MATRIX_A_Y * MATRIX_A_X)))) {
		printf("cudaMalloc CUDA Error: %s (code: %d)\n", cudaGetErrorString(error), error);
	}

	if (cudaSuccess != (error = cudaMalloc((void**)&d_B, (sizeof(int) * MATRIX_B_Y * MATRIX_B_X)))) {
		printf("cudaMalloc CUDA Error: %s (code: %d)\n", cudaGetErrorString(error), error);
	}

	if (cudaSuccess != (error = cudaMalloc((void**)&d_C, (sizeof(int) * MATRIX_A_Y * MATRIX_B_X)))) {
		printf("cudaMalloc CUDA Error: %s (code: %d)\n", cudaGetErrorString(error), error);
	}

	if (cudaSuccess != (error = cudaMemcpy((void*)d_A, (void*)A, (sizeof(int) * MATRIX_A_Y * MATRIX_A_X), cudaMemcpyHostToDevice))) {
		printf("cudaMemcpy CUDA Error: %s (code: %d)\n", cudaGetErrorString(error), error);
	}

	if (cudaSuccess != (error = cudaMemcpy((void*)d_B, (void*)B, (sizeof(int) * MATRIX_B_Y * MATRIX_B_X), cudaMemcpyHostToDevice))) {
		printf("cudaMemcpy CUDA Error: %s (code: %d)\n", cudaGetErrorString(error), error);
	}

	dim3 thread(THREAD_SIZE, THREAD_SIZE);
	dim3 grid((MATRIX_A_Y / THREAD_SIZE), (MATRIX_B_X / THREAD_SIZE));

	int nElement = MATRIX_A_X;
	int pitchA = MATRIX_A_X;
	int pitchB = MATRIX_B_X;

	int pitchC  = MATRIX_A_Y;

	matrixMul_Kernel<<<grid, thread>>>(d_A, d_B, d_C, pitchA, pitchB, pitchC, nElement);

	if (cudaSuccess != (error = cudaDeviceSynchronize())) {
		printf("cudaDeviceSynchronize CUDA Error: %s (code: %d)\n", cudaGetErrorString(error), error);
	}

	//Reset the result buffer
	for (int y = 0; y < MATRIX_A_Y; y++) {
		for (int x = 0; x < MATRIX_B_X; x++)
		{
			C[y][x] = 0;
		}
	}
	
	if (cudaSuccess != (error = cudaMemcpy((void*)C, (void*)d_C, (sizeof(int) * MATRIX_A_Y * MATRIX_B_X), cudaMemcpyDeviceToHost))) {
		printf("cudaMemcpy CUDA Error: %s (code: %d)\n", cudaGetErrorString(error), error);
	}

	//Print the result
	printf("CUDA Source :: Matrix Multiplication Result (C = A * B): \n");
	for (int y = 0; y < MATRIX_A_Y; y++) {
		for (int x = 0; x < MATRIX_B_X; x++)
		{
			printf("%d ", C[y][x]);
		}
		printf("\n");
	}
}

int main()
{
	int A[MATRIX_A_Y][MATRIX_A_X];
	int B[MATRIX_B_Y][MATRIX_B_X];
	int C[MATRIX_A_Y][MATRIX_B_X];

	//Filling the A and B matrix

	for (int y = 0; y < MATRIX_A_Y; y++) {
		for (int x = 0; x < MATRIX_A_X; x++)
		{
			A[y][x] = y * MATRIX_A_X + x + 1;
		}
	}

	for (int y = 0; y < MATRIX_B_Y; y++) {
		for (int x = 0; x < MATRIX_B_X; x++)
		{
			B[y][x] = y * MATRIX_B_X + x + 1;
		}
	}

	printf("A = \n");
	for (int y = 0; y < MATRIX_A_Y; y++) {
		for (int x = 0; x < MATRIX_A_X; x++)
		{
			printf("%d ", A[y][x]);
		}
		printf("\n");
	}

	printf("B = \n");
	for (int y = 0; y < MATRIX_B_Y; y++) {
		for (int x = 0; x < MATRIX_B_X; x++)
		{
			printf("%d ", B[y][x]);
		}
		printf("\n");
	}

	//Call Reference Source
	matrixMul_RefC(A, B, C);

	//Call CUDA kernel
	matrixMul_CUDA(A, B, C);
	

	return 0;
}