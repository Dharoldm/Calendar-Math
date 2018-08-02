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
        """
        This finds the time between the two days given. Preferably, this method is called on the earlier date.
        :param other: The other date
        :return: The days between the two dates
        """
        curr_year = self.year  # The year that is being started from
        goal_year = other.year  # The end year of this length of time being figured out
        curr_month = self.month  # The starting month
        goal_month = other.month  # Ending month
        curr_day = self.day  # Starting day
        goal_day = other.day  # Ending day
        days = 0  # Days between the two dates
        month = self.calendar.head  # Linked list of every month with their days
        leap = False  # if the year is a leap year this is true
        # I'm writing up here that leap years have stupid math asociated with them that'll make this code uglier than it
        # is
        while month.key is not self.month_str:
            month = month.next
        if curr_year != goal_year:
            while goal_year - curr_year > 1:
                curr_year += 1
                if curr_year%4 == 0:
                    if curr_year%100 != 0:
                        days += 366
                    elif curr_year%400 == 0:
                        days += 366
                    else:
                        days += 365
                else:
                    days += 365
            if curr_month < goal_month:
                assert isinstance(goal_month, int)
                curr_year += 1
                if curr_year % 4 == 0:
                    if curr_year % 100 != 0:
                        days += 366
                    elif curr_year % 400 == 0:
                        days += 366
                    else:
                        days += 365
                else:
                    days += 365
                if curr_year % 4 == 0:
                    if curr_year % 100 != 0:
                        leap = True
                    elif curr_year % 400 == 0:
                        leap = True
                    else:
                        leap = False
                while curr_month < goal_month-1:
                    if leap is True and month.key == "Feb":
                        days += 29
                        month = month.next
                        curr_month += 1
                    else:
                        days += month.value
                        month = month.next
                        curr_month += 1
        while month.next.key is not other.month_str:
            if curr_year % 4 == 0:
                if curr_year % 100 != 0:
                    leap = True
                elif curr_year % 400 == 0:
                    leap = True
                else:
                    leap = False
            if leap is True and month.key == "Feb":
                days += 29
                month = month.next
                curr_month += 1
            else:
                days += month.value
                month = month.next
                curr_month += 1
            if curr_month == 13:
                curr_month = 1
                curr_year += 1
            leap = False
        if curr_day < goal_day:
            if leap is True and month.key == "Feb":
                days += 29
                month = month.next
                curr_month += 1
            else:
                days += month.value
                month = month.next
                curr_month += 1
            if curr_month == 13:
                curr_month = 1
                curr_year += 1
                leap = False
        else:
            if leap is True and month.key == "Feb":
                days += 29 - curr_day + 1
                month = month.next
                curr_month += 1
                curr_day = 1
            else:
                days += month.value - curr_day + 1
                month = month.next
                curr_month += 1
                curr_day = 1
            if curr_month == 13:
                curr_month = 1
                curr_year += 1
                leap = False
        if curr_day < goal_day:
            days += goal_day-curr_day
        return days


test = Date(11, "Jul", 1901)
that = Date(30, "Apr", 2837)
print(test)
print(test.subtraction(that))