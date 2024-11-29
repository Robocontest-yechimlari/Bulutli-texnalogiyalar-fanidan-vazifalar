n = 7
A = [[0] * n for _ in range(n)]

nomber = 1
x, y = n // 2, n // 2

dx, dy = 0, -1
qadam = 1

while nomber <= n * n:
    for _ in range(2):
        for _ in range(qadam):
            if 0 <= x < n and 0 <= y < n:
                A[x][y] = nomber
                nomber += 1
            x += dx
            y += dy

        dx, dy = -dy, dx

    qadam += 1

for row in A:
    print("\t".join(map(str, row)))