from pprint import pprint
pprint([{'bin':bin(num), 'dec':num, 'hex':hex(num), 'oct':oct(num)} for num in range(16)])
