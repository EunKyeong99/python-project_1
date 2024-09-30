N = int(input("지뢰찾기 게임을 위한 NxN의 N 값을 입력하세요: "))

minefield = [list(map(int, input(f"{i + 1}번째 행 (공백으로 구분): ").split())) for i in range(N)]

result = [['0' for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if minefield[i][j] == 1:
            result[i][j] = '*'
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if di == 0 and dj == 0:
                        continue
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N:
                        if result[ni][nj] != '*':
                            result[ni][nj] = str(int(result[ni][nj]) + 1)

print("\n지뢰찾기 결과:")
for row in result:
    print(' '.join(row))
