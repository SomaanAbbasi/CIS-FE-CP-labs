num = int(input("Enter end limit of series: "))

print(f'Even numbers less than {num}: ')

i = 0

while (2**i) < (num):       #checks if limit reached, continues if not
    print(2**i, end=' ')
    i += 1

