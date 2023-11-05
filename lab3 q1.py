num = int(input("Enter a number: "))

if num < 0:
    quit()

elif (num % 2) == 0:
    print(f'{num} is even.')

else:
    print(f'{num} is odd.')