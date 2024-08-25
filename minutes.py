from datetime import datetime, timedelta,date
import re
class Date:
    def __init__(self, time=None):
        self.time = time if time else date.today()

    def __sub__(self, other):
        timediff = self.time - other.time
        return timediff.days * 24 * 60 + timediff.seconds // 60
    def __str__(self):
        return f"{self.time}"

def main():
    print(convert(input("Date of birth: ")))

def convert(t):
    # need to elaborate input and split it
    time = re.search(r"([0-9]{4})-([0-9]{2})-([0-9]{2})", t)
    year,month,day = time.groups()
    #validate input through date module
    try:
        date_= date.today()
        year= int(year)
        month= int(month)
        day = int(day)
        d = date(year,month,day)
        final= date_ - d
        return final

    except ValueError as e:
        sys.exit(f"{e}: Invalid Date")


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
