# CARLOS ALBERTO DE LA ROSA CANEPA 2152203
# https://usaco.org/index.php?page=viewproblem2&cpid=1011

import sys
from pathlib import Path

base_path = Path(__file__).parent
input_path = base_path / "triangles.in"
output_path = base_path / "triangles.out"

sys.stdin = open(input_path, "r")
sys.stdout = open(output_path, "w")

n = int(input())
coords = []

for i in range(n):
    item = list(map(int, input().split()))
    coords.append(item)

area = 0

for a in coords:
    for b in coords:
        for c in coords:
            # Verifica si es triángulo rectángulo
            if a[0] == b[0] and a[1] == c[1]:
                base = abs(a[0] - c[0])
                height = abs(a[1] - b[1])
                # El problema nos pide el doble del área del triángulo
                area = max(area, base * height)

print(area)
