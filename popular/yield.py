# What is Yield keyword used for?

# 1. Understand iterables.
# 2. Generators.
# 3. Then, yield.

list1 = [1, 2, 3, 4]
for i in list1:
    print(i)

print(list1)

gen1 = (x*x for x in range(3))

print(gen1)

for i in gen1:
    print(i)


def create_generator():
    list2 = range(3)
    for i in list2:
        yield i*i


gen2 = create_generator()
print(gen2)

for i in gen2:
    print(i)