from tkinter import *
from time import *
from PIL import ImageTk

test = Tk()
test.attributes("-fullscreen", True)
test.config(bg="black")


wallpaper = ImageTk.PhotoImage(file="C:/Users/evert/Pictures/1876553.gif")
browserlogo = ImageTk.PhotoImage(file="C:/Users/evert/Pictures/70x70Logo.scale-100.png")
vscimage = ImageTk.PhotoImage(file=
"C:/Users/evert/AppData/Local/Programs/Microsoft VS Code/resources/app/resources/win32/code_70x70.png")

wp = Label(test, image=wallpaper)
wp.pack(side=TOP)


def open_vsc():
    import os
    os.startfile("C:/Users/evert/AppData/Local/Programs/Microsoft VS Code/Code.exe")


def open_browser():
    import os
    os.startfile("C:/Users/evert/AppData/Local/Programs/Opera GX/opera.exe")


def opensm():
    start = Tk()
    start.geometry("250x400+0+450")
    start.config(bg="black")
    start.overrideredirect(1)

    def clock2():
        time_string2 = strftime("%H:%M:%S")
        clock2lbl.config(text=time_string2)

        (start.after(10, clock2))

    def shutdown():
        start.destroy()
        test.destroy()

    def close():
        start.destroy()

    def settings():
        settingswindow = Tk()
        settingswindow.attributes("-fullscreen", True)
        settingswindow.config(bg="black")

        def closewndw():
            settingswindow.destroy()

        closebtn2 = Button(settingswindow, command=closewndw, text=X, bg="red", width=4, height=2)
        closebtn2.place(y=0, x=1500)

        settingswindow.mainloop()

    start.after(30000, close)

    closebtn = Button(start, command=shutdown, text="shutdown", bg="black", fg="white", width=30, height=2)
    closebtn.place(y=350, x=0)

    funcbtn1 = Button(start, command=close, text="close", bg="black", fg="white", width=30, height=2)
    funcbtn1.place(y=300, x=0)

    funcbtn2 = Button(start, command=settings, text="settings", bg="black", fg="white", width=30, height=2)
    funcbtn2.place(y=250, x=0)

    name = Label(start, text="J.[S].A.R.V.I.S.", bg="Black", fg="Blue", font=("OCR A Extended", 20))
    name.pack(side=TOP)

    name2 = Label(start, text="Project", bg="Black", fg="Blue", font=("OCR A Extended", 20))
    name2.pack(side=TOP)

    clock2lbl = Label(start, font=("OCR A Extended", 10), fg="blue", bg="black")
    clock2lbl.pack(side=TOP)

    clock2()


tb = Label(test, bg="blue", width=1500, height=2)
tb.pack(side=BOTTOM)

startmenu = Button(test, bg="Black", text="Menu", command=opensm, fg="white")
startmenu.place(y="830", x="0")


browser = Button(test, image=browserlogo, command=open_browser, bg="black")
browser.place(x=1400, y=0)

vscode = Button(test, bg="black", image=vscimage, command=open_vsc)
vscode.place(x=1330, y=0)

def clock():
    time_string = strftime("%H:%M:%S")
    time_label.config(text=time_string)

    test.after(10, clock)


time_label = Label(test, font=("OCR A Extended", 20), fg="white", bg="Blue")
time_label.place(y=830, x=1395)

clock()


test.mainloop()
