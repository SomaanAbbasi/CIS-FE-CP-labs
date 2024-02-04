num = int(input("Enter a number to display Times Table: "))


print(f'Times Table for {num}')
for i in range(1, 11):
    print(f'{num} x {i} = {i*num}')
