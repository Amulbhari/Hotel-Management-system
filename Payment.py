
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
from tkinter import messagebox
import mysql.connector

class Payment_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1306x530+220+255")

        #variable for msql
        self.var_Customer_ID = StringVar()
        self.var_Payment_ID = StringVar()
        x=random.randint(100,999)
        self.var_Payment_ID.set(str(x))
        self.var_Payment_Mode = StringVar()
        self.var_Paymment_Date = StringVar()
        self.var_Amount = StringVar()

        # Title of Project
        lbl_title = Label(self.root, text="ADD Payments Details", font=("times new roman", 19, "bold"), bg="black", fg="white", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1306, height=50)

        # Logo of Hotel         
        img2 = Image.open("C:/Users/amulb/OneDrive/Desktop/DBMS project/photos/1633410403702hotel-images/hotel images/logoofhotel.jpeg")
        img2 = img2.resize((80, 43), Image.ADAPTIVE)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg2.place(x=5, y=3, width=80, height=43)

        # Label frame
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Payments Details", padx=2, font=("times new roman", 19, "bold"))
        labelframeleft.place(x=5, y=50, width=500, height=470)

        # Customer ID
        lbl_cust_ref = Label(labelframeleft, text="Customer ID -", padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)  

        entry_ref = ttk.Entry(labelframeleft,textvariable=self.var_Customer_ID, width=25)
        entry_ref.grid(row=0, column=1)

        # Payment Id
        lbl_payment_id = Label(labelframeleft, text="Payment ID -", padx=2, pady=6)
        lbl_payment_id.grid(row=1, column=0, sticky=W)  

        epayment_id = ttk.Entry(labelframeleft,textvariable=self.var_Payment_ID,state="readonly", width=25)
        epayment_id.grid(row=1, column=1)

        # Payment Mode
        lbl_Payment_mode = Label(labelframeleft, text="Payment Mode -", padx=2, pady=6)
        lbl_Payment_mode.grid(row=2, column=0, sticky=W)  

        combo_Payment_Mode = ttk.Combobox(labelframeleft,textvariable=self.var_Payment_Mode, width=22, state="readonly")
        combo_Payment_Mode["values"]= ("Online", "Cash", "Card")
        combo_Payment_Mode.grid(row=2, column=1)

        # Payment Date 
        lbl_payment_date = Label(labelframeleft, text="Payment Date -", padx=2, pady=6)
        lbl_payment_date.grid(row=3, column=0, sticky=W)  

        epayment_date= ttk.Entry(labelframeleft,textvariable=self.var_Paymment_Date, width=25)
        epayment_date.grid(row=3, column=1)

        # Amount of payment
        lbl_Amount_of_payment = Label(labelframeleft, text="Amount -", padx=2, pady=6)
        lbl_Amount_of_payment.grid(row=4, column=0, sticky=W)  

        eAmount_of_payment = ttk.Entry(labelframeleft,textvariable=self.var_Amount, width=25)
        eAmount_of_payment.grid(row=4, column=1)

        # Button frame
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=10, y=300, width=400, height=35)

        # Add button
        btnAdd = Button(btn_frame, text="Add",command=self.add_data, font=("Arial", 12), bg="black", fg="white", width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        # Delete button
        btnDelete = Button(btn_frame, text="Delete",command=self.mDelete, font=("Arial", 12), bg="black", fg="white", width=10)
        btnDelete.grid(row=0, column=1, padx=1)

        # Update button
        btnUpdate = Button(btn_frame, text="Update", command=self.Update,font=("Arial", 12), bg="black", fg="white", width=10)
        btnUpdate.grid(row=0, column=2, padx=1)

        # Reset button
        btnReset = Button(btn_frame, text="Reset",command=self.reset, font=("Arial", 12), bg="black", fg="white", width=10)
        btnReset.grid(row=0, column=3, padx=1)

        # Table frame in right side
        # Label frame
        labelTableframeright = LabelFrame(self.root, bd=2, relief=RIDGE, text="The Details", padx=2, font=("times new roman", 19, "bold"))
        labelTableframeright.place(x=510, y=50, width=790, height=470)

        # Search By Label
        cSearchbar = Label(labelTableframeright, text="Search By", bg="black", fg="white")
        cSearchbar.grid(row=0, column=0, sticky=W, padx=2)  

        # Search Bar Combobox
        self.search_var=StringVar()
        combo_search_bar = ttk.Combobox(labelTableframeright,textvariable=self.search_var, width=30, state="readonly")
        combo_search_bar["values"] = ("Customer ID", "Payment ID", "Payment Mode", "Payment Date", "Amount")
        combo_search_bar.grid(row=0, column=1, padx=2)

        # Entry field for combo box
        self.text_cSearchBar=StringVar()
        textcSearchBar = ttk.Entry(labelTableframeright,textvariable=self.text_cSearchBar, width=30)
        textcSearchBar.grid(row=0, column=2, padx=2)

        # Search Button
        btnSearch = Button(labelTableframeright,command=self.search, text="Search", font=("Arial", 12), bg="black", fg="gold", width=15)
        btnSearch.grid(row=0, column=3, padx=1)

        # Show all Button
        btnShow_all = Button(labelTableframeright,command=self.fetch_data, text="Show all", font=("Arial", 12), bg="black", fg="gold", width=15)
        btnShow_all.grid(row=0, column=4, padx=1)

        # Details table frame
        Details_table_frame = Frame(labelTableframeright, bd=2, relief=RIDGE)
        Details_table_frame.place(x=0, y=45, width=780, height=400)

        # Scrollbars for the table
        scrol_x = Scrollbar(Details_table_frame, orient=HORIZONTAL)
        scrol_y = Scrollbar(Details_table_frame, orient=VERTICAL)

        self.Payment_details_table = ttk.Treeview(Details_table_frame, columns=("Customer ID", "Payment ID", "Payment Mode", "Payment Date", "Amount"), xscrollcommand=scrol_x.set, yscrollcommand=scrol_y.set)
        scrol_x.pack(side=BOTTOM, fill=X)
        scrol_y.pack(side=RIGHT, fill=Y)

        scrol_x.config(command=self.Payment_details_table.xview)
        scrol_y.config(command=self.Payment_details_table.yview)

        # Setting headings
        headings = ("Customer ID", "Payment ID", "Payment Mode", "Payment Date", "Amount")
        for i, heading in enumerate(headings):
            self.Payment_details_table.heading(i, text=heading)
            self.Payment_details_table.column(i, width=150)

        self.fetch_data()
        self.Payment_details_table["show"] = "headings"
        self.Payment_details_table.pack(fill=BOTH, expand=1)
        self.Payment_details_table.bind("<ButtonRelease-1>",self.get_cursor)

        # Validation for user
    def add_data(self):
        if self.var_Customer_ID.get() == "" or self.var_Amount.get() == "":
            messagebox.showerror("Error", "Please Fill All Details", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="atulakulamul990", database="hotelmanagementsystem")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO Payment VALUES (%s,%s,%s,%s,%s)",
                                    (self.var_Customer_ID.get(), self.var_Payment_ID.get(), self.var_Payment_Mode.get(), self.var_Paymment_Date.get(),
                                    self.var_Amount.get()
                                    ))
                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("Success", "Payment Added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="atulakulamul990", database="hotelmanagementsystem")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM Payment")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Payment_details_table.delete(*self.Payment_details_table.get_children())
            for i in rows:
                self.Payment_details_table.insert("", END, values=i)
            conn.commit()
        conn.close()
    def get_cursor(self, event=""):
        cursor_row = self.Payment_details_table.focus()
        content = self.Payment_details_table.item(cursor_row)
        row = content["values"]
        self.var_Customer_ID.set(row[0])
        self.var_Payment_ID.set(row[1])
        self.var_Payment_Mode.set(row[2])
        self.var_Paymment_Date.set(row[3])
        self.var_Amount.set(row[4])

    def Update(self):
        if self.var_Customer_ID.get() == "" or self.var_Payment_ID.get() == "":
            messagebox.showerror("Error", "Please Enter the Contact", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="atulakulamul990", database="hotelmanagementsystem")
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE Payment SET `Payment ID`=%s,`Payment Mode`=%s,`Payment Date`=%s,`Amount`=%s Where `Customer ID`=%s",(
                self.var_Payment_ID.get(), self.var_Payment_Mode.get(), self.var_Paymment_Date.get(),
                self.var_Amount.get(),self.var_Customer_ID.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Paymment Details have been updated", parent=self.root)

    def mDelete(self):
        mDelete = messagebox.askyesno("hotelmanagementsystem", "Do you want to delete this Customer", parent=self.root)
        if mDelete:
            conn = mysql.connector.connect(host="localhost", username="root", password="atulakulamul990", database="hotelmanagementsystem")
            my_cursor = conn.cursor()
            query = "DELETE FROM Payment WHERE `Customer ID`=%s" 
            values = (self.var_Customer_ID.get(),)
            my_cursor.execute(query, values)
            conn.commit()
            self.fetch_data()
            conn.close()
        else:
            return  # return if the user chooses not to delete

    def reset(self):
        self.var_Customer_ID.set(""),
        # self.var_Payment_ID.set(""),
        self.var_Payment_Mode.set(""),
        self.var_Paymment_Date.set(""),
        self.var_Amount.set("")

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="atulakulamul990", database="hotelmanagementsystem")
        my_cursor = conn.cursor()

        # Removed unnecessary backticks around the column name
        my_cursor.execute("SELECT * FROM Payment WHERE `" + str(self.search_var.get()) + "` LIKE '%" + str(self.text_cSearchBar.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Payment_details_table.delete(*self.Payment_details_table.get_children())
            for i in rows:
                self.Payment_details_table.insert("", END, values=i)
            conn.commit()
        conn.close()

if __name__ == "__main__":
    root = Tk()
    obj = Payment_Win(root)
    root.mainloop()