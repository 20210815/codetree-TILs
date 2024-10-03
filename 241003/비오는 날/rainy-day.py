class Weather:
    def __init__ (self, date, day, wea):
        self.date = date
        self.day = day
        self.wea = wea


n = int(input())

arr = [tuple(input().split()) for _ in range(n)]
guess = [Weather(date, day, wea) for date, day, wea in arr]

target_id = 0
min_date = "2100-00-00"
for i, weat in enumerate(guess):
    if weat.wea == 'Rain':
        if min_date > weat.date:
            min_date = weat.date
            target_id = i

print(f'{guess[target_id].date} {guess[target_id].day} {guess[target_id].wea}')