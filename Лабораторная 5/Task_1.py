from pprint import pprint
for num in range(16):
    now_ = [num]
    dict_ = {
        'bin': bin(num),
        'dec': num,
        'hex': hex(num),
        'oct': oct(num)
    }
    pprint(dict_)