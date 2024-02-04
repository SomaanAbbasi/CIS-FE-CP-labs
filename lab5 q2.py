n = int(input("Enter number of lines with max stars: "))

for i in range(1,n+1):
    print("*" * i)

for i in range(n, 0, -1):
    print("*" * i)
