import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(filepath, separator_value=',', separator_line='\n') -> list[dict]:
    with open(filepath) as f:
        f_line = f.readline().strip(separator_line).split(separator_value)
        json_ = [dict(zip(f_line, row.strip(separator_line).split(separator_value))) for row in f]
    return json.dumps(json_, indent=4)

print(csv_to_list_dict(INPUT_FILE))