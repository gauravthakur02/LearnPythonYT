from my_package import module1

from my_package import module2

arear = module2.rectangle(4, 3)

areas = module2.square(4)

add = module1.add(2, 3)
sub = module1.subs(4, 2)
multi = module1.multi(3, 4)
div = module1.div(5, 3)

print(f"Area of rectange (l=4, b=3): {arear}")
print(f"Area of square (l=4): {areas}")
print(f"Addition: {add}")
print(f"Substraction: {sub}")
print(f"Multiply: {multi}")
print(f"Division: {div}")

print(f"Value of PI: {module2.pi}")
