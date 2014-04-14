#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
typedef uint32_t  u32;

int main(int argc, char const *argv[])
{
	u32 i = 0;
	u32 B = 0, F = 0, number = 0;
	FILE *p = NULL;
	if (( p = fopen(argv[1], "r")) == NULL) {
		exit(1);
	}
	while (fscanf(p, "%d %d %d", &F, &B, &number) == 3) {
		// printf("%d %d %d\n\n", F, B, number);
		for (i = 1; i < number; ++i) {
			if (i % F == 0 && i % B == 0) {
				printf("FB ");
			} else if (i % B == 0) {
				printf("B ");
			} else if (i % F == 0) {
				printf("F ");
			} else {
				printf("%d ", i);
			}
		}
		if (number % B == 0 && number % F == 0) {
			printf("FB\n");
		} else if (number % B == 0) {
			printf("B\n");
		} else if (number % F == 0) {
			printf("F\n");
		} else {
			printf("%d\n", number);
		}
	}
	fclose(p);
	return 0;
}
