#include <stdio.h>


#define __same_type(a, b) __builtin_types_compatible_p(typeof(a), typeof(b))
#define __TYPE_IS_LL(t) (__same_type((t)0, 0LL) || __same_type((t)0, 0ULL))

int main(void)
{
    /*int cc = __TYPE_IS_LL(long long); // long long返回1，int，long返回0*/
    /*printf("%d\n", cc);*/
    int a = sizeof(int);
    printf("%u\n", sizeof(int));
}

