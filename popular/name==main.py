# What does if __name__ == "__method__": do?

import test

# 1. Sets a few special variables like __name__
# 2. Execute code in the file

print(__name__)
print("It prints __main__ which is the hard-coded string")
