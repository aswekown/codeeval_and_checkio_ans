#include <stdio.h>
#include <stdlib.h>

size_t FileLength(char *FileName) {
    FILE * f = fopen(FileName, "r");
	if (f == NULL) {
		return -1;
	}
	size_t res;
	if (fseek(f, 0, SEEK_END)) {
		fclose(f);
		return -2;
	}
	res = ftell(f);
	fclose(f);
	return res;
}

int main(int argc, char const *argv[])
{
	printf("%d", FileLength(argv[1]));
	return 0;
}