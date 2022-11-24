from tkinter import messagebox, Tk, Menu, Toplevel, Entry, Button, Text, SUNKEN, Label

root = Tk()

root.geometry("700x400")
root.title("TextPad")

menu_bar = Menu(root)

fileMenu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=fileMenu)
editMenu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=editMenu)


def FindMenu():
    def find():
        sub = entry.get()
        val = typeWindow.get("1.0", "end-1c")

        if sub not in val:
            messagebox.showerror("Error", "No matching occurences found!")
            
    
        l = 1
        c = 0
        res = []
        text = val.split('\n')
        for string in text:
            i = 0
            j = len(sub)
            while j<=len(string):
                if j==len(string):
                    if string[i:] == sub:
                        res.append((str(l)+'.'+str(i),str(l)+'.'+str(j)))
                    break
                else:
                    if string[i:j] == sub:
                        res.append((str(l)+'.'+str(i),str(l)+'.'+str(j)))
                        i = j
                    else:
                        i += 1
                    j = i + len(sub)
            l += 1
    
        typeWindow.delete("1.0", "end-1c")
        typeWindow.insert("1.0", val)
        typeWindow.tag_configure("highlight", background="yellow", foreground="black")
        for pos in res:
            typeWindow.tag_add("highlight", pos[0], pos[1])

    popup = Toplevel(root)
    popup.title("Find")
    popup.geometry("300x100")
    entry = Entry(popup, width=25)
    entry.place(x=30, y=35)
    button = Button(popup, text="Find", command=find, padx=10)
    button.place(x=200, y=32)


def ReplaceMenu():
    def replace():
        sub = entry1.get()
        subn = entry2.get()
        val = typeWindow.get("1.0", "end-1c")

        if not sub or not val:
            messagebox.showerror("Error", "Please enter valid inputs!")

        l = 1
        c = 0
        res = []
        text = val.split('\n')
        val = ''
        for string in text:
            i = 0
            j = len(sub)
            while j<=len(string):
                if j==len(string):
                    if string[i:] == sub:
                        res.append((str(l)+'.'+str(i),str(l)+'.'+str(j)))
                        val += subn
                    else:
                        val += string[i:]
                    break
                else:
                    if string[i:j] == sub:
                        res.append((str(l)+'.'+str(i),str(l)+'.'+str(j)))
                        val += subn
                        i = j
                    else:
                        val += string[i]
                        i += 1
                    j = i + len(sub)
            val += '\n'
            l += 1
        typeWindow.delete("1.0", "end-1c")
        typeWindow.insert("1.0", val)
        typeWindow.tag_configure("highlight", background="yellow", foreground="black")
        for pos in res:
            typeWindow.tag_add("highlight", pos[0], pos[1])

    popup = Toplevel(root)
    popup.title("Replace")
    popup.geometry("300x100")
    label1 = Label(popup,text="Find : ")
    label1.place(x=30, y=35)
    entry1 = Entry(popup, width=25)
    entry1.place(x=112, y=35)
    entry2 = Entry(popup, width=25)
    entry2.place(x=30, y=70)
    button = Button(popup, text="Replace", command=replace, padx=10)
    button.place(x=200, y=67)


fileMenu.add_command(label="Find", command=FindMenu)
fileMenu.add_command(label="Replace", command=ReplaceMenu)
editMenu.add_command(label="Copy")
editMenu.add_command(label="Cut")


typeWindow = Text(root, relief=SUNKEN, height=19, width=84)
typeWindow.place(x=10, y=50)


root.config(menu=menu_bar)
root.mainloop()