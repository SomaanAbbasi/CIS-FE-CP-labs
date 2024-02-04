
id = int(input("Enter your id: "))

while True:

    print("""
Main Menu
**********
1. Deposit Money
2. Withdraw Amount
3. Login as Different User
Select your choice.
""")
    choice = input()
    money = int(input("Enter amount: "))
    print("Transaction Completed.")

    confirmation = input("Do you want to continue? [Y/y]")

    if confirmation == 'y' or confirmation == 'Y':
        continue

    else:
        break