def parse_input(input_str: str) -> tuple[int, str, str, dict[str, str]]:
    lines = input_str.split("\n")
    K = int(lines[0])

    str_dict = {}
    for i in range(1, K-2):
        temp_row = lines[i].split(" ")
        str_dict[temp_row[0]] = temp_row[1]
    
    A = lines[K-1]
    B = lines[K]

    return K, A, B, str_dict
