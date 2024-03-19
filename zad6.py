def funkcja(a=1,b=4,ile=10):
    iloczyn = a
    for x in range(ile):
        iloczyn *= b
    return iloczyn


print(funkcja())
