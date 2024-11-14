A = input()

result = 0
for i in range(len(A)):
    # 대신 먼저 고른 게 열린 괄호여야ㅑ 함
    if A[i] == '(': 
        for j in range(i, len(A)):
        # 1번과
        # 2 3 4 5 6번
        # 2번과
        # 3 4 5 6 번        
            if A[j] == ')':
                result += 1


print(result)