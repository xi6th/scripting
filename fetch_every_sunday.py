import datetime
today = datetime.date.today()
next_monday = today - datetime.timedelta(days=-today.weekday(), weeks=1)
print(next_monday)
