#define _GNU_SOURCE
#include <stdio.h>
#include <stdarg.h>
#include <stdlib.h>
#include <limits.h>
#include <errno.h>
#include <math.h>

static void die(const char *fmt, ...)
{
	va_list argp;
	va_start(argp, fmt);
	vfprintf(stderr, fmt, argp);
	va_end(argp);
	fputc('\n', stderr);
	exit(1);
}

static unsigned long get_num(const char *str)
{
	char *end, c;
	unsigned long val;

	if (!str)
		return 0;
	val = strtoul(str, &end, 0);
	if (!val || val == ULONG_MAX)
		return 0;
	while ((c = *end++) != 0) {
		switch (c) {
		case 'k':
			val <<= 10;
			break;
		case 'M':
			val <<= 20;
			break;
		case 'G':
			val <<= 30;
			break;
		default:
			return 0;
		}
	}
	return val;
}

int read_wavfile(const char *name, char **wavdata)
{
	FILE *fp = fopen(name, "rb");
	if (fp == NULL)
		die("file not available: %s", name);

	fseeko64(fp, 0, SEEK_END);

	size_t file_sz = ftello64(fp);
	printf("file size: %ld\n", file_sz);

	char *pdata = calloc(sizeof(char), file_sz);
	if (pdata == NULL)
		die("memory allocation failure");

	fseeko64(fp, 0, SEEK_SET);

	if (file_sz != fread(pdata, 1, file_sz, fp))
		die("file read error");

	if (fp) {
		fclose(fp);
		fp = NULL;
	}

	*wavdata = pdata;

	return EXIT_SUCCESS;
}

int main(int argc, char **argv)
{
	const char *arg;
	char *wavfile = NULL;
	char *wavdata = NULL;

	while ((arg = argv[1]) != NULL) {
		if (*arg != '-')
			break;
		for (;;) {
			switch (*++arg) {
			case 0:
				break;
			case 'i':
				wavfile = argv[2];
				continue;
			default:
				die("Unknown flag '%s'", arg);
			}
			break;
		}
		argv++;
	}

	if (wavfile == NULL)
		die("bad arguments: test-wav [-i] <wavfile>");

	printf("processing: %s\n", wavfile);

	if (read_wavfile(wavfile, &wavdata) != EXIT_SUCCESS)
		die("read wave file error");

	if (wavdata) {
		free(wavdata);
		wavdata = NULL;
	}

	return 0;
}
