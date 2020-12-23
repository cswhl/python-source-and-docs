#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{

    if (argc != 2) {
        fprintf(stderr, "Argument error!\n");
        exit(1);
    }

    if (mknod(argv[1], 0600|S_IFIFO, 0) < 0) {  // 以第一个参数作为管道文件路径
        perror("mknod()");
        exit(1);
    }

    exit(0);
}
