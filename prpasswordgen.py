import string
import random


# VARIABLES
values = string.printable
longitud = 16

# CÓDIGO
for _ in range(5):
    code = random.sample(values, longitud)
    passwd="".join(code)
    print(passwd)

