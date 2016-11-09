#########################################################################################
# EndOfMonth.py - Python Script to the last day of the current month.
# Copyrights (c) - Frédéric Charette 2016
#
# usage: Call the function to a variable in order to report the last day of the month
#
##########################################################################################
#

import datetime

def LastDayOfMonth(AnyDay):
    NextMonth = AnyDay.replace(day=28) + datetime.timedelta(days=4)  
    return NextMonth - datetime.timedelta(days=NextMonth.day)

dEndOfMonth = LastDayOfMonth(datetime.date.today()) 

