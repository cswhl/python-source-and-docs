# include <stdio.h>

#define __stringify_1(x...) #x  // #的作用是将宏参数字符串化,如:#do = > "do"
#define __stringify(x...)   __stringify_1(x)

void sys_socket(int n) __attribute__((alias(__stringify(SyS_socket))));

void SyS_socket(int num) {
    printf("%d,%s\n", num, "you call SYS_socket");
}

int main(void) {
    sys_socket(1);
}

