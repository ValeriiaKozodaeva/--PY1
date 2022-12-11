from string import ascii_uppercase, ascii_lowercase, digits
import random
def get_random_password(quantity) -> str:
    symbols = ascii_uppercase + ascii_lowercase + digits
    return random.sample(symbols, quantity)

print(get_random_password(8))
