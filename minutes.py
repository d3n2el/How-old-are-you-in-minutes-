from datetime import datetime, timedelta,date
import re
import inflect
import sys
p=inflect.engine()
class Date:
    def __init__(self, time=None):
        self.time = time if time else date.today()

    def __sub__(self, other):
        timediff = self.time - other.time
        return timediff.days * 24 * 60 + timediff.seconds // 60
    def __str__(self):
        return f"{self.time}"

def main():
    print(get_date(input("Date of birth: ")))

def get_date(t):
    # need to elaborate input and split it
    time = re.search(r"([0-9]{4})-([0-9]{2})-([0-9]{2})", t)
    if time == None:
        sys.exit("Invalid input")
    year,month,day = time.groups()
    #validate input through date module
    try:
        date_= date.today()
        year= int(year)
        month= int(month)
        day = int(day)
        birth_date = Date(date(year, month, day))
        today = Date(date_)
        minutes_diff = today - birth_date
    except ValueError as e:
        sys.exit(f"{e}: Invalid Date")
    else:
        return f"{p.number_to_words(minutes_diff, andword="")} minutes".capitalize()







...


if __name__ == "__main__":
    main()
