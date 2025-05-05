# CARLOS ALBERTO DE LA ROSA CANEPA 2152203
# https://usaco.org/index.php?page=viewproblem2&cpid=1276&lang=es

import sys
from pathlib import Path

base_path = Path(__file__).parent
input_path = base_path / "three_logos.in"
output_path = base_path / "three_logos.out"

sys.stdin = open(input_path, "r")
sys.stdout = open(output_path, "w")


def generate_permutations(items):
    # generar todas las permutaciones para 3 items
    a, b, c = items
    return [
        [a, b, c],
        [a, c, b],
        [b, a, c],
        [b, c, a],
        [c, a, b],
        [c, b, a],
    ]


def generate_orientations():
    # generar orientaciones para 3 items
    return [
        [False, False, False],
        [False, False, True],
        [False, True, False],
        [False, True, True],
        [True, False, False],
        [True, False, True],
        [True, True, False],
        [True, True, True],
    ]


# intentar llenar los rectangulos
def try_fill_square(rects):
    for perm in generate_permutations([(0, "A"), (1, "B"), (2, "C")]):
        for orientations in generate_orientations():
            dims = []
            for (i, ch), rotate in zip(perm, orientations):
                x, y = rects[i]
                if rotate:
                    x, y = y, x
                dims.append((x, y, ch))

            # caso 1
            w = max(d[0] for d in dims)
            h = sum(d[1] for d in dims)
            if w == h:
                n = w
                grid = [[""] * n for _ in range(n)]
                y_offset = 0
                for dx, dy, ch in dims:
                    for i in range(y_offset, y_offset + dy):
                        grid[i][:dx] = [ch] * dx
                    y_offset += dy
                return n, grid

            # caso 2
            h = max(d[1] for d in dims)
            w = sum(d[0] for d in dims)
            if w == h:
                n = h
                grid = [[""] * n for _ in range(n)]
                x_offset = 0
                for dx, dy, ch in dims:
                    for i in range(dy):
                        grid[i][x_offset : x_offset + dx] = [ch] * dx
                    x_offset += dx
                return n, grid

            # caso 3
            a, b, c = dims
            if b[1] == c[1] and a[0] == max(b[0] + c[0], a[0]) and a[1] + b[1] == a[0]:
                n = a[0]
                grid = [[""] * n for _ in range(n)]
                for i in range(a[1]):
                    grid[i][: a[0]] = [a[2]] * a[0]
                for i in range(b[1]):
                    grid[a[1] + i][: b[0]] = [b[2]] * b[0]
                    grid[a[1] + i][b[0] : b[0] + c[0]] = [c[2]] * c[0]
                return n, grid

    return -1, None


x1, y1, x2, y2, x3, y3 = map(int, input().split())
rects = [(x1, y1), (x2, y2), (x3, y3)]

n, grid = try_fill_square(rects)

if n == -1:
    print(-1)
else:
    print(n)
    for row in grid:
        print("".join(row))

# fin
