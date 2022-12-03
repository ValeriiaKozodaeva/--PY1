def delete(list_, index=None):
    if index != None:
        list_new = list_[:index] + list_[index+1:]
    else:
        list_new = list_[:-1]

    return list_new

print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
