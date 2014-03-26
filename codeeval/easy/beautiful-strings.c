#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int cmp(const void*a, const void*b) {
	return *(int*)a- *(int*)b;
}

int 
main (int argc, char *argv[])
{
	int sum = 0;
	char chars[26] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	char msg[1000];
	FILE *p = NULL;
	int i = 0;
	p = fopen(argv[1], "r");
	while((fgets(msg, 1000, p)) != NULL) {
		// puts(msg);
		int *times = NULL;
		times = (int*)malloc(26 * sizeof(int));
		sum = 0;
		for (i = 0; msg[i]; i++) {
			if (isalpha(msg[i])) {
				msg[i] = toupper(msg[i]);
				*(times + msg[i] - 'A') += 1;
			}
		}
		qsort(times, 26, sizeof(int), cmp);
		for (i = 25; times[i]; i -= 1) {
			sum += ((i+1) * times[i]);
		}
		printf("%d\n", sum);
	}
	return 0;
}