#include <stdio.h>
#include <unistd.h>
#include <signal.h>

int count = 0;
int main()
{
    alarm(1);
    while(1) {
        count++;
        printf("count size: %d\n", count);
    }
    return 0;
}
