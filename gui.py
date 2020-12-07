from tkinter import *
import calc
import data
import createICS


def quit(window):
    window.destroy()


def createFrames(window):
    title = Frame(window)
    content = Frame(window)
    interaction = Frame(window)
    information = Frame(window)
    title.grid(column=0, row=0)
    content.grid(column=0, row=1)
    interaction.grid(column=0, row=2)
    information.grid(column=0, row=3)
    scrollbar = Scrollbar(content, orient='horizontal')
    return title, content, interaction, information


def create_information(frame,infotext):
    lbl = Label(frame, text=infotext)
    lbl.grid(column=0, row=0)


def create_content_Label(frame, labeltext,x,y):
    lbl = Label(frame, text=labeltext, font=("Courier", 8))
    lbl.grid(column=x, row=y)


def interaction_button(window, frame,chkdict,yr,mon):
    btn = Button(frame, text="Quit", command=lambda : quit(window))
    btn.grid(column=1, row=0)
    btn = Button(frame, text="Create ICS", command=lambda : createICS.create_ics(chkdict,yr,mon))
    btn.grid(column=0, row=0)

def create_checkboxes(chkdict, columndict, frame, x, y):
    chk_state = BooleanVar()
    chk = Checkbutton(frame, var=chk_state, font=("Courier", 3))
    chk.grid(column=x, row=y)
    chkdict.update({str(y) + "_" + columndict[x]: chk_state})
    return chkdict

def generate_gui():
    columndict = data.columndict
    yr, mon, day = calc.monthlen()
    mon = str(mon)
    if len(mon) == 1:
        mon = "0"+mon
    columndict.update({0: str(mon)+"-"+str(yr)})
    lastColumn = len(columndict)
    lastRow = day+1
    chkdict={}

    window = Tk()

    title, content, interaction, information = createFrames(window)

    for x in range(0, lastColumn):
        for y in range(0, lastRow):
            labeltext=""
            if y == 0:
                labeltext=columndict[x]
            else:
                if x == 0:
                    labeltext=str(y)
                else:
                    chkdict = create_checkboxes(chkdict, columndict, content, x, y)

            if labeltext != "":
                create_content_Label(content, labeltext, x, y)

    interaction_button(window, interaction,chkdict,yr,mon)
    create_information(information, "(c) 2020 by AWoodGnome")

    window.mainloop()