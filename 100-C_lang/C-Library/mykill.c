#include <stdio.h>
#include <signal.h>
#include <sys/types.h>
#include <stdlib.h>

static void usage(const char *proc)
{
    printf("Usage: %s signo pid \n:", proc);
}

/* use kill sent signal to process, because kill can set any signal */
int main(int argc, char * argv[])
{
    if (argc != 3) {
        usage(argv[0]);
        return 0;
    }
    int signo = atoi(argv[1]);
    int pid = atoi(argv[2]);

    kill(pid, signo); // sent signo to  pid process
    return 0;
}
