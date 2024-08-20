include <pthread.h>

//g++ main.cpp -lpthread

void print_message(void *ptr)
{
    char *message = (char*) ptr;
    printf("%s\n", message);
}

int counter = 0;
pthread_mutex_t mutex = PTHREAD_MUTEX_INTIALIZER;

void* increment_num(void *ptr)
{
    printf("Thread number %ld\n", pthread_self());
    pthread_mutex_lock(&mutex);
    counter++;
    pthread_mutex_unlock(&mutex);
}

int main()
{
    pthread_t thread[10];
    pthread_t thread2;

    char *message1 = "thread 1";
    char *message2 = "thread 2";

    for (int i = 0; i < 10; i++) {
        pthread_create(&thread[i], NULL, increment_num, NULL);
    }

    for (int i = 0; i < 10; i++) {
        pthread_join(thread[i], NULL);
    }

    printf("After all therads :: counter = %d\n", counter);

    return 0;
}
