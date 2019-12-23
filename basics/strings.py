name = "umaiR anwar"
age = 31
print("Hello %s, age = %d" % (name, age))
print('Hello %s, age = %d' % (name, age))

data = ("Umair",  31)
print("Name = %s, Age = %d" % data)


print(len(name))
print(name.index('a'))
print(name.count('t'))  # find occurrences

print(name.capitalize())  # capitalize fist letter, and other are small
print(name.casefold())  # case-less comparison
print(name.zfill(15))  # fills with zeros
print(name.upper())
print(name.lower())


print(name.split(' '))

