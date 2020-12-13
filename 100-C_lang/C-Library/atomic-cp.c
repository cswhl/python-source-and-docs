#include <stdio.h>
#include <stdatomic.h>
#include <pthread.h>
#include <unistd.h>

// 编译: gccc -std=gnu11 -o atomic-cp atomic-cp.c -pthread
int cnt;
atomic_int acnt; // 定义一个原子对象

void* f(void* param)
{
    for(int n = 0; n < 1000; ++n) {
      ++cnt;
      atomic_fetch_add(&acnt, 1);
    }
    return NULL;
}

// 测试原子操作在线程中的意义：使用原子操作的acnt计算结果为10000，而普通变量的计算结果则不一定为10000
int main(void)
{
    pthread_t t[10];
    for (int i = 0; i < 10; i++) pthread_create(&t[i], NULL, f, NULL);//创建10个线程,每个都执行f函数
    for (int i = 0; i < 10; i++) pthread_join(t[i], NULL);
        printf("acnt = %u; cnt = %u;\n", acnt, cnt);
    atomic_int v = ATOMIC_VAR_INIT(1); // 初始化一个新的原子对象
    printf("v=%d\n", v);
    atomic_init(&v, 5); // 初始化现有原子对象, 放函数体外就会报错，何故？
    printf("v=%d\n", v);
}


