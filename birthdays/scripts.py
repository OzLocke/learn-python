import os
from datetime import datetime

class Birthday:
    def __init__(self, birthdate):
        self.birthdate = datetime.strptime(birthdate, '%Y%m%d')
        print(birthdate)

    def age(self):
        return datetime.now().year - \
            self.birthdate.year - \
                ((datetime.now().month, datetime.now().day) < (self.birthdate.month, self.birthdate.day))

    def birthday_dictionary(self):
        bday_dict = {
            "Day": self.birthdate.day,
            "Month": self.birthdate.strftime('%B'),
            "Year": self.birthdate.year
            }
        
        return bday_dict
    
    def day_of_birth(self):
        return self.birthdate.strftime('%A') 

    def same_day_count(self):
        same_day_count = 0
        for y in range(self.birthdate.year, datetime.now().year + 1):
            birthday_that_year = datetime.strptime(str(y) \
                + str(self.birthdate.month) + \
                    str(self.birthdate.day), \
                        '%Y%m%d')
            if birthday_that_year.weekday() == self.birthdate.weekday():
                same_day_count += 1
        
        return same_day_count

class Output:
    def __init__(self, birthdate):
        self.birthdate = birthdate
        birthday_scr_obj = Birthday(birthdate)
        self.age = birthday_scr_obj.age()
        self.day_of_birth = birthday_scr_obj.day_of_birth()
        self.birthday_dictionary = birthday_scr_obj.birthday_dictionary()
        self.same_day_count = birthday_scr_obj.same_day_count()
    
    def output(self):
        print('You are {age} years old'.format(age=self.age))
        print('you were born on {day}, {month}, {year}'.format( \
            day=self.birthday_dictionary["Day"], month=self.birthday_dictionary["Month"], year=self.birthday_dictionary["Year"]) \
            )
        print('You were born on a {day}'.format(day=self.day_of_birth))
        print('Including the day of your birth, your birthday has fallen on a {day} {x} times'.format( \
            day=self.day_of_birth, x=self.same_day_count) \
            )