def parse_input(input_str: str) -> tuple[int, str, str, dict[str, int]]:
    lines = input_str.split("\n")
    K = int(lines[0])

    str_dict = {}
    for i in range(1, len(lines)-2):
        temp_row = lines[i].split(" ")
        str_dict[temp_row[0]] = int(temp_row[1])
    
    A = lines[-2]
    B = lines[-1]

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

    # now backtrack
    i_ptr = len(A)
    j_ptr = len(B)
    max_value = table[len(A)][len(B)] # just the bottom right value because it represents using all of A and all of B

    subsequence = ""

    while((i_ptr != 0) and (j_ptr != 0)):
        if(A[i_ptr-1] == B[j_ptr-1]):
            subsequence += A[i_ptr-1]
            i_ptr -= 1
            j_ptr -= 1
        else:
            if (table[i_ptr-1][j_ptr] > table[i_ptr][j_ptr-1]):
                # the cell above is better than the one on the left
                i_ptr -= 1
            else:
                j_ptr -= 1

    return max_value, subsequence[::-1]
        

            





