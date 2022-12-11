from string import ascii_uppercase, ascii_lowercase, digits
import random
s = ascii_uppercase + ascii_lowercase + digits
def get_random_password(n) -> str:
    return random.sample(s, n)

print(get_random_password(8))
