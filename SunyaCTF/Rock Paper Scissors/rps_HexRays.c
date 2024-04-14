//----- (080491E6) --------------------------------------------------------
int generateComputerChoice() {
	unsigned int v0; // eax

	v0 = time(0);
	srand(v0);
	return rand() % 3;
}

//----- (08049239) --------------------------------------------------------
int __cdecl main(int argc, const char **argv, const char **envp) {
	char s[100];        // [esp+0h] [ebp-7Eh] BYREF
	char v5[2];         // [esp+64h] [ebp-1Ah] BYREF
	int ComputerChoice; // [esp+66h] [ebp-18h]
	char v7;            // [esp+6Dh] [ebp-11h]
	int v8;             // [esp+6Eh] [ebp-10h]
	int v9;             // [esp+72h] [ebp-Ch]
	int *p_argc;        // [esp+76h] [ebp-8h]

	p_argc = &argc;
	setvbuf(stdout, 0, 2, 0);

	v9 = 0;
	v8 = 0;
	v7 = 0;

	puts("Welcome to Rock, Paper, Scissors!");
	printf("Enter your name: ");
	fgets(s, 150, stdin);
	s[strcspn(s, "\n")] = 0;

	while (1) {
		printf("\n%s, choose your move:\n", s);
		puts("1. Rock");
		puts("2. Paper");
		puts("3. Scissors");
		puts("4. Shoot");
		puts("0. Quit");
		printf("Enter your choice: ");

		fgets(v5, 3, stdin);

		v5[0] -= 48;
		if (!v5[0])
			break;
		if (v5[0] > 0 && v5[0] <= 4) {
			ComputerChoice = generateComputerChoice();
			printf("Computer chooses ");
			if (ComputerChoice == 2) {
				puts("Scissors.");
			} else if (ComputerChoice <= 2) {
				if (ComputerChoice) {
					if (ComputerChoice == 1)
						puts("Paper.");
				} else {
					puts("Rock.");
				}
			}
			if (v5[0] == 4) {
				if (v7 == 1) {
					if (flag) {
						puts("You won with devastating damage, and the computer burst and gave you a flag.");
						printf(flag);
						exit(0);
					}
					puts("Contact an administrator, since the flag is not available.");
				} else {
					puts("Only the creator of this program can use the gun.");
				}
			}

			if (v5[0] == 1 && ComputerChoice == 2 || v5[0] == 2 && !ComputerChoice ||
			    v5[0] == 3 && ComputerChoice == 1) {
				puts("Computer wins!");
				++v8;
			} else if (
				v5[0] == 1 && !ComputerChoice || v5[0] == 2 && ComputerChoice == 1 ||
				v5[0] == 3 && ComputerChoice == 2) {
				puts("Player wins!");
				++v9;
			} else {
				puts("It's a tie!");
			}
		} else {
			puts("Invalid choice. Please choose again.");
		}
	}
	printf("Thanks for playing, %s. Final scores:\n", s);
	printf("Player: %d\n", v9);
	printf("Computer: %d\n", v8);
	return 0;
}
