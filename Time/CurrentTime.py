# -*- coding: utf-8 -*-

from datetime import datetime

str = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
print("all=" + str)

str = datetime.now().year
print("year={}".format(str))

str = datetime.now().month
print("month={}".format(str))

str = datetime.now().day
print("day={}".format(str))

str = datetime.now().weekday()
print("week={}".format(str))

str = datetime.now().hour
print("hour={}".format(str))

str = datetime.now().minute
print("minute={}".format(str))

str = datetime.now().second
print("second={}".format(str))
