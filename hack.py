from random import choice
from string import ascii_lowercase, digits

chars = ascii_lowercase + digits
lst = [''.join(choice(chars) for _ in range(32)) for _ in range(1000000000000000)]
print(lst)