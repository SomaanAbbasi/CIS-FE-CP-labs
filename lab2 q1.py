
print(f'Enter the coefficients of a quadratic equation in the form ax² + bx + c')
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))


x1 = (-(b) + (((b**2) - (4*a*c) ))**0.5)/(2*a)

x2 = (-(b) - (((b**2) - (4*a*c) ))**0.5)/(2*a)



print(f'The roots of the given quadratic are: \n{round(x1,3)} and {round(x2, 3)}')