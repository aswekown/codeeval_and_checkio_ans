#include <stdio.h>
#include <string.h>

main(int argc, const char* argv[]) {
	FILE *p = NULL;
	p = fopen(argv[1], "r");
	char msg[200];
	while(fgets(msg, 200, p) != NULL) {
		if (msg) {
			int index = -1;
			int i, j;
			if (msg[strlen(msg) - 1] == '\n') {
				i = strlen(msg) - 2;
				j = strlen(msg) - 3;
			} else {
				i = strlen(msg) - 1;
				j = strlen(msg) - 2;
			}
			
			char wanted_char = msg[i];

			for (; j ; j--) {
				if (wanted_char == msg[j]) {
					index = j;
					break;
				}
			}	
			printf("%d\n", index);
		}
	}
}
