# N명의 개발자
# 악수 횟수: T번
# 악수 걸리는 시간 t: x-y 끼리
# K번만 전염병을 옮김


N, K, P, T = tuple(map(int, input().split()))

time = []
developer = [0] * N

#최초 감염자
developer[P-1] = 1 # 감염자 파악
desease = [0] * N
desease[P-1] = K # 숫자 세는 거

for i in range(T):
    t, x, y = tuple(map(int, input().split()))
    time.append((t,x,y))

time.sort()

for t, x, y in time:
    #둘 다 감염자라면?
    if (developer[y-1] == 1 and desease[y-1] > 0) and (developer[x-1] == 1 and desease[x-1] > 0):
        desease[x-1]-=1
        desease[y-1]-=1

    # x가 감염자라면 그리고 감염시키는 횟수도 남아있다면
    elif (developer[x-1] == 1 and desease[x-1] > 0):
        if developer[y-1] != 1:
            developer[y-1] = 1
            desease[y-1] = K
            desease[x-1] -= 1
    #y가 감염자라면
    elif (developer[y-1] == 1 and desease[y-1] > 0):
        if developer[y-1] != 1:
            developer[x-1] = 1
            desease[x-1] = K
            desease[y-1] -= 1


print(*developer, sep='')