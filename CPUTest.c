#include <time.h>
#include <sys/time.h>
#include <stdlib.h>
#include <stdio.h>

#define MILLION 1000000
#define SCHEDOFF 3 
int main(int argc, char **argv) {
	long int iterations = MILLION;
	struct timeval start, end;
	long int i;
	long int time;
	long int prevtime = 0;
	long int offcount = 0;
	long int oncount = 0;
	long int inc = 0;

	gettimeofday(&start, NULL);

	for (i = 0; i < iterations; i++) {
	   gettimeofday(&end, NULL);
	   time = (end.tv_sec * 1000000 + end.tv_usec) -
		    (start.tv_sec * 1000000 + start.tv_usec);
	   if ((time - prevtime) > SCHEDOFF) {
			inc = (time - prevtime)/SCHEDOFF;
			offcount = offcount + inc;	
	   }
	   printf("%ld\t%ld\t%ld\n", i, time, offcount); 
	   prevtime = time;
	}
	return 0;
}
