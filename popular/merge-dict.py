# How to merge two dictionaries in a single expression?

x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

# Merging by overwriting values from x by y
z = {**x, **y}

print(z)

# check the order
print({**y, **x})

# https://stackoverflow.com/questions/38987/how-do-i-merge-two-dictionaries-in-a-single-expression
