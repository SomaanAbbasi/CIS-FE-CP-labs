list =  input("Enter a bunch of numbers, seperated by spaces: ")

list = list.split() #this removes the spaces, and puts each num in a list

largest = int(list[0])  #assuming first element to be largest

for num in list:
    if int(num) > largest:      #comparing each element to largest
        largest = int(num)

print(f'Largest number in the given numbers: {largest}')

