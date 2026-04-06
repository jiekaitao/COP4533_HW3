def parse_input(input_str: str) -> tuple[int, str, str, dict[str, int]]:
    lines = input_str.split("\n")
    K = int(lines[0])

    str_dict = {}
    for i in range(1, len(lines)-2):
        temp_row = lines[i].split(" ")
        str_dict[temp_row[0]] = int(temp_row[1])
    
    A = lines[K-1]
    B = lines[K]

    return K, A, B, str_dict



def main(input_str: str) -> tuple[int, str]:
    K, A, B, str_dict = parse_input(input_str)
    # build 2d table where each entry (i,j) is the maximal value of the subsequence that would be realized upon using the first 
    # i characters of A and the first j characters of B
    table = []
    for i in range(len(A) + 1):
        row = []
        for j in range(len(B) + 1):
            row.append(0)
        table.append(row)

    # # base case: both strings are empty
    # for i in range(len(A) + 1):
    #     table[i][0] = 0
    
    # for j in range(len(B) + 1):
    #     table[0][j] = 0
    
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                table[i+1][j+1] = table[i][j] + str_dict[A[i]] # one indexed because of the base cases
            else:
                table[i+1][j+1] = max(table[i][j+1], table[i+1][j])
        

            





