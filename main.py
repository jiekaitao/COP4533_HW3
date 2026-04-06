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

def score_subsequence(A_sub: str, B_sub: str, str_dict = dict[str, str]) -> int:
   for i in A_sub:
       for j in B_sub:
           if 



def main(input_str: str) -> tuple[int, str]:
    K, A, B, str_dict = parse_input(input_str)
    # build 2d table where each entry (i,j) is the maximal value of the subsequence that would be realized upon using the first 
    # i characters of A and the first j characters of B

    table = [[]]
    for i in range(len(A)):
        for j in range(len(B)):
            score_subsequence(A[:i], B[:j])



