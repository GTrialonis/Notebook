# This is a calendrical notebook 
# you can find it at """
# C:\Users\User\Desktop\PYTHON\notebook_3a.py."""

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
pd.set_option('mode.chained_assignment', None)
back_option = 0

def initialize():
    global ddays, jump, today, cdt, calDay, txdDay, calEntries, text_var
    global daysDict, dictDays, sysDate, calDF, calStart
    ### The line below reads the csv file (the calendar 2020)
    calDF = pd.read_csv("/Users/User/Desktop/cal2020-A.csv")

    # ============= My variables =============
    program_start = 0
    
    jump = 1
    frame_tab = []
    txtDay = []
    calEntries = {}
    ddays = 0
    text_var = {-1:"PAST day is: ", 0:"Today is: ", 1:"FUTURE day is: "}
    daysDict = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
    dictDays = {'Monday':0, 'Tuesday':1, 'Wednesday':2, 'Thursday':3, 'Friday':4, 'Saturday':5, 'Sunday':6}
    numdays = 7

    today = date.today() # this is formated as: 2020-01-21, current date
    cdt = today.weekday() # current(system) day as integer, e.g. 4
    calDay = calendar.day_name[today.weekday()] # the calendar day, e.g. 'Sunday'
    # ============== Difference between start of year and start of calendar ======

    first_date = date(2020, 1, 1)
    now_date = today # the now_date changes EVERY DAY, it is the current date, e.g. 2020-02-12
    delta = now_date - first_date # number of days since start of year, it prints: 30 days, 0:00:00
    calStart = delta.days # number of days since start of year, an integer number

    sysDate = datetime.date.today() + datetime.timedelta(days=ddays)

#-----------------------------------------------------------------------------

def doNothing():
    pass

def exitProgr():
    root.destroy()

def loadEntries(): # this can be used to load calendars of previous years
    calDF = pd.read_csv("/Users/User/Desktop/cal2020-A.csv")
##    calDF = pd.read_csv('/Users/User/Desktop/cal2020.csv', encoding='latin-1')

    
def saveEntries():
    calDF.to_csv("/Users/User/Desktop/cal2020-A.csv", index=False)

def saveEachEdit():
    global calStar
    calDF['Entry'][calStart]=txtDay.get('1.0', END)

# ------- DATE CHANGE as buttons [<] or [>], are pressed: The MOVE module -------
def currentDay():
    global sysDate, ddays, calStart
    txtDay.delete('1.0', END)
    # the below is a date, e.g. 2020-01-30
    sysDate = datetime.date.today() + datetime.timedelta(days=ddays)
    
    date = str(sysDate)
    tps = findDay(date) # week-day as string to be used to define position of tab below
    nb.select(dictDays[tps]) # dictDays[tps] gives an integer number
    
    # ----------- Using Pandas to display current Entry --------
    txtDay.delete('1.0', END) # delete any previous entry
    # txtDay.insert(END, '\n')
    nowEntry = calDF.iloc[calStart]['Entry'] # shows current entry, which is correct
    txtDay.insert(END, nowEntry)
    #-------Change Label date--------
    Labels()
    Buttons()
# -----------------------------------------------------------------

def backEntries():
    global ddays, sysDate, calStart, first_date, then_date, jump
    # jump = -jump
    ddays = ddays-1
    print('jump at backEntries: ', jump)
    print('ddays at backEntries: ', ddays)
    calStart = calStart-jump # decrements days by one or more numbers
            # calStart represents the index number of an entry
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
        jump = 1
    
    #------Change Label date------
    Labels()
    Buttons()

# ---------------------------------------------------------------
    
def fwdEntries():
    global ddays, sysDate, calStart, first_date, then_date, jump
    try:
        ddays = ddays+jump
        print('jump at fwdEntries: ', jump)
        print('ddays at fwdEntries: ', ddays)
        print('------------------------------')
        calStart = calStart+jump # increments days by one
        
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
            jump = 1
        
    except TypeError:
        doNothing()
    #-------Change Label date--------
    Labels()
    Buttons()

def findDay(date):
    '''
    the first line below prints an integer, 0-6, for the days of the week
    the second line returns the corresponding name of the day
    '''
    tabPosit = datetime.datetime.strptime(date, '%Y-%m-%d').weekday()
    return (calendar.day_name[tabPosit])


root = Tk()
root.title("Notebook")
# root.configure(background='#B0C4DE')
root.geometry('620x300')

dateFrame = Frame(root)
dateFrame.pack(side=TOP)

rightFrame = Frame(root)
rightFrame.pack(side=RIGHT)

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)


def Labels():
    global sysDate, calStart, ddays
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

def other():
    pass
##    wnd = Tk()
##    wnd.title("Specifying Calendar Details")
##    global nw, scrTxt
# ---------------------------------------------------------

def return_to_date():
    initialize()
    currentDay()
# -------------------------------------------------
def make_New_Entry(event):
    global yyyy, mm, dd, calStart, now_date, today, back_option
    global sysDate, first_date, then_date, jump, delta
    jump = 1
    ''' Make a new entry, for past of future '''
    try:
        date_input = day_text.get() # pronts user for imput of date
        dateEntry = calDF['Entry'][calDF['day']==date_input] # gets date for new entry
        dateEntry = list(dateEntry) # the entry made by the user
        dateEntry = dateEntry[0].strip() # the above entry stripped
    except IndexError:
        doNothing()
        
    ''' Slicing the date_input of the user.'''
    yyyy = int(date_input[6:]) # the Year as integer
    mm = int(date_input[3:5]) # the month as integer
    dd = int(date_input[:2]) # the day as integer
    
    ''' Calculation of difference between new date given and now_date '''
    ''' BEWARE both past and future must be taken into account.'''
    # the below is only for the present
    then_date = date(yyyy, mm, dd)
    now_date = today
    delta = then_date - now_date # positive for future and negative for past
    deltaa = str(delta) # same as above
    print('deltaa at make_New_Entry: ', deltaa)
    try:
        deltaa = int(deltaa[0:3]) # <--------------
    except ValueError:
        doNothing()
        
    # calStart = calStart+deltaa
    jump = deltaa # jump forward or backward
    print('jump at make_New_Entry: ', jump) # this must be the same as deltaa
    loadEntries()
    if deltaa > 0: # future
        fwdEntries()
    elif deltaa < 0 and back_option < 1:
        txtDay.insert(END, "Use the left arrow key, [<], to go back to make and edit entry")
        # backEntries()
        back_option += 1
        initialize()
        
    else:
        doNothing()
        
# -----------RADIO BUTTONS ---------------------------------

def sel():
    pass

lbl2 = Label(rightFrame, text="Type date (dd/mm/yyyy) in box\nbelow to MAKE or EDIT entry")
lbl2.grid(row=0, column=0, padx=5)
# ----------- the ENTRY box -------
day_text = StringVar()
entr1 = Entry(rightFrame, width=10,textvariable=day_text)
entr1.grid(row=1, column=0, padx=5, pady=5)
entr1.focus_set()
entr1.bind('<Return>', make_New_Entry)

# --------------------------------------------------
lbl3 = Label(rightFrame, text="Repeat THIS Entry: ")
lbl3.grid(row=2, column=0, padx=11, pady=5)

var = IntVar()
R1 = Radiobutton(rightFrame, text = "Daily", variable = var, value = 1,
                  command = sel)
R1.grid(row=3, sticky=W, padx=10)

R2 = Radiobutton(rightFrame, text = "Weekly", variable = var, value = 2,
                  command = sel)
R2.grid(row=4, sticky=W, padx=10)

R3 = Radiobutton(rightFrame, text = "every TWO weeks", variable = var, value = 3,
                  command = sel)
R3.grid(row=5, sticky=W, padx=10)

R4 = Radiobutton(rightFrame, text = "Monthly", variable = var, value = 4,
                  command = sel)
R4.grid(row=6, sticky=W, padx=10)

label = Label(rightFrame, text="")
label.grid(row=7, sticky=W, padx=10)
butReturn = Button(rightFrame, text="RETURN TO DATE", command=return_to_date)
butReturn.grid(row=8, sticky=S, pady=7)                   
#--------------------------------------------------------
ttk.Style().configure("TButton", foreground="blue")
ttk.Style().configure("TButton", background="cyan")

butLoad = Button(bottomFrame, text="OTHER", command=other)
butLoad.grid(row=0, column=0, pady=5)

butSave = Button(bottomFrame, text="Save EACH Edit...", command=saveEachEdit)
butSave.grid(row=0, column=1, pady=5)

butSave = Button(bottomFrame, text="..then SAVE Calendar", command=saveEntries)
butSave.grid(row=0, column=2, pady=5)

butExit = Button(bottomFrame, text="Exit Program", command=exitProgr)
butExit.grid(row=0, column=3, pady=5)

nb = ttk.Notebook(root)
nb.pack(side=TOP)

initialize()

Labels()
Buttons()

#-------- Make the tabs -------------
for i in range(7):
    frame_tab = ttk.Frame(nb, relief=SUNKEN) # this gives us 7 frames
    nb.add(frame_tab, text=daysDict[i], state="normal") # the text refers to the day of the week

txtDay = Text(root, width=50, height=12, bd=2, bg='#FFFAFA', padx=10, wrap=WORD)
txtDay.pack(side=TOP, pady=5, padx=10)




currentDay() 


root.mainloop()

