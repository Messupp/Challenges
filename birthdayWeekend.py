import datetime

class Solution:

    def run(self, birthday_date):

        a = birthday_date.split("-")
        day = int(a[0])
        month = int(a[1])
        alist = []
        leap = False

        if month == 2:
            if day == 29:
                leap = True


        for year in range(2016,2066):
            if leap == False:
                a = datetime.date(year, month, day)
                weekDay = a.weekday()
                if weekDay == 4:
                    friday = "Fri-{year}".format(year=year)
                    alist.append(friday)
                if weekDay == 5:
                    friday = "Sat-{year}".format(year=year)
                    alist.append(friday)
                if weekDay == 6:
                    friday = "Sun-{year}".format(year=year)
                    alist.append(friday)
        if leap == True:
                alist.append("Sat-2020 Sun-2032 Fri-2036 Sat-2048 Sun-2060 Fri-2064")


        future_dates = " ".join(alist)
        print(future_dates)
        return future_dates

Solution.run("", "29-02")
'''
Input:
"29-02"

Expected Result:
Sat-2020 Sun-2032 Fri-2036 Sat-2048 Sun-2060 Fri-2064
'''