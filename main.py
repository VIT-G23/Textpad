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
)

root = Tk()
root.geometry("700x370")
root.title("Text Editor")
root.configure(bg="light gray")
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

        if not sub or not val:
            messagebox.showerror("Error", "Please enter valid inputs!")

        print(sub, val)

        """insert find logic here and return a list of tuples with indices
            eg --> [(1.0,1.4),(2.4,2.6)]"""

        typeWindow.delete("1.0", "end-1c")
        typeWindow.insert("1.0", val)

        """iterate over the returned list with two pointers i,j

            typeWindow.tag_add("highlight", f"{i}", f"{j}")

        call this function inside the for-loop"""

        # typeWindow.tag_configure("highlight", background="yellow", foreground="green")

    popup = Toplevel(root)
    popup.title("Find")
    popup.geometry("300x100")
    entry = Entry(popup, width=25)
    entry.place(x=30, y=35)
    button = Button(popup, text="Find", command=find, padx=10)
    button.place(x=200, y=32)


def ReplaceMenu():
    def replace():
        sub = entry.get()
        val = typeWindow.get("1.0", "end-1c")

        if not sub or not val:
            messagebox.showerror("Error", "Please enter valid inputs!")

        print(sub, val)
        """insert Replace logic here and return a list of tuples with indices
            eg --> [(1.0,1.4),(2.4,2.6)]"""

        typeWindow.delete("1.0", "end-1c")
        typeWindow.insert("1.0", val)

        """iterate over the returned list with two pointers i,j

            typeWindow.tag_add("highlight", f"{i}", f"{j}")
            ⠀
        call this function inside the for-loop"""

        # typeWindow.tag_configure("highlight", background="yellow", foreground="green")

    popup = Toplevel(root)
    popup.title("Replace")
    popup.geometry("300x100")
    entry = Entry(popup, width=25)
    entry.place(x=30, y=35)
    button = Button(popup, text="Find", command=replace, padx=10)
    button.place(x=200, y=32)


def font_style():
    fonts = font.families()
    font_str = StringVar()
    font_str.set("calibri")

    def font_set():
        fontstyle = fontlist.get()
        typeWindow.config(font=(f"{fontstyle}",))

    popup = Toplevel(root)
    popup.title("Font Style")
    popup.geometry("300x100")
    fontlist = ttk.Combobox(popup, textvariable=font_str, values=fonts)
    fontlist.place(x=30, y=35)
    button = Button(popup, text="Apply", command=font_set, padx=10)
    button.place(x=200, y=32)


fileMenu.add_command(label="Find", command=FindMenu)
fileMenu.add_command(label="Replace", command=ReplaceMenu)
editMenu.add_command(label="Copy")
editMenu.add_command(label="Cut")
fontMenu.add_command(label="Font Size")
fontMenu.add_command(label="Font Style", command=font_style)
fontMenu.add_command(label="Format")

typeWindow = Text(root, relief=GROOVE, height=19, width=90, font=("Calibri", 12))
typeWindow.place(x=0, y=30)


root.config(menu=menu_bar)
root.mainloop()
