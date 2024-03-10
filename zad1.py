A = {1-key: key for key in range(1, 10)}
print(A)
B = sorted({4**i for i in range(0, 8)})
print(B)
C = sorted({x for x in B if x % 2 == 0})
print(C)
