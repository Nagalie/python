eingabe = input("wie groß soll ihr weihnachtsbaum sein?: ")

for i in range(1, int(eingabe) + 1, 2):
    print(f"{' ' * int(eingabe)}{'*' * i}")