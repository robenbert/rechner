from tkinter import *

window = Tk()
window.title("binär umrechner")
window.geometry("350x200")

txt = Entry(window, width=10)
txt.grid(column=0, row=0)

lbl = Label(window, text="qaqa")
lbl.grid(column=0, row=2)

selected = IntVar()

rad1 = Radiobutton(window, text="dezimal", value=1, variable=selected)
rad2 = Radiobutton(window, text="binär", value=2, variable=selected)
rad3 = Radiobutton(window, text="logik gates", value=3, variable=selected)
rad1.grid(column=0, row=1)
rad2.grid(column=1, row=1)
rad3.grid(column=2, row=1)

def clicked():
    val = selected.get()

    if val == 1:
        plus = 1
        ergebnis = 0
        text = txt.get()[::-1]
        for i in text:
            if i == "1":
                plus += plus
                ergebnis += plus
            elif i == "0":
                plus += plus
        lbl.configure(text=str(int(ergebnis / 2)))

    if val == 2:
        ergebnis = ""
        rest = 0
        zahl = int(txt.get())
        while True:
            rest = zahl % 2
            ergebnis += str(rest)
            zahl = int(zahl / 2)
            if zahl == 0:
                break
        lbl.configure(text=ergebnis[::-1])

    if val == 3:
        text = txt.get().split(" ")
        for i in range(0, len(text)):
            if text[i] == "AND":
                x = text[i - 1]
                y = text[i + 1]
                if x == "1" and y == "1":
                    text[i + 1] = "1"
                else:
                    text[i + 1] = "0"
            elif text[i] == "OR":
                x = text[i - 1]
                y = text[i + 1]
                if x == "1" or y == "1":
                    text[i + 1] = "1"
                else:
                    text[i + 1] = "0"
            elif text[i] == "XOR":
                x = text[i - 1]
                y = text[i + 1]
                if x != y:
                    text[i + 1] = "1"
                else:
                    text[i + 1] = "0"
        lbl.configure(text=text[len(text) - 1])

btn = Button(window, text="umrechnen", command=clicked)
btn.grid(column=1, row=2)

window.mainloop()