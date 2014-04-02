#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
  FILE *p = fopen(argv[1], "r");
	int a, b;
	int res = 0;
	while(fscanf(p, "%d,%d", &a, &b) != EOF) {
		res = a - (a / b)*b;
		printf("%d\n", res);
	}
	return 0;
}
