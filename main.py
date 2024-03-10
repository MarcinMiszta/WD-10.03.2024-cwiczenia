# try:
#     a = int(input())
#     b = int(input())
#     result = a/b
#     # print(result)
# # except ZeroDivisionError:
# # except ValueError:
#     # print("wrong value")
# except Exception:
#     print("error")
# else:
#     print(result)
#
# l1 = [1,2,3,4,5,6,7,8,9]
# l2 = []
# for i in l1:
#     l2.append(i**2)
# print(l2)
# l2 = [i**2 for i in l1]
# print(l2)
# l3 = [3**y for y in range(1, 6)]
# print(l3)
# l4 = [x for x in l1 if x % 2 == 1]
# print(l4)
# l5 = [(x, y) for x in l2 for y in l4]
# print(l5)
# l6 = []
# for i in l2:
#     for j in l3:
#         l6.append((i, j))
# print(l6)
#
#

#
from math import *


# def rownanie_kwadratowe(a, b, c):
#     delta = b**2 - 4*a*c
#     if delta < 0:
#         print("Niepoprawne")
#         return 0
#     if delta == 0:
#         print("jeden pierwiastek")
#         x = (-b) / (2*a)
#         return x
#     elif delta > 0:
#         print("dwa pierwiastki")
#         x1 = (-b + sqrt(delta)) / (2*a)
#         x2 = (-b - sqrt(delta)) / (2*a)
#         return x1, x2
#
#
# print(rownanie_kwadratowe(5, 3, 1))
# print(rownanie_kwadratowe(1, 2, 1))
# print(rownanie_kwadratowe(2, 6, 1))


def dlugosc_odcinka(x1=1, x2=2, y1=3, y2=4):
    return sqrt((x1-x2)**2 + (y1-y2)**2)


print(dlugosc_odcinka())
print(dlugosc_odcinka(3, 5, 1, 6))
print(dlugosc_odcinka(y1=3, x1=12, x2=1, y2=6))
print(dlugosc_odcinka(1, 5, y2=1, y1=6))
