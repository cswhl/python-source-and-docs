/*
 * =====================================================================================
 *
 *       Filename:  alarm.c
 *
 *    Description:  ararm SIGALARM
 *
 *        Version:  1.0
 *        Created:  12/10/2020 06:44:57 AM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (),
 *   Organization:
 *
 * =====================================================================================
 */
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
