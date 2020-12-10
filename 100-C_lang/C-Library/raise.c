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
    signal(SIGINT, handler); // set SIGINT to  handler
    while(1){
        printf("process running..., pid: %d\n", getpid());
        sleep(3);
        raise(SIGINT); // set SIGINT to yourself
    }
}
