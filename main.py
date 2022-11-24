from tkinter import (
    messagebox,
    Tk,
    Menu,
    Toplevel,
    Entry,
    Button,
    Text,
    SUNKEN,
    RAISED,
    GROOVE,
    RIDGE,
    FLAT,
    StringVar,
    OptionMenu,
    font,
    ttk,
    Label,
    BOTH,
    IntVar,
)

root = Tk()
root.geometry("700x370")
root.title("Text Editor")
root.configure(bg="light gray")

font_str = StringVar()
font_size = IntVar()

string = "Calibri"
size = 12

menu_bar = Menu(root)

fileMenu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=fileMenu)
editMenu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=editMenu)
fontMenu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Font", menu=fontMenu)


def FindMenu():
    def find():
        sub = entry.get()
        val = typeWindow.get("1.0", "end-1c")

        if sub not in val or not val or not sub:
            messagebox.showerror("Error", "No matching occurences found!")

        index = 1
        c = 0
        res = []
        text = val.split("\n")

        for string in text:
            i = 0
            j = len(sub)
            while j <= len(string):
                if j == len(string):
                    if string[i:] == sub:
                        res.append(
                            (str(index) + "." + str(i), str(index) + "." + str(j))
                        )
                    break
                else:
                    if string[i:j] == sub:
                        res.append(
                            (str(index) + "." + str(i), str(index) + "." + str(j))
                        )
                        i = j
                    else:
                        i += 1
                    j = i + len(sub)
            index += 1

        typeWindow.delete("1.0", "end-1c")
        typeWindow.insert("1.0", val)
        typeWindow.tag_configure("highlight", background="yellow", foreground="black")

        for pos in res:
            typeWindow.tag_add("highlight", pos[0], pos[1])

        popup.destroy()

    popup = Toplevel(root)
    popup.transient(root)
    popup.title("Find")
    popup.geometry("300x100")

    entry = Entry(popup, width=25)
    entry.place(x=30, y=35)

    button = Button(
        popup,
        text="Find",
        font=("Courier", 11, "bold"),
        command=find,
        padx=10,
        relief=GROOVE,
    )
    button.place(x=200, y=32)


def ReplaceMenu():
    def replace():
        sub = entry1.get()
        subn = entry2.get()
        val = typeWindow.get("1.0", "end-1c")

        if not sub or not val:
            messagebox.showerror("Error", "Please enter valid inputs!")

        index = 1
        c = 0
        res = []
        text = val.split("\n")
        val = ""

        for string in text:
            i = 0
            j = len(sub)
            while j <= len(string):
                if j == len(string):
                    if string[i:] == sub:
                        res.append(
                            (str(index) + "." + str(i), str(index) + "." + str(j))
                        )
                        val += subn
                    else:
                        val += string[i:]
                    break
                else:
                    if string[i:j] == sub:
                        res.append(
                            (str(index) + "." + str(i), str(index) + "." + str(j))
                        )
                        val += subn
                        i = j
                    else:
                        val += string[i]
                        i += 1
                    j = i + len(sub)
            val += "\n"
            index += 1

        typeWindow.delete("1.0", "end-1c")
        typeWindow.insert("1.0", val)
        typeWindow.tag_configure("highlight", background="yellow", foreground="black")

        for pos in res:
            typeWindow.tag_add("highlight", pos[0], pos[1])

        popup.destroy()

    popup = Toplevel(root)
    popup.transient(root)
    popup.title("Replace")
    popup.geometry("300x100")

    label1 = Label(popup, text="Find", font=("Courier", 13, "bold"))
    label1.place(x=40, y=20)

    entry1 = Entry(popup, width=25)
    entry1.place(x=112, y=23)

    entry2 = Entry(popup, width=25)
    entry2.place(x=30, y=55)

    button = Button(popup, text="Replace", command=replace, padx=10, relief=GROOVE)
    button.place(x=200, y=52)


def FontStyle():
    global font_str
    fonts = font.families()
    sizes = [i for i in range(8, 30)]
    font_str.set(string)
    font_size.set(size)

    def font_set():
        global font_str, string, size
        fontstyle = fontlist.get()
        size_font = fontsize.get()
        string = fontstyle
        size = size_font
        typeWindow.config(font=(f"{fontstyle}", size_font))
        popup.destroy()

    popup = Toplevel(root)
    popup.transient(root)
    popup.title("Font Style")
    popup.geometry("300x100")

    fontlist = ttk.Combobox(popup, textvariable=font_str, state="readonly")
    fontlist["values"] = fonts
    fontlist.current(fonts.index(string))
    fontlist.place(x=30, y=25)

    fontsize = ttk.Combobox(popup, textvariable=font_size, state="readonly")
    fontsize["values"] = sizes
    fontsize.current(sizes.index(int(size)))
    fontsize.place(x=30, y=45)

    button = Button(popup, text="Apply", command=font_set, padx=10, relief=GROOVE)
    button.place(x=200, y=32)


fileMenu.add_command(label="Find", command=FindMenu)
fileMenu.add_command(label="Replace", command=ReplaceMenu)
editMenu.add_command(label="Copy")
editMenu.add_command(label="Cut")
fontMenu.add_command(label="Font Style", command=FontStyle)
fontMenu.add_command(label="Format")

typeWindow = Text(root, relief=GROOVE, height=19, width=90, font=("Calibri", 12))
typeWindow.pack_propagate(False)
typeWindow.pack(fill=BOTH, expand=True)

root.config(menu=menu_bar)
root.mainloop()
