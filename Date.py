from LinkedList import LinkedList, HashListNode

class Date(object):
    def __init__(self, day, month, year):
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        days =  [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.day = day
        self.month_str = month
        self.year = year
        self.calendar = LinkedList()
        for i in range(0,12):
            self.calendar.append(months[i],days[i])
        self.calendar.tail.next = self.calendar.head
        calendar = self.calendar.head
        self.month = 1
        while self.month_str is not calendar.key:
            calendar = calendar.next
            self.month += 1

    def __repr__(self):
        return f"{self.month_str} {self.day}, {self.year}"

    def subtraction(self, other):
        curr_year = self.year
        goal_year = other.year
        curr_month = self.month
        goal_month = other.month
        days = 0
        month = self.calendar.head
        while month.key is not self.month_str:
            month = month.next

        if abs(curr_year-goal_year) > 0:
           while goal_year - curr_year > 1:
               curr_year += 1
               if curr_year%4 == 0:
                   days += 366
               else:
                   days += 365
           if curr_month < goal_month:
               assert isinstance(goal_month, int)
               curr_year += 1
               if curr_year % 4 == 0:
                   days += 366
               else:
                   days += 365
               while curr_month < goal_month:
                   days+= month.value
                   month = month.next
                   curr_month += 1
        return days


test = Date(1,"Feb",-38)
that = Date(1,"Aug",2018)
print(test)
print(test.subtraction(that))