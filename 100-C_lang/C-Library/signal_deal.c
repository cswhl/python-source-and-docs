
#include<stdio.h>
#include<signal.h>
#include<unistd.h>

/*
 * Add the signal SIGINT to the signal set, set the signal set to a blocked signal set, get the pending signal set, and print it out. When you enter Ctrl+C, you can find that the pending signal set has changed.
 *
 * in conclusion:
 *
 * If a signal is blocked by the process, it will not be passed to the process, but it will stay in the pending state.When the signal is blocked, The signal will be processed immediately.
 */

// Block a signal, print the pending signal set
void printsigset(sigset_t *set)
{
    int i = 0;
    for(;i<32;i++){
		if(sigismember(set,i)) //Determine whether the specified signal is in the target set
            putchar('1');
        else
            putchar('0');
    }
    puts("");
}

int main()
{
	sigset_t s,p; //Define the signal set object, and clear the initialization, sigset_t 128bytes
    sigemptyset(&s);
	sigaddset(&s,SIGINT); //Add signal to the signal set, SIGINT是 ctrl+c发出的信号
	sigprocmask(SIG_BLOCK,&s,NULL); //Set blocking signal set, SIGINT信号被阻挡后ctrl+c是无法停止程序的
    while(1) {
		sigpending(&p); //Get pending signal set
        printsigset(&p);
        sleep(1);
    }
    return 0;
}

