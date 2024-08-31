from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
from tkinter import messagebox
import mysql.connector 

class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1306x530+220+255")


        #variable for msql
        self.var_Customer_ID = StringVar()
        x=random.randint(1000,9999)
        self.var_Customer_ID.set(str(x))

        self.var_Customer_Name = StringVar()
        self.var_Gender = StringVar()
        self.var_E_mail = StringVar()
        self.var_Customer_address = StringVar()
        self.var_Date_of_Birth = StringVar()
        self.var_Room_no = StringVar()
        self.var_Room_type = StringVar()
        self.var_Floor = StringVar()
        self.var_Contact = StringVar()
        self.var_Check_in_Date = StringVar()
        self.var_Check_out_Date = StringVar()
        self.var_Persions_with_customer = StringVar()
        self.var_varification_Mode = StringVar()

        self.search_var=StringVar()

        # Title of Project
        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 19, "bold"), bg="black", fg="white", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1306, height=50)

        # Logo of Hotel         
        img2 = Image.open("C:/Users/amulb/OneDrive/Desktop/DBMS project/photos/1633410403702hotel-images/hotel images/logoofhotel.jpeg")
        img2 = img2.resize((80, 43), Image.ADAPTIVE)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg2.place(x=5, y=3, width=80, height=43)

        # Label frame
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", padx=2, font=("times new roman", 19, "bold"))
        labelframeleft.place(x=5, y=50, width=500, height=470)

        # Labels and entries
        #customer Id
        lbl_cust_ref = Label(labelframeleft, text="Customer ID -", padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)  

        entry_ref = ttk.Entry(labelframeleft,textvariable=self.var_Customer_ID,state="readonly", width=25)
        entry_ref.grid(row=0, column=1)

        # Customer name 
        cname = Label(labelframeleft, text="Customer Name - ", padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)  
        
        textcname = ttk.Entry(labelframeleft,textvariable=self.var_Customer_Name, width=25)
        textcname.grid(row=1, column=1)

        # Gender of customer
        c_gender = Label(labelframeleft, text="Gender - ", padx=2, pady=6)
        c_gender.grid(row=2, column=0, sticky=W) 

        combo_gender = ttk.Combobox(labelframeleft,textvariable=self.var_Gender, width=22, state="readonly")
        # combo_gender.current(0)
        combo_gender["values"]= ("Male", "Female", "Other")
        combo_gender.grid(row=2, column=1)

        #customer DOB
        cDOB = Label(labelframeleft, text="Date_of_Birth  - ", padx=2, pady=6)
        cDOB.grid(row=3, column=0, sticky=W)  
        
        textcDOB = ttk.Entry(labelframeleft,textvariable=self.var_Date_of_Birth, width=25)
        textcDOB.grid(row=3, column=1)

        # Customer Room NO 
        croomNo = Label(labelframeleft, text="Room No - ", padx=2, pady=6)
        croomNo.grid(row=4, column=0, sticky=W)  
        
        textcroomNo = ttk.Entry(labelframeleft,textvariable=self.var_Room_no, width=25)
        textcroomNo.grid(row=4, column=1)

        #customer Room Type 
        croomType = Label(labelframeleft, text="Rooom Type - ", padx=2, pady=6)
        croomType.grid(row=5, column=0, sticky=W)  
        
        textcroomType = ttk.Combobox(labelframeleft, textvariable=self.var_Room_type,width=22, state="readonly")
        #combo_verificatio_Mode.current(0)
        textcroomType["values"]= ("AC", "Non-AC", "Delux","Super Delux")
        textcroomType.grid(row=5, column=1)

        #Customer Floor 
        cFloor = Label(labelframeleft, text="Floor - ", padx=2, pady=6)
        cFloor.grid(row=6, column=0, sticky=W)  
        
        textcFloor = ttk.Entry(labelframeleft, textvariable=self.var_Floor,width=25)
        textcFloor.grid(row=6, column=1)

        #customer Address
        cAddress = Label(labelframeleft, text="Customer Address - ", padx=2, pady=6)
        cAddress.grid(row=7, column=0, sticky=W)  
        
        textcAddress = ttk.Entry(labelframeleft,textvariable=self.var_Customer_address, width=25)
        textcAddress.grid(row=7, column=1)

        #Customer Contact
        cContact = Label(labelframeleft, text="Contact - ", padx=2, pady=6)
        cContact.grid(row=8, column=0, sticky=W)  
        
        textcContact = ttk.Entry(labelframeleft, textvariable=self.var_Contact,width=25)
        textcContact.grid(row=8, column=1)

        #customer E - mail
        cE_mail = Label(labelframeleft, text="E-mail - ", padx=2, pady=6)
        cE_mail.grid(row=9, column=0, sticky=W)  
        
        textcE_mail = ttk.Entry(labelframeleft,textvariable=self.var_E_mail, width=25)
        textcE_mail.grid(row=9, column=1)

        #Check_in_date of customer
        cCheck_in_Date = Label(labelframeleft, text="Check_in_Date - ", padx=2, pady=6)
        cCheck_in_Date.grid(row=10, column=0, sticky=W)  
        
        textcCheck_in_Date = ttk.Entry(labelframeleft,textvariable=self.var_Check_in_Date, width=25)
        textcCheck_in_Date.grid(row=10, column=1)

        #check_out_Date of customer
        cCheck_out_Date = Label(labelframeleft, text="Check_out_Date - ", padx=2, pady=6)
        cCheck_out_Date.grid(row=11, column=0, sticky=W)  
        
        textcCheck_out_Date = ttk.Entry(labelframeleft,textvariable=self.var_Check_out_Date, width=25)
        textcCheck_out_Date.grid(row=11, column=1)

    


        #Customer Members
        cMembers = Label(labelframeleft, text="Persons with Customer - ", padx=2, pady=6)
        cMembers.grid(row=12, column=0, sticky=W)
        
        textcMembers = ttk.Entry(labelframeleft, textvariable=self.var_Persions_with_customer,width=25)
        textcMembers.grid(row=12, column=1)

        #customer verification Mode
        cvarification_Mode = Label(labelframeleft, text="Varification_Mode - ", padx=2, pady=6)
        cvarification_Mode.grid(row=13, column=0, sticky=W)  
        
        combo_verificatio_Mode = ttk.Combobox(labelframeleft, textvariable=self.var_varification_Mode,width=22, state="readonly")
        #combo_verificatio_Mode.current(0)
        combo_verificatio_Mode["values"]= ("Aadhar Card", "Pan Card", "Voter ID")
        combo_verificatio_Mode.grid(row=13, column=1)

        #buttons frames ADD,Delete,Update,Reset
        btn_frame = Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=300,y=5,width=190,height=200)

        #add button
        btnAdd= Button(btn_frame,text= "Add",command=self.add_data,font=( "Arial",12),bg="black",fg="white",width=20,height=2)
        btnAdd.grid(row=0,column=0,padx=1)

        #delete  button
        btnDelete= Button(btn_frame,text= "Delete",command=self.mDelete,font=( "Arial",12),bg="black",fg="white",width=20,height=2)
        btnDelete.grid(row=1,column=0,padx=1)

        #update button
        btnUpdate= Button(btn_frame,text= "Update",command=self.Update,font=( "Arial",12),bg="black",fg="white",width=20,height=2)
        btnUpdate.grid(row=2,column=0,padx=1)

        #aReset button
        btnReset= Button(btn_frame,text= "Reset",command=self.reset,font=( "Arial",12),bg="black",fg="white",width=20,height=2)
        btnReset.grid(row=3,column=0,padx=1)

       # Table frame on the right side
        labelTableframeright = LabelFrame(self.root, bd=2, relief=RIDGE, text="The Details ", padx=2, font=("times new roman", 19, "bold"))
        labelTableframeright.place(x=510, y=50, width=790, height=470)

        # Search By Label
        cSearchbar = Label(labelTableframeright, text="Search By",font="bold", fg="black")
        cSearchbar.grid(row=0, column=0, sticky=W, padx=2)  

        
        # Search Bar Combobox
        combo_search_bar = ttk.Combobox(labelTableframeright,textvariable=self.search_var, width=30, state="readonly")
        combo_search_bar["values"] = ("Customer ID", "Customer Name", "Contact", "Gender", "Email", "Address", "Date_of_Birth", "Room NO", "Room Type", "Floor", "Check_in_Date", "Check_out_Date", "Persons with Customer", "Verification Mode",)
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

        self.cust_details_table = ttk.Treeview(Details_table_frame, columns=("Customer ID", "Customer Name", "Gender", "Email", "Date_of_Birth", "Room NO", "Room Type", "Floor", "Customer Address","Contact", "Check_in_Date", "Check_out_Date", "Persons with Customer", "Verification Mode"), xscrollcommand=scrol_x.set, yscrollcommand=scrol_y.set)
        scrol_x.pack(side=BOTTOM, fill=X)
        scrol_y.pack(side=RIGHT, fill=Y)

        scrol_x.config(command=self.cust_details_table.xview)
        scrol_y.config(command=self.cust_details_table.yview)


        # Setting headings
        headings = ("Customer ID", "Customer Name", "Gender",  "Date_of_Birth", "Room NO", "Room Type", "Floor", "Customer Address","Contact", "Email","Check_in_Date", "Check_out_Date", "Persons with Customer", "Verification Mode")
        for i, heading in enumerate(headings):
            self.cust_details_table.heading(i, text=heading)
            self.cust_details_table.column(i, width=100)

        self.cust_details_table["show"] = "headings"
        self.cust_details_table.pack(fill=BOTH, expand=1)
        self.cust_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    # Validation for user
    def add_data(self):
        if self.var_Contact.get() == "" or self.var_E_mail.get() == "":
            messagebox.showerror("Error", "Please Fill in All the Details", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="atulakulamul990", database="hotelmanagementsystem")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO Customer VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                    (self.var_Customer_ID.get(), self.var_Customer_Name.get(), self.var_Gender.get(), self.var_Date_of_Birth.get(),
                                    self.var_Room_no.get(), self.var_Room_type.get(), self.var_Floor.get(), self.var_Customer_address.get(),
                                    self.var_Contact.get(), self.var_E_mail.get(), self.var_Check_in_Date.get(), self.var_Check_out_Date.get(),
                                    self.var_Persions_with_customer.get(), self.var_varification_Mode.get()))
                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("Success", "Customer Added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    #fetch data from Databases.
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="atulakulamul990", database="hotelmanagementsystem")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM Customer")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("", END, values=i)
            conn.commit()
        conn.close()
        
    #get the all entries in enrity frame and then we can delete and update the value
    def get_cursor(self, event=""):
        cursor_row = self.cust_details_table.focus()
        content = self.cust_details_table.item(cursor_row)
        row = content["values"]
        self.var_Customer_ID.set(row[0])
        self.var_Customer_Name.set(row[1])
        self.var_Gender.set(row[2])
        self.var_Date_of_Birth.set(row[3])
        self.var_Room_no.set(row[4])
        self.var_Room_type.set(row[5])
        self.var_Floor.set(row[6])
        self.var_Customer_address.set(row[7])
        self.var_Contact.set(row[8])
        self.var_E_mail.set(row[9])
        
        self.var_Check_in_Date.set(row[10])
        self.var_Check_out_Date.set(row[11])
        self.var_Persions_with_customer.set(row[12])
        self.var_varification_Mode.set(row[13])

    def Update(self):
        if self.var_Contact.get() == "" or self.var_Customer_Name.get() == "":
            messagebox.showerror("Error", "Please Enter the Contact", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="atulakulamul990", database="hotelmanagementsystem")
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE customer SET `Customer Name`=%s, Gender=%s, Date_of_Birth=%s, `Room NO`=%s, `Room Type`=%s, Floor=%s, `Customer Address`=%s, `Contact`=%s, `Email`=%s, `Check_in_Date`=%s, `Check_out_Date`=%s,`Persons with Customer`=%s, `Verification Mode`=%s WHERE `Customer Id`=%s", (
                self.var_Customer_Name.get(), self.var_Gender.get(), self.var_E_mail.get(), self.var_Customer_address.get(), self.var_Date_of_Birth.get(),
                self.var_Room_no.get(), self.var_Room_type.get(), self.var_Floor.get(), 
                self.var_Contact.get(), self.var_Check_in_Date.get(), self.var_Check_out_Date.get(),self.var_Persions_with_customer.get(),
                self.var_varification_Mode.get(), self.var_Customer_ID.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Customer Details have been updated", parent=self.root)

    def mDelete(self):
        mDelete = messagebox.askyesno("hotelmanagementsystem", "Do you want to delete this Customer", parent=self.root)
        if mDelete:
            conn = mysql.connector.connect(host="localhost", username="root", password="atulakulamul990", database="hotelmanagementsystem")
            my_cursor = conn.cursor()
            query = "DELETE FROM customer WHERE `Customer ID`=%s" 
            values = (self.var_Customer_ID.get(),)
            my_cursor.execute(query, values)
            conn.commit()
            self.fetch_data()
            conn.close()
        else:
            return  # return if the user chooses not to delete

    def reset(self):
        # self.var_Customer_ID.set(""),
        self.var_Customer_Name.set(""),
        self.var_Gender.set(""),
        self.var_E_mail.set(""),
        self.var_Customer_address.set(""),
        self.var_Date_of_Birth.set(""),
        self.var_Room_no.set(""),
        self.var_Room_type.set(""),
        self.var_Floor.set(""),
        self.var_Contact.set(""),
        self.var_Check_in_Date.set(""),
        self.var_Check_out_Date.set(""),
        self.var_Persions_with_customer.set(""),
        self.var_varification_Mode.set("")

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="atulakulamul990", database="hotelmanagementsystem")
        my_cursor = conn.cursor()

        # Remove the double quotes around the column name
        my_cursor.execute("SELECT * FROM Customer WHERE `" + str(self.search_var.get()) + "` LIKE '%" + str(self.text_cSearchBar.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("", END, values=i)
            conn.commit()
        conn.close()










if __name__ == "__main__":
    root=Tk()
    obj = Cust_Win(root)
    root.mainloop()
