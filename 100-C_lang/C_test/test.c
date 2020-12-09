#include <stdio.h>

#define STRINGIFY(x) #x
#define STR_APPEND2_STR(param1, param2) STRINGIFY(param1##param2)

int main(void) {
    printf("to_str = %s, append_str = %s\n", STRINGIFY(1+1), STR_APPEND2_STR(ABC_, ABC));
}
