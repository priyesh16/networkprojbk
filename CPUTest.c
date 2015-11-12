#include <time.h>
#include <sys/time.h>
#include <stdlib.h>
#include <stdio.h>

#define MILLION 1000000
int main(int argc, char **argv) {
	long int iterations = MILLION;
	struct timeval start, end;
	long int i;
	long int time;

	gettimeofday(&start, NULL);

	for (i = 0; i < iterations; i++) {
	   gettimeofday(&end, NULL);
	   time = (end.tv_sec * 1000000 + end.tv_usec) -
		    (start.tv_sec * 1000000 + start.tv_usec);
	   printf("%ld\t%ld\n", i, time); 
	}
	return 0;
}
