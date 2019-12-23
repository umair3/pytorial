x = 2
print(x == 2)
print(x == 3)
print(x <= 2)

if x == 2:
    print("x is 2.")

print(True)
print(not True)

if not x == 3:
    print("x is not equal to 3")

y = 2
y += 1
print(x is y)  # checks if it is same instance
print(id(x))
print(id(y))

a = [1,2,3]
b = [1,2,3]
print(a == b)  # true
print(a is b)  # false

