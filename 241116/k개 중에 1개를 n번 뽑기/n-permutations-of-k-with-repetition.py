K, N = tuple(map(int, input().split()))

answer = []

def printAnswer():
    for i in range(N):
        print(answer[i], end=" ")
    print()

def C(num):
    if num == N+1:
        printAnswer()
        return
    
    for i in range(1, K+1):
        answer.append(i)
        C(num+1)
        answer.pop()

C(1)
