#include <stdio.h>
#include <signal.h>
#include <stdlib.h>
#include<unistd.h>

int func(int *p)
{
	*p = 0;
}
int main()
{
	func(NULL);
	return 0;
}

