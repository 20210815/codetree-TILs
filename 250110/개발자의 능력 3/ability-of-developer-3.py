abilities = list(map(int, input().split()))

# Write your code here!
checkMember = [False] * 6

result = 1000000
for i in range(6-2):
    for j in range(i+1, 6-1):
        for k in range(j+1, 6):
            checkMember[i] = True
            checkMember[j] = True
            checkMember[k] = True
            teamSum = 0
            teamSum = abilities[i] + abilities[j] + abilities[k]
# 팀 만들기
            anotherTeam = 0
# 팀 비교하기
            for h in range(len(abilities)):
                if checkMember[h] == False:
                    anotherTeam += abilities[h]
            
            if abs(teamSum - anotherTeam) < result:
                result = abs(teamSum - anotherTeam)
            anotherTeam = 0
            teamSum = 0
            checkMember[i] = False
            checkMember[j] = False
            checkMember[k] = False

# 가장 최소 찾기
print(result)

