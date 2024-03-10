zakupy = {'chleb': 'sztuki', 'ser': 'kg', 'mleko': 'litry'}
zakupy2 = {key: value for key, value in zakupy.items() if value == 'sztuki'}
print(zakupy2)