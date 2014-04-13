#include <stdio.h>
#include <stdlib.h>

int
main (int argc, char *argv[],int i) {
	char msg[200];
	FILE *p = fopen(argv[1], "r");
	while (fgets(msg, 200, p)) {
		int times[26] = {0};		
		for (i=0; msg[i]; i++) {
			if (msg[i] >= 'a' && msg[i] <= 'z') {
				times[msg[i] - 'a']++;
			} else if (msg[i] >= 'A' && msg[i] <= 'Z') {
				times[msg[i] + 32 - 'a']++;
			} else {
				continue;
			}
		}
		short full = 1;
		for (i = 0; i < 26; i++) {
			if (times[i] == 0) {
				printf("%c", i + 'a');
				full = 0;
			}
		}
		if (full == 0) {
			printf("\n");
		} else {
			puts("NULL");
		}
	}
}
