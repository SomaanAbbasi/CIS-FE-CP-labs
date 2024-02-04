
import math

def out_circle():

    def in_circle():
        circumference = 2 * math.pi * r2
        return circumference

    if r2 < r1:
        circumference = in_circle()

    area = math.pi * (r1 ** 2)




    print(f'Area of outer circle= {area} ')
    print(f'Circumference of inner circle = {circumference}')

r1= int(input("Enter radius of outer circle: "))    #global variable
r2 = int(input("Enter radius of inner circle: "))

out_circle()

# print(f'Area of outer circle= {out_circle(r1, r2)[0]}')
#
# print(f'Circumference of inner circle = {out_circle(r1, r2)[1]}')





