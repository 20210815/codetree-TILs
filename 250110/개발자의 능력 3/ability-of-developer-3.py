abilities = list(map(int, input().split()))

# Write your code here!
checkMember = [False] * len(abilities)

result = 1000000
for i in range(len(abilities)):
    for j in range(len(abilities)):
        for k in range(len(abilities)):
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

# 가장 최소 찾기
print(result)

