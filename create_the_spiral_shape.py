n = 7 
A = [[0] * n for _ in range(n)]
num = 1
yuqori, pasti, chap, ong = 0, n - 1, 0, n - 1

while num <= n * n:
    for i in range(chap, ong + 1):
        A[yuqori][i] = num
        num += 1
    yuqori += 1

    for i in range(yuqori, pasti + 1):
        A[i][ong] = num
        num += 1
    ong -= 1
    
    for i in range(ong, chap - 1, -1):
        A[pasti][i] = num
        num += 1
    pasti -= 1
    
    for i in range(pasti, yuqori - 1, -1):
        A[i][chap] = num
        num += 1
    chap += 1

for row in A:
    print("\t".join(map(str, row)))
