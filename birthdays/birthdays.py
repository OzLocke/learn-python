from datetime import datetime

def birthdays(date):
    birthday = datetime.strptime(date, '%Y%m%d')
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    # Need logic to add the letters at the end
    day = birthday.day
    month = birthday.strftime('%B')
    year = birthday.year
    weekday = birthday.strftime('%A')
    age = datetime.now().year - birthday.year - ((datetime.now().month, datetime.now().day) < (birthday.month, birthday.day))

    
    same_day_count = 0
    for y in range(birthday.year, datetime.now().year + 1):
        birthday_that_year = datetime.strptime(str(y) + str(birthday.month) + str(day), '%Y%m%d')
        if birthday_that_year.weekday() == birthday.weekday():
            same_day_count += 1


    return('You are {age}.\n \
            You were born on {day} {month} {year}.\n \
            You were born on a {weekday}.\n \
            Including the day of your birth, your birthday has fallen on a {weekday} {same_day_count} times.' \
            .format(age=age, day=day, month=month, year=year, weekday=weekday, same_day_count=same_day_count)
        )

print(birthdays('19851114'))