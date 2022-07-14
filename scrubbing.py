

from hashlib import new
import string


valid = [">", "<", ".", ",", "+", "-", "[", "]"]

code = "abcdse><"

newlist = str([x for x in code if x in valid])

print(newlist)

