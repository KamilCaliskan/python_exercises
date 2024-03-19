import calendar

days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

month, day, year = map(int, input().split())

day_index = calendar.weekday(year, month, day)

print(days[day_index])
