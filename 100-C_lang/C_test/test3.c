#include <stdio.h>
#include <signal.h>
#include <stdlib.h>
#include<unistd.h>

/// 捕获一个ctrl + c产生的SIGINT信号
void handler(int sig) {
    printf("pid: %d get a signal: %d, process exit\n", getpid(), sig);
    exit(1);
}

int main() {
    signal(2, handler);
    while(1) {
        printf("process running...%d\n", getpid());
        sleep(2);
    }
    /*int *p = (int *)10;*/
    /**p = 10;*/
    return 0;
}
