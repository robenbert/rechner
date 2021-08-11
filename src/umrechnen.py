from tkinter import *

window = Tk()
window.title("umrechner")
window.geometry("350x200")

umrech_liste = [["millimeter", 1], ["centimeter", 10], ["meter", 1000], ["killometer", 1000000]]

txt = Entry(window, width=10)
txt.grid(column=0, row=0)

lbl1 = Label(window, text="qaqa")
lbl1.grid(column=1, row=0)

val1 = StringVar()
val1.set("auswählen")
val2 = StringVar()
val2.set("auswählen")

options_list = ["millimeter", "centimeter", "meter", "killometer"]

opt1 = OptionMenu(window, val1, *options_list)
opt1.grid(column=0, row=1)

lbl2 = Label(window, text="zu")
lbl2.grid(column=1, row=1)

opt2 = OptionMenu(window, val2, *options_list)
opt2.grid(column=2, row=1)

##########################################################################################

def temp():
    x = 0
    valu1 = val1.get()
    valu2 = val2.get()
    if valu1 == "grad":
        x = float(txt.get())
    elif valu1 == "Fahrenheit":
        x = (float(txt.get()) - 32) / 1.8
    elif valu1 == "kelvin":
        x = float(txt.get()) + 273.15

    if valu2 == "Fahrenheit":
        x = x * 1.8 + 32
    elif valu2 == "kelvin":
        x = x - 273.15

    lbl1.config(text=str(x))

def umrech():
    global umrech_liste
    x = 0
    valu1 = val1.get()
    valu2 = val2.get()
    for i in umrech_liste:
        if valu1 == i[0]:
            x = float(txt.get()) * i[1]

    for i in umrech_liste:
        if valu2 == i[0]:
            x = x / i[1]

    lbl1.config(text=str(x))

btn = Button(window, text="umrechnen", command=umrech)
btn.grid(column=0, row=2)

##############################################################################

def umgewicht(valu3):
    global umrech_liste
    valu3 = val3.get()
    if valu3 == "längen":
        options_list = ["millimeter", "centimeter", "meter", "killometer"]
        umrech_liste = [["millimeter", 1], ["centimeter", 10], ["meter", 1000], ["killometer", 1000000]]
        btn.config(command=umrech)
    elif valu3 == "masse":
        options_list = ["milligram", "gram", "killogram", "tonnen"]
        umrech_liste = [["milligram", 1], ["gram", 1000], ["killogram", 1000000], ["tonnen", 1000000000]]
        btn.config(command=umrech)
    elif valu3 == "zeit":
        options_list = ["millisekunde", "sekunde", "minute", "stunde"]
        umrech_liste = [["millisekunde", 1], ["sekunde", 1000], ["minute", 60000], ["stunde", 3600000]]
        btn.config(command=umrech)
    elif valu3 == "temperatur":
        options_list = ["grad", "Fahrenheit", "kelvin"]
        btn.config(command=temp)

    opt1 = OptionMenu(window, val1, *options_list)
    opt1.grid(column=0, row=1)
    opt2 = OptionMenu(window, val2, *options_list)
    opt2.grid(column=2, row=1)

auswahl = ["längen", "masse", "zeit", "temperatur"]
val3 = StringVar()
val3.set("längen")

opt3 = OptionMenu(window, val3, *auswahl, command=umgewicht)
opt3.grid(column=0, row=3)

window.mainloop()