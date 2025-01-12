ability = list(map(int, input().split()))

# Write your code here!
people = [False] * 6
result = 100000
ability.sort()

teamA = ability[0]+ ability[-1]
teamB = ability[1]+ ability[-2]
teamC = ability[2]+ ability[-3]

result = max(teamA, teamB, teamC) - min(teamA, teamB, teamC)

print(result)