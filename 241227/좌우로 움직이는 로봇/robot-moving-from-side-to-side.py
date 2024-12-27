OFFSET = 10
MAX = 20

n, m = tuple(map(int, input().split()))

timeList = []
timeListB = []
time = 0
Agps = OFFSET

for i in range(n):
    t, d = input().split()
    t = int(t)

    #내가 이동할 때
    if d == 'L':
        #왼쪽으로 이동할 때, 시간에 (위치, 누구)
        for count in range(t):
            Agps-=1
            timeList.append(Agps)
    else:
        for count in range(t):
            Agps+=1
            timeList.append(Agps)

    time += t


Bgps = OFFSET
time = 0
for i in range(m):
    t, d = input().split()
    t = int(t)

    #내가 이동할 때
    if d == 'L':
        #왼쪽으로 이동할 때, 시간에 (위치, 누구)
        for count in range(t):
            Bgps-=1
            timeListB.append(Bgps)
    else:
        for count in range(t):
            Bgps+=1
            timeListB.append(Bgps)

    time += t


countResult = 0
#시간 안에
for index in range(min(len(timeList), len(timeListB))):
    if timeList[index] == timeListB[index] and index != 0:
        #이전 확인
        if timeList[index-1] != timeListB[index-1]:
            countResult += 1


#혼자 돌고 있을 때
for index in range(max(len(timeList), len(timeListB)) - min(len(timeList), len(timeListB))):
    if len(timeList) > len(timeListB): # A가 더 큰 리스트일 때는 A가 돌면서 B랑 같아지는지 봐야 함
        if timeList[index+len(timeListB)] == timeListB[-1]:
            countResult += 1
    else:
        if timeListB[index+len(timeList)] == timeList[-1]:
            countResult += 1

print(countResult)