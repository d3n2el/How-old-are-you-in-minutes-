from datetime import date
from datetime import timedelta
import re
class Date:
    date = datetime.date.today
    def __init__(self, year, month, day):
        if year == None or month == None or day == None:
            raise ValueError("Invalid Time")
        self.year= year
        if int(month)> 12:
            raise ValueError("Invalid month")
        else:
            self.month = month
        if int(day)> 31:
            raise ValueError("Invalid day")
        else:
            self.day = day

    def __sub__(self, other):
        time = datetime(year,month,day)
        minutes= 
        return time

def main():
    #print the converted time. Will probably make a convert function
    #also, ask for input]
    print(convert(input("Date of birth: ")))

def convert(t):
    # need to elaborate input and split it
    year,month,day = re.search(r"([0-9]{4})-([0-9]{2})-([0-9]{2})", t)

    #either .split or re.split
    #Probably re.split since its way more flexible, since i want to get yyyy-mm-dd format
    #will probably need to convert the time in int
    # override - so that it returns a timedelta
    # will use inflect to return the written minutes properly
    #acutally return the value so that main can print it
    #Also need to properly define Date, as of rn its barebones



...


if __name__ == "__main__":
    main()
