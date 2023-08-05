from tkinter import *
import tkinter.messagebox as msg

class Multiple():
    def __init__(self,root):
        self.root = root
        self.root.geometry("400x400")
        self.root.title("Library Management System")
        self.root.config(bg ="powderblue")
        title = Label(self.root,text = "Home Page", bg = "powderblue",font = ('bold','25'))
        title.pack()

        admin_button = Button(self.root, text = "Admin" , command=self.admin_page)
        admin_button.place(x=150,y=120)

        user_button = Button(self.root, text = "User", command = self.user_page)
        user_button.place(x=150,y=220)
    

    def  admin_page(self):
        window = Tk()
        window.title("Admin Page")
        window.geometry("500x500")
        window.config(bg="powderblue")

        bookname_label = Label(window, text = "Book Name: ",bg = "powderblue",font = ('bold','18'))
        bookname_label.place(x=70,y=100)

        author_label = Label(window, text="Author Name",bg = "powderblue",font = ('bold','18'))
        author_label.place(x=70,y=160)

        quantity_label = Label(window, text="Quantity",bg = "powderblue",font = ('bold','18'))
        quantity_label.place(x=70,y=220)

        self.bookname_entry = Entry(window)
        self.bookname_entry.place(x=240,y=100)

        self.author_entry = Entry(window)
        self.author_entry.place(x=240,y=160)

        self.quantity_entry = Entry(window)
        self.quantity_entry.place(x=240,y=220)

        label = Button(window,text="Submit", command=self.admin_data)
        label.place(x=150,y=320)


    def user_page(self):
        window1 = Tk()
        window1.title("User Page")
        window1.geometry("500x500")
        window1.config(bg="powderblue")

        bookname_label = Label(window1, text="Book Name: ",bg ="powderblue", font=('bold','18'))
        bookname_label.place(x=70,y=100)

        author_label = Label(window1,text="Author Name: ",bg="powderblue",font=('bold','18'))
        author_label.place(x=70,y=160)

        self.user_book = Entry(window1)
        self.user_book.place(x=240,y=100)

        self.user_author = Entry(window1)
        self.user_author.place(x=240,y=160)


        user_button = Button(window1,text="Submit",command=self.user_data)
        user_button.place(x=150,y=320)


    def admin_data(self):
        import mysql.connector

        mydb = mysql.connector.connect(host = 'localhost',port=3306,user='root',password = 'Bhavesh@2001',database='library_management')
        mycursor = mydb.cursor()

        bookname = self.bookname_entry.get()
        author = self.author_entry.get()
        qty = self.quantity_entry.get()

        mycursor.execute("insert into admin values(%s,%s,%s)",(bookname,author,qty))
        mydb.commit()
        msg.showinfo("Admin Books","Books added to stock")

    def user_data(self):
        import mysql.connector
        mydb = mysql.connector.connect(host = 'localhost',port=3306,user='root',password = 'Bhavesh@2001',database='library_management')
        mycursor = mydb.cursor()

        book_name = self.user_book.get()
        author = self.user_author.get()

        mycursor.execute("Select Quantity form admin where Book_name=%s and Author=%s",(book_name,author))


        q=0
        for i in mycursor:
            q=int(i[0])
        if q>=1:
            q=q-1
            mycursor.execute("update admin set Quantity =%s where Book_name=%s and Author=%s",(q,book_name,author))
            mycursor.execute("insert into user values(%s,%s)",(book_name,author))
            mydb.commit()
            msg.showinfo("Book Availability","Book Available")
        else:
            msg.showerror("Book Availability","Book not found")


root = Tk()
obj = Multiple(root)
root.mainloop()


