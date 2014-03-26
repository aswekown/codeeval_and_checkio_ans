#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(int argc, char const *argv[])
{
    FILE *f = fopen(argv[1], "r");
	char line[4026];
	while (fscanf(f, "%s", line) != EOF) {
		int sum = 0;
		int i;
		for (i = 0; line[i]; ++i) {
			if (isdigit(line[i])) {
				sum += (line[i] - '0');
			}
		}
		printf("%d\n", sum);
	}
	return 0;
}