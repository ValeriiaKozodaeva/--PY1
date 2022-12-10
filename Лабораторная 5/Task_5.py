def get_random_password(n) -> str:
    import string
    alph_upp = string.ascii_uppercase
    alpha_low = string.ascii_lowercase
    numb = string.digits
    s = alpha_low + alph_upp + numb
    import random
    passw = random.sample(s, n)
    return passw

print(get_random_password(8))
