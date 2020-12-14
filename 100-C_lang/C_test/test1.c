#include <stdio.h>
#include <stdatomic.h>
#include <pthread.h>
#include <unistd.h>

int cnt;
atomic_int acnt;
/*atomic_int v = ATOMIC_VAR_INIT(1); // 初始化一个新的原子对象*/
/*atomic_init(&v, 5); // 初始化现有原子对象*/

void* f(void* param) {
    for(int n = 0; n < 1000; ++n) {
      ++cnt;
      atomic_fetch_add(&acnt, 1);
    }
    return NULL;
}

int main(void) {
    pthread_t t[10];
    for (int i = 0; i < 10; i++) pthread_create(&t[i], NULL, f, NULL);
    for (int i = 0; i < 10; i++) pthread_join(t[i], NULL);
        printf("acnt = %u; cnt = %u;\n", acnt, cnt);
}


