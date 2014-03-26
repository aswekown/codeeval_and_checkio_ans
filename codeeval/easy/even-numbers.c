#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    FILE *f = fopen(argv[1], "r");
	int num = 0;
	while (fscanf(f, "%d", &num) != EOF) {
		printf("%d\n", ((num & 1) == 0));
	}
	return 0;
}