from datetime import time

a = time()
b = time(11, 34, 56)
c = time(hour=11, minute=34, second=56)
d = time(11, 34, 56, 234566)

print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)
