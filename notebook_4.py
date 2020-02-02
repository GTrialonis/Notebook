# This is a calendrical notebook 
# you can find it at """
# C:\Users\User\Desktop\PYTHON\notebook_2.py."""

import csv
import pandas as pd
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from datetime import date
import calendar, datetime

import time
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
# print(current_time)

# ===== Difference between first day of year and current day =====
pd.set_option('mode.chained_assignment', None)

### The line below reads the csv file (the calendar 2020)
calDF = pd.read_csv('/Users/User/Desktop/cal2020.csv', encoding='latin-1')

frame_tab = []

today = date.today() # this is formated as: 2020-01-21, current date
calDay = calendar.day_name[today.weekday()] # the calendar day, e.g. 'Sunday'
# d1 = today.strftime("%d/%m/%Y") # 21/01/2020, current date
# d2 = today.strftime("%B %d, %Y") # January 21, 2020, current date

# ============= My variables =============
txtDay = []
calEntries = {}
ddays = 0
text_var = {-1:"PAST day is: ", 0:"Today is: ", 1:"FUTURE day is: "}
daysDict = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
dictDays = {'Monday':0, 'Tuesday':1, 'Wednesday':2, 'Thursday':3, 'Friday':4, 'Saturday':5, 'Sunday':6}
numdays = 7
cdt = today.weekday() # current(system) day as integer, e.g. 4

# ============== Difference between start of year and start of calendar ======
first_date = date(2020, 1, 1)
now_date = today # the now_date changes EVERY DAY
delta = now_date - first_date # number of days sine start of year
calStart = delta.days # this is the correct day for the start of calendar
    # this calendar starts on 30 January 2020. SAME AS delta ABOVE.
# ---------------------------------------------------------------------------
calStartDay = int(calDF.index.values[calStart]) # this is an index number, e.g. 0, 1, etc.
                                    # of the record in the pandas data frame
                                    # It reads the 30th record of the calendar

sysDate = datetime.date.today() + datetime.timedelta(days=calStartDay)
                                    # prints: system date, e.g. 2020-01-30
#-----------------------------------------------------------------------------

def doNothing():
    pass

def exitProgr():
    root.destroy()

def loadEntries(): # this can be used to load calendars of previous years
    doNothing()
##    calDF = pd.read_csv('/Users/User/Desktop/cal2020.csv', encoding='latin-1')
##    currentDay()
    
def saveEntries():
    calDF.to_csv('/Users/User/Desktop/cal2020.csv', index=False, encoding='latin-1')

def editEntry():
    global calStar
    calDF['Entry'][calStart]=txtDay.get('1.0', END)

# ------- DATE CHANGE as buttons are pressed: The MOVE module -------
def currentDay():
    global sysDate, ddays, calStart
    # ddays = 0
    txtDay.delete('1.0', END)
    # the below is a date, e.g. 2020-01-30
    sysDate = datetime.date.today() + datetime.timedelta(days=ddays)
    
    date = str(sysDate)
    tps = findDay(date) # week-day as string to be used to define position of tab below
    nb.select(dictDays[tps]) # dictDays[tps] gives an integer number
    
    # ----------- Using Pandas to display current Entry --------
    txtDay.delete('1.0', END) # delete any previous entry
    # txtDay.insert(END, '\n')
    nowEntry = calDF.iloc[calStart]['Entry']
    txtDay.insert(END, nowEntry)
    #-------Change Label date--------
    Labels()
    Buttons()

def backEntries():
    global ddays, sysDate, calStart
    ddays = ddays-1
    calStart -= 1 # decrements days by one
    if calStart < 0:

        txtDay.insert(END, 'No more entries. \n Search previous calendars')

    elif calStart == 30:
        txtDay.delete('1.0', END)
        currentDay()
    
    else:
        txtDay.delete('1.0', END)
        sysDate = datetime.date.today() + datetime.timedelta(days=ddays) # ok, it workds
        date = str(sysDate)
        tps = findDay(date) # week-day as string to be used to define position of tab below
        nb.select(dictDays[tps]) # this is a string
        # ----------- Using Pandas --------
        prevEntry = calDF['Entry'][calStart] # previous Entry
        txtDay.insert(END, prevEntry)
    #------Change Label date------
        Labels()
        Buttons()
    
def fwdEntries():
    global ddays, sysDate, calStart
    ddays = ddays+1 # increments days by one
    calStart += 1

    if calStart == 30:
        txtDay.delete('1.0', END)
        currentDay()
    else:
        txtDay.delete('1.0', END)
        sysDate = datetime.date.today() + datetime.timedelta(days=ddays) # ok, it workds
        date = str(sysDate)
        tps = findDay(date) # week-day as string to be used to define position of tab below
        nb.select(dictDays[tps]) # this is a string
        # ----------- Using Pandas --------
        nxtEntry = calDF['Entry'][calStart] # next Entry
        txtDay.insert(END, nxtEntry)
    #-------Change Label date--------
        Labels()
        Buttons()

def findDay(date): 
    tabPosit = datetime.datetime.strptime(date, '%Y-%m-%d').weekday() 
    return (calendar.day_name[tabPosit])

root = Tk()
root.title("Notebook")
# root.configure(background='#B0C4DE')
root.geometry('450x300')

dateFrame = Frame(root)
dateFrame.pack(side=TOP)

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

def Labels():
    global sysDate, calStart, ddays
    print(ddays)
    if ddays < 0:
        lbl = Label(dateFrame, text=text_var[-1]+str(sysDate))
        lbl.configure(font='12')
        lbl.configure(foreground='red')
        lbl.grid(row=1, column=0, sticky='W', padx=3)
    elif ddays > 0:
        lbl = Label(dateFrame, text=text_var[1]+str(sysDate))
        lbl.configure(font='12')
        lbl.configure(foreground='green')
        lbl.grid(row=1, column=0, sticky='W', padx=3)
    else:
        lbl = Label(dateFrame, text=text_var[0]+str(sysDate)+"            ")
        lbl.configure(font='12')
        lbl.configure(foreground='black')
        lbl.grid(row=1, column=0, sticky='W', padx=3)
        
def Buttons():
    butBwd = Button(dateFrame, text="<", command=backEntries)
    butBwd.configure(width='3')
    butBwd.grid(row=1, column=1, padx=3, sticky=E)

    butFwd = Button(dateFrame, text=">", command=fwdEntries)
    butFwd.configure(width='3')
    butFwd.grid(row=1, column=2, padx=3, sticky=E)

ttk.Style().configure("TButton", foreground="blue")
ttk.Style().configure("TButton", background="cyan")

butLoad = Button(bottomFrame, text="Load Calendar", command=loadEntries)
butLoad.grid(row=0, column=0, pady=5)

butSave = Button(bottomFrame, text="Save EACH Edit...", command=editEntry)
butSave.grid(row=0, column=1, pady=5)

butSave = Button(bottomFrame, text="..then SAVE Calendar", command=saveEntries)
butSave.grid(row=0, column=2, pady=5)

butExit = Button(bottomFrame, text="Exit Program", command=exitProgr)
butExit.grid(row=0, column=3, pady=5)

nb = ttk.Notebook(root)
nb.pack(side=TOP)


Labels()
Buttons()

#-------- Make the tabs -------------
for i in range(7):
    frame_tab = ttk.Frame(nb, relief=SUNKEN) # this gives us 7 frames
    nb.add(frame_tab, text=daysDict[i], state="normal") # the text refers to the day of the week

txtDay = Text(root, width=50, height=12, bd=2, bg='#FFFAFA', padx=10, wrap=WORD)
txtDay.pack(side=TOP, pady=5)
    
 
currentDay() 

nb.enable_traversal()


root.mainloop()

