#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    FILE *f = fopen(argv[1], "r");
	int num = 0;
	int sum = 0;
	while (fscanf(f, "%d", &num) != EOF) {
		sum += num;
	}
	printf("%d\n", sum);
	return 0;
}