#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>

#define STRING "hello world!"

int main()
{
    int pipefd[2];
    char buf[BUFSIZ];

    if (pipe(pipefd) == -1) { // 创建一个管道
        perror("pipe()");
        exit(1);
    }

    if (write(pipefd[1], STRING, strlen(STRING)) < 0) {
        perror("write()");
        exit(1);
    }

    if (read(pipefd[0], buf, BUFSIZ) < 0) {
        perror("write()");
        exit(1);
    }

    printf("%s\n", buf);

    exit(0);
}
