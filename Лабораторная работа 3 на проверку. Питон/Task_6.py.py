list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

maksim_posledniy = 0
for i in range(len(list_numbers)):
    if list_numbers[i] >= maksim_posledniy:
        maksim_posledniy = list_numbers[i]
        index_maksima = i

a = list_numbers[-1]
list_numbers[-1] = maksim_posledniy
list_numbers[index_maksima] = a

print(list_numbers)
