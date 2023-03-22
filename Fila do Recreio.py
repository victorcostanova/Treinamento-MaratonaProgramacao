
n = int(input())
for x in range(n):
    m = int(input())
    p = list(map(int, input().split()))
    psorted = sorted(p, reverse=True)
    alunos = 0
    for i in range(len(p)):
        if p[i] == psorted[i]:
            alunos += 1
    print(alunos)


