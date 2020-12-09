#include <stdio.h>
// 测试 __TYPE_IS_LL宏, 要使用gcc -std=gnu11 test2.c编译

#define __same_type(a, b) __builtin_types_compatible_p(typeof(a), typeof(b))

#define __TYPE_IS_LL(t) (__same_type((t)0, 0LL) || __same_type((t)0, 0ULL))

#define BUILD_BUG_ON_ZERO(e) (sizeof(struct { int:-!!(e);  }))

#define _SC_TEST(t)  (void)BUILD_BUG_ON_ZERO(!__TYPE_IS_LL(t) && sizeof(t) > sizeof(long))

int main(void)
{
    int c1 = __TYPE_IS_LL(long long); // long long返回1，int，long返回0
    int c2 = __TYPE_IS_LL(long); // long返回0
    int c3 = __TYPE_IS_LL(int); // int返回0
    printf("%d, %d, %d\n", c1, c2, c3);
    _SC_TEST(long long); _SC_TEST(long); _SC_TEST(int);
    printf("%d, %d, %d\n", (int) sizeof(long long), (int) sizeof(long), (int) sizeof(int));
}

