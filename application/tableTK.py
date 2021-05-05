from tkinter import *


class Table:

    def __init__(self, root, row, column, lst):

        # code for creating table
        for i in range(row):
            for j in range(column):
                self.e = Label(root, width=15, fg='blue',
                               font=('Arial', 10, 'bold'))
                if i == 0:
                    self.e.configure(fg='black')

                self.e.grid(row=i, column=j)
                self.e.configure(text=str(lst[i][j]))
