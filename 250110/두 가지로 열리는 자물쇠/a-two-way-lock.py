N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())


def checkDistance(i, j, k):
    if (abs(a1-i) % N <= 2) or ((a1+i) % N <= 2):
        if (abs(b1-j) % N <= 2) or ((b1+j) % N <= 2):
            if (abs(c1-k) % N <= 2) or ((c1+k) % N <= 2):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def checkDistance2(i, j, k):
    if (abs(a2-i) % N <= 2) or ((a2+i) % N <= 2):
        if (abs(b2-j) % N <= 2) or ((b2+j) % N <= 2):
            if (abs(c2-k) % N <= 2) or ((c2+k) % N <= 2):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
        

# Write your code here!
#비밀번호 만들기
result = 0
number1 = []
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            if i == j or i == k or j == k:
                continue
            result1 = checkDistance(i, j, k)
            result2 = checkDistance2(i, j, k)
            if result1 or result2:
                #print(i,j,k)
                result += 1

print(result)

# 거리 차이 알아내기
 # n~1이 인접 (mod) 방향 중 작은 거에 대해서 2 이내인지 비교
    # 시계 방향 (조합 + 비밀번호) % 9
    # 반시계 방향 (9 %(비밀번호-조합)