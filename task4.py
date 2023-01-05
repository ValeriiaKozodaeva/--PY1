import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(filepath, separator_value=',', separator_line='\n') -> list[dict]:
    with open(filepath) as f:
        list_ = []
        for index, line in enumerate(f):
            array = line.strip(separator_line).split(separator_value)
            if index == 0:
                column = array
                continue

            list_.append({})

            for i, _ in enumerate(column):
                list_[-1].update({column[i]: array[i]})
    return list_

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))