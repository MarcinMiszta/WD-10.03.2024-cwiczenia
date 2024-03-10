def spr(a,b,c):
    if (a**2 + b**2 == c**2) | (a**2 + c**2 == b**2) | (b**2+c**2 == a**2):
        print('trojkąt jest prostokątny')
        return 1
    else:
        print('trojkąt nie jest prostokątny')
        return 0
print(spr(3,4,5))