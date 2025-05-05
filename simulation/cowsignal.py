# CARLOS ALBERTO DE LA ROSA CANEPA 2152203
# https://usaco.org/index.php?page=viewproblem2&cpid=665&lang=es

import sys
from pathlib import Path

base_path = Path(__file__).parent
input_path = base_path / "cowsignal.in"
output_path = base_path / "cowsignal.out"

sys.stdin = open(input_path, "r")
sys.stdout = open(output_path, "w")

first = input()
m, n, k = map(int, first.split())

rest = [input().strip() for _ in range(m)]

for line in rest:
    scaled_horizontal = "".join(char * k for char in line)
    for _ in range(k):
        print(scaled_horizontal)
