#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(int argc, char const *argv[])
{
	FILE *f = NULL;
	f = fopen(argv[1], "r");
	char line[4026];
	int i = 0;
	while (fgets(line, 4026, f) != NULL) {
		// puts(line);
		int none = 1;
		for (i = 0; line[i]; ++i) {
			if (isdigit(line[i])) {
				none = 0;
				printf("%c", line[i]);
			} else if (islower(line[i]) && (line[i] <= 'j')) {
				none = 0;
				printf("%d", line[i] - 'a');
			}
		}
		if (none) {
			puts("NONE");
		} else {
			printf("\n");
		}

	}
	return 0;
}
