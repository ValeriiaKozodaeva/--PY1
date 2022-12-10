import random
def get_unique_list_numbers() -> list[int]:
    rand = []
    while len(rand) < 15:
        numb = random.randint(-10,10)
        if numb not in rand:
            rand.append(numb)
    return rand

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
