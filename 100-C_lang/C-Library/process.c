#include <stdio.h>
#include <signal.h>
#include <unistd.h>

void handler(int sig)
{
    printf("get a signal: %d\n", sig);
}

/* use with mykill process
 * just kill -9 can terminator the process */
int main()
{
    int i = 1;
    for (; i<=31; i++) {
        signal(i, handler); // set signal i to  handler
    }
    while(1){
        printf("process running..., pid: %d\n", getpid());
        sleep(3);
    }
}
