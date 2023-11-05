
password_accepted = False
password = input("Enter a password: ")


if 7 <= len(password) <= 15:

    if '0' in password or '1' in password or '2' in password or'3'in password or'4' in password or '5' in password or '6' in password or '7'in password or'8'in password or'9' in password:

        if '!' in password or '?' in password or '$' in password or '-' in password or '_' in password:

            password_accepted = True

if password_accepted == True:
    print("Password Accepted.")

else: print("""
Invalid Password.
Password must be alpha-numeric and contain atleast 1 special character from ( ! ? $ - _ )""")