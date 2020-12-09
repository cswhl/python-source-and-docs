#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <string.h>

/* sigqueue andsa_sigaction is used in conjunction to send signals and carry information
 */

void my_sigaction(int signo, siginfo_t *info, void *acInfo)
{
    printf("Cat a singal:%d\n",signo);
    printf("send signal id:%d\n",info->si_pid);
    printf("Reveive value_wordr:%d\n",(int)info->si_value.sival_int);
}

int main()
{

    //Create a child process in the parent process
    int iFork = fork();
	if (iFork> 0) {//parent process
        struct sigaction act;
        memset(&act,0,sizeof(act));
      /*
		 //How to use the function sigaction when act.sa_flags = 0
		 //Set value to act
		 act.sa_flags = 0;//Use void (*sa_handler)(int) in the structure struct sigaction to process the signal
		 act.sa_handler = signal_handler;//Set function pointer
		 sigemptyset(&act.sa_mask);//Clear the sa_mask in the structure struct sigaction to avoid random values
		 //Signal installation
         sigaction(SIGINT, &act,NULL);
      */
		 //How to use the function sigaction when act.sa_flags = SA_SIGINFO
		 //Set value to act
	    act.sa_flags = SA_SIGINFO;//Use void (*sa_sigaction)(int, siginfo_t *, void *); in the structure struct sigaction to process the signal
		act.sa_sigaction = my_sigaction;//Set function pointer
		sigemptyset(&act.sa_mask);//Clear the sa_mask in the structure struct sigaction to avoid random values

	  //Signal installation
      sigaction(SIGINT, &act,NULL);

      while (1) {
       pause();
      }
   }
   else if (iFork == 0) {//sub process
       sleep(1);
       union sigval val;
       val.sival_int=100;
       sigqueue(getppid(),SIGINT,val);
   }
   else {
     perror("fork error:");
   }
  return 0;
}

