import datetime
import time
import sys

class Time(object):


    #def init(self, hour, minute, second):
    
    def __init__(self, hour, minute, second):
        assert isinstance(hour, int)
        assert isinstance(minute, int) 
        assert isinstance(second, int) 
        self.hour = hour
        self.minute = minute
        self.second = second

        t = datetime.localtime()
    ##DATETIME OBJECTS
    #Get today's date from datetime class
        today=datetime.now()
    #print (today)
    # Get the current time
    #print "The current time is", t
    #weekday returns 0 (monday) through 6 (sunday)
       # wd = date.weekday(today)
    #Days start at 0 for monday
        days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

       #give the current time
#t = datetime.localtime()
print("Today is day number %d" % wd)
print("which is a " + days[wd])
print("And the time is" +t)
print ("The current time is", t)

          
if __name__== "__Time__":
    Time()
