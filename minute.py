from datetime import datetime, timedelta,date
import re
class Date:
    date_ = date.today
    def __init__(self, time):
        self.time = time
    def __sub__(self):
        timedelta(date_, time)


def main():
    print(convert(input("Date of birth: ")))

def convert(t):
    # need to elaborate input and split it
    time = re.search(r"([0-9]{4})-([0-9]{2})-([0-9]{2})", t)
    year,month,day = time.groups()
    #validate input through date module
    try:
        year= int(year)
        month= int(month)
        day = int(day)
        d = date(year,month,day)
        return Date(d)
    except ValueError as e:
        return f"{e}: Invalid Date"


    # If no exception is raised, the format is correct
    # Handle the error if the format is incorrect
    #if not valid,raise valueError
    #else: pass the data to Data
    #now i need to understand where i use inflect
    # will use inflect to return the written minutes properly
    #acutally return the value so that main can print it



...


if __name__ == "__main__":
    main()
