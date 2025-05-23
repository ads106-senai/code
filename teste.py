num = int(input("Numero"))
primo = True

for x in range(2, num-1):
    if (num % x == 0):
        primo = False

if (primo)
    print("Primo")
else:
    print("Não Primo")
