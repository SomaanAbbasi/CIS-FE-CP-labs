# X = 99
# def func(Y):
#     Z = X + Y
#     return Z
#
# # func(1)
# # print(func(1))
# var = func(1)
# print(var)
#
# var2 = 100
# ans = func(var2)
# print(ans)


x = 88

def func():
    global x
    x = 99

func()
print(x)