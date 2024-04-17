//----- (0000000000401196) ----------------------------------------------------
int sub_401196() {
	char v1;      // [rsp+7h] [rbp-9h]
	FILE *stream; // [rsp+8h] [rbp-8h]

	puts("Congratulations! You've called the win function.");
	stream = fopen("flag.txt", "r");
	if (!stream)
		return puts("Error opening the file.");
	puts("Contents of flag.txt:");
	while (1) {
		v1 = fgetc(stream);
		if (v1 == -1)
			break;
		putchar(v1);
	}
	return fclose(stream);
}

//----- (0000000000401221) ----------------------------------------------------
__int64 sub_401221() {
	char v1[64]; // [rsp+0h] [rbp-40h] BYREF

	setvbuf(stdout, 0LL, 2, 0LL);
	printf("Give me something and shall give you something in return.");
	return gets(v1);
}
