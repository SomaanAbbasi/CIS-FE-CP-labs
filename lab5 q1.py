string_1 = input("Enter a string: ")
string_2 = input("Enter another string: ")

for ch in string_1:

    if ch in string_2:
        print("Common: ", ch)   #prints the common character if found in both strings

    else:
        print("Uncommon:", ch)  #if not found, prints it as "Uncommon"