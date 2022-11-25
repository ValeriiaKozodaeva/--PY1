list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

last, max_last = list_numbers[-1], 0

for i, value in enumerate(list_numbers):
    if value >= max_last:
        max_last = value
        index_max = i

list_numbers[index_max], list_numbers[-1] = last, max_last

print(list_numbers)
