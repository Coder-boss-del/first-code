from tkinter import *
from tkinter import messagebox


def getlist():
    lists = listbox.get("1")
    messagebox.showinfo(lists , title="success" )

def add_task():
    task = entry.get()
    if task:
        listbox.insert(END , task)
        entry.delete(0 , END)
    else:
        messagebox.showerror(title='ERROR' , message='PLEASE ENTER A TASK FIRST')

def delete_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)
    else:
        messagebox.showwarning(title='WARNING' , message='Select a task to be deleted???')

def enter1():
    enter = enter.get
    if enter:
        messagebox.showinfo(title="Thanks" , message="Thank You Please Go To Cashier for Products")
    

if __name__ == '__main__':
    window = Tk()
    window.title("Shop to chop supermarket")
    window.minsize=('1000*900')
    
    label = Label(text='Shop To Chop Supermarket', font=('Arial' , 30 , 'bold'))
    label.pack()
    
    entry = Entry()
    entry.pack()
    
    add_button = Button(text='Add product' , command=add_task)
    add_button.pack()
    
    listbox = Listbox()
    listbox.pack()
    
    delete_button = Button(text='Delete product' , command=delete_task)
    delete_button.pack()
    
    clear_button = Button(text='Clear all products')
    clear_button.pack()
    
    enter1_button = Button(text="Enter", command=getlist)
    enter1_button.pack()

window.mainloop()