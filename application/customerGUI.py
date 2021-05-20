from tkinter import *
from tkinter import ttk
from business.productBS import ProductBS

# list of all products
product = ProductBS()
List = product.findAll()


def showAllProducts():
    new_window = Toplevel()
    # columns
    columns = ('#1', '#2', '#3', '#4')

    tree = ttk.Treeview(new_window, columns=columns, show='headings')

    # define headings
    tree.heading('#1', text='ID')
    tree.heading('#2', text='product_class')
    tree.heading('#3', text='description')
    tree.heading('#4', text='price')

    # adding data to the treeview
    for item in List:
        tree.insert('', END, values=item)

    tree.grid(row=0, column=0)


def selectByID():
    id = int(id_input.get())
    item = product.findById(id)
    new_window = Toplevel()
    # columns
    columns = ('#1', '#2', '#3', '#4')

    tree = ttk.Treeview(new_window, columns=columns, show='headings')

    # define headings
    tree.heading('#1', text='ID')
    tree.heading('#3', text='product_class')
    tree.heading('#2', text='description')
    tree.heading('#4', text='price')

    # adding data to the treeview
    tree.insert('', END, values=(item.id, item.product_class, item.desc, item.price))


    tree.grid(row=0, column=0)


root = Tk()

root.title("customer page")
root.geometry('300x300')

showAllLabel = Label(text="Show All: ")
showAllLabel.grid(row=0, column=0)

showAllProductsButton = Button(text="Products", command=showAllProducts)
showAllProductsButton.grid(row=0, column=1)

selectByIdLabel = Label(text="Select by ID: ")
selectByIdLabel.grid(row=3, column=0)

id_input = Entry()
id_input.grid(row=3, column=1)

selectByIdButton = Button(text="search", command=selectByID)
selectByIdButton.grid(row=3, column=2)

mainloop()
