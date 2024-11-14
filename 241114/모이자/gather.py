n = int(input())

people = list(map(int, input().split()))

goto = 0
min_sum = 999
for i in range(n):
    # 내가 가려는 집이 i 라면 
    goto = i
    # 이동 거리를 구해서

    
    result = 0
        # 현재 집에서부터 - i 까지의 이동 거리
    for j in range(n):
       result += abs(j - i) * people[j]
    # 최소를 구함
    min_sum = min(result, min_sum)

print(min_sum)