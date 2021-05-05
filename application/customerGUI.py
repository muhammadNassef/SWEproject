from tkinter import *
from application.tableTK import Table
from business.customerBS import CustomerBS

# take the data
customerList = CustomerBS().findAll()

root = Tk()

root.title("customer page")
root.geometry('900x500+300+100')

Table(root, len(customerList), len(customerList[0]), customerList)

mainloop()
