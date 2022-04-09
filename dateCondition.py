from datetime import date

import quote

today = date.today()

d1 = today.strftime("%m/%d").replace('0', '')  #replace 0 from 04/07 format
d2 = today.strftime("%A") #Monday to Friy

def dateCondition():
    d1 = today.strftime("%m/%d").replace('0', '')
    d2 = today.strftime("%A")
    if d1 == today.strftime("7/10"):
        return"happy birthday🤗🎂 Today is {d2}".format(d1 = d1, d2=d2, nouns = quote.nouns)
    elif d1 == today.strftime("12/24"):
        return "Merry Christmas,Today is {d1}, {d2}".format(d1 = d1,d2=d2)
    elif d1 == today.strftime("1/1"):
        return "Happy new year🥳,Today is {d1}, {d2}".format(d1 = d1,d2=d2)
    else:
        return "Today is {d1}, {d2}".format(d1 = d1,d2=d2)
