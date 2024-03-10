zakupy = {'chleb': 'sztuki', 'ser': 'kg', 'mleko': 'litry'}
zakupy2 = [key for key, value in zakupy.items() if value == 'sztuki']
print(zakupy2)