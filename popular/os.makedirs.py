# Create nested directory safely?

import os

directory = "test-dir"

if not os.path.exists(directory):
    os.makedirs(directory)

# In Python 3.3+

try:
    os.makedirs(directory)
except FileExistsError:
    # directory already exists
    pass

# or
print(os.makedirs(directory, exist_ok=True))

print(123)

# https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory