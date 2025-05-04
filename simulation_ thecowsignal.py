# CARLOS ALBERTO DE LA ROSA CANEPA 2152203
# https://usaco.org/index.php?page=viewproblem2&cpid=665&lang=es
input='''5 4 2
XXX.
X..X
XXX.
X..X
XXX.
'''

lines = input.splitlines()

[first, *rest] = lines

[m,n,k] = map(int, first.split())

output = [
    ''.join(char * k for char in line)
    for line in rest
    for _ in range(k)
]

result = '\n'.join(output) + '\n'
print(result)