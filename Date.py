class Date(object):
    def __init__(self, day, month, year):
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        days =  [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.day = day
        self.month = month
        self.year = year
        for i in range(0,12):
            print([months[i],days[i]])

    def __repr__(self):
        return f"{self.month} {self.day}, {self.year}"

    def subtraction(self, other):
        days = 0
        if self.year != other.year:
           days +=  abs(self.year - other.year)*365


test = Date(1,2,3)
print(test)