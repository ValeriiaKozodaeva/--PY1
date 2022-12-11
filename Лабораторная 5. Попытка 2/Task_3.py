import random
def get_unique_list_numbers(start_, finish_, count_) -> list[int]:
    rand = []
    while len(rand) < count_:
        numb = random.randint(start_, finish_)
        if numb not in rand:
            rand.append(numb)
    return rand

list_unique_numbers = get_unique_list_numbers(-10, 10, 15)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
