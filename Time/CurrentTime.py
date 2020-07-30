# -*- coding: utf-8 -*-

from datetime import datetime

str = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
print("all=" + str)

str = datetime.now().year()
print("year=" + str)

str = datetime.now().month()
print("month=" + str)

str = datetime.now().day()
print("day=" + str)

str = datetime.now().weekday()
print("week=" + str)

str = datetime.now().hour()
print("hour=" + str)

str = datetime.now().minute()
print("minute=" + str)

str = datetime.now().second()
print("second=" + str)
