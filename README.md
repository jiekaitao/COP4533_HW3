COP 4533 - Assignment 3: Highest Value Longest Common Subsequence

Student: Jie Tao
UFID: 51630537

# Question 1

How to Run:

```
python3 Q1.py
```
This generates input/output files and a runtime graph.

To run the algorithm on any input file:
```
python3 -c "from main import main; f=open('YOUR_FILE.txt'); v,s=main(f.read()); print(v); print(s); f.close()"
```

Input format is as the homework specified:

```
K
x1 v1
x2 v2
...
xK vK
A
B
```

- K = number of characters in the alphabet
- Each of the next K lines has a character and its value
- A = first string
- B = second string

Output format just returns the max_value (string) and optimal_subsequence (string).

The runtime vs string lengths graph is located in outputs/runtime_over_str_len.png. The example inputs are in ./inputs/ and the corresponding outputs are in ./outputs.

Requirements / Assumptions:

  - Python 3.10+
  - matplotlib is required for Q1 graphing

# Question 2
Let OPT[i][j] be the maximum value of any common subsequence using the first i characters of A and the first j characters of B. Let str_dict be the mapping from the characters to their respective values.

In the base case, the first column and the first row are all 0. More specifically,
```
OPT[i][0] = 0 for all i
OPT[0][j] = 0 for all j

If A[i] == B[j]: OPT[i][j] = OPT[i-1][j-1] + str_dict[A[i]]

If A[i] != B[j]: OPT[i][j] = max(OPT[i-1][j], OPT[i][j-1])
```

This is correct because when the characters match, including that character to the existing best subsequence is how we reach the maximum value at that respective recursive depth. When they don't match, there exists at least one character that can't be part of the optimal subsequence, so we choose whichever neighboring subproblem gives the better value. 

# Question 3
```
HVLCS(A, B, str_dict):
    n = length(A)
    m = length(B)
    create zero matrix of size (n+1) * (m+1)
    for i from 1 to n:
        for j from 1 to m:
            if A[i] == B[j]:
                table[i][j] = table[i-1][j-1] + str_dict[A[i]]
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    return table[n][m]
```

The runtime is O(nm) because there are two nested loops. The outer loop iterates from 1 to n and the inner loop iterates from 1 to m. The actual table operations (array accessing and insertion) just take O(1) time.