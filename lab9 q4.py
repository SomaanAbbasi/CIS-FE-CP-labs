
import math

def out_circle(r1, r2):

    area = math.pi * (r1**2)

    def in_circle(r2):
        circ = 2 * math.pi * r2
        return circ

    if r2 < r1:
        circ = in_circle(r2)

    return area, circ



r1= int(input("Enter radius of outer circle: "))
r2 = int(input("Enter radius of inner circle: "))

print(f'Area of outer circle= {out_circle(r1, r2)[0]}')

print(f'Circumference of inner circle = {out_circle(r1, r2)[1]}')





