from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
from tkinter import messagebox
import mysql.connector

class Emp_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1306x530+220+255")

        #variable for msql
        self.var_Employee_ID = StringVar()
        x=random.randint(1000,9999)
        self.var_Employee_ID.set(str(x))
        self.var_EmployeeName = StringVar()
        self.var_Post = StringVar()
        self.var_Salary = StringVar()
        self.var_EmployeeDOB = StringVar()
        self.var_Gender = StringVar()
        self.var_EmployeeAddress = StringVar()
        self.var_EmployeeContact = StringVar()

        # Title of Project
        lbl_title = Label(self.root, text="ADD Employee Details", font=("times new roman", 19, "bold"), bg="black", fg="white", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1306, height=50)

        # Logo of Hotel         
        img2 = Image.open("C:/Users/amulb/OneDrive/Desktop/DBMS project/photos/1633410403702hotel-images/hotel images/logoofhotel.jpeg")
        img2 = img2.resize((80, 43), Image.ADAPTIVE)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg2.place(x=5, y=3, width=80, height=43)

        # Label frame
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Employee Details", padx=2, font=("times new roman", 19, "bold"))
        labelframeleft.place(x=5, y=50, width=500, height=470)

        # Labels and entries
        # Employee ID
        lbl_EmployeeId = Label(labelframeleft, text="Employee ID -", padx=2, pady=6)
        lbl_EmployeeId.grid(row=0, column=0, sticky=W)  

        eEmployeeId = ttk.Entry(labelframeleft,textvariable=self.var_Employee_ID,state="readonly", width=25)
        eEmployeeId.grid(row=0, column=1)

        # Employee Name
        lbl_EmployeeName = Label(labelframeleft, text="Name - ", padx=2, pady=6)
        lbl_EmployeeName.grid(row=1, column=0, sticky=W) 

        eEmployeeName = ttk.Entry(labelframeleft,textvariable=self.var_EmployeeName, width=25)
        eEmployeeName.grid(row=1, column=1)

        # Employee Post
        lbl_EmployeePost = Label(labelframeleft, text="Post - ", padx=2, pady=6)
        lbl_EmployeePost.grid(row=2, column=0, sticky=W)  

        combo_EmpolyeePost = ttk.Combobox(labelframeleft,textvariable=self.var_Post, width=22, state="readonly")
        combo_EmpolyeePost["values"]= ("Manager", "Employee", "Waitor", "Janitors", "Room_service", "Receptionist")
        combo_EmpolyeePost.grid(row=2, column=1)

        # Employee Salary
        lbl_EmployeeSalary = Label(labelframeleft, text="Salary - ", padx=2, pady=6)
        lbl_EmployeeSalary.grid(row=3, column=0, sticky=W) 

        eEmployeeSalary = ttk.Entry(labelframeleft,textvariable=self.var_Salary, width=25)
        eEmployeeSalary.grid(row=3, column=1)

        # Employee DOB
        lbl_EmployeeDOB = Label(labelframeleft, text="Date of Birth - ", padx=2, pady=6)
        lbl_EmployeeDOB.grid(row=4, column=0, sticky=W) 

        eEmployeeDOB =ttk.Entry(labelframeleft,textvariable=self.var_EmployeeDOB, width=25,)
        eEmployeeDOB.grid(row=4, column=1)

        # Employee Gender
        lbl_EmployeeGender = Label(labelframeleft, text="Gender - ", padx=2, pady=6)
        lbl_EmployeeGender.grid(row=5, column=0, sticky=W) 

        combo_EmpolyeeGender = ttk.Combobox(labelframeleft,textvariable=self.var_Gender, width=22, state="readonly")
        combo_EmpolyeeGender["values"]= ("Male", "Female", "Other")
        combo_EmpolyeeGender.grid(row=5, column=1)

        # Employee Address
        lbl_EmployeeAddress = Label(labelframeleft, text="Address - ", padx=2, pady=6)
        lbl_EmployeeAddress.grid(row=6, column=0, sticky=W) 

        eEmployeeAddress = ttk.Entry(labelframeleft,textvariable=self.var_EmployeeAddress, width=25)
        eEmployeeAddress.grid(row=6, column=1)

        # Employee Contact
        lbl_EmployeeContact = Label(labelframeleft, text="Contact - ", padx=2, pady=6)
        lbl_EmployeeContact.grid(row=7, column=0, sticky=W) 

        eEmployeeContact = ttk.Entry(labelframeleft,textvariable=self.var_EmployeeContact, width=25)
        eEmployeeContact.grid(row=7, column=1)

        #button
        btn_frame = Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=10,y=300,width=400,height=35)

        #add button
        btnAdd= Button(btn_frame,text= "Add",command=self.add_data,font=( "Arial",12),bg="black",fg="white",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        #delete button
        btnDelete= Button(btn_frame,text= "Delete",command=self.mDelete,font=( "Arial",12),bg="black",fg="white",width=10)
        btnDelete.grid(row=0,column=1,padx=1)

        #update button
        btnUpdate= Button(btn_frame,text= "Update",command=self.Update,font=( "Arial",12),bg="black",fg="white",width=10)
        btnUpdate.grid(row=0,column=2,padx=1)

        #aReset button
        btnReset= Button(btn_frame,text= "Reset",command=self.reset,font=( "Arial",12),bg="black",fg="white",width=10)
        btnReset.grid(row=0,column=3,padx=1)

          #Table frame in right side
         # Label frame
        labelTableframeright = LabelFrame(self.root, bd=2, relief=RIDGE, text="The Details", padx=2, font=("times new roman", 19, "bold"))
        labelTableframeright.place(x=510, y=50, width=790, height=470)

         # Search By Label
        cSearchbar = Label(labelTableframeright, text="Search By", bg="black", fg="white")
        cSearchbar.grid(row=0, column=0, sticky=W, padx=2)  

        # Search Bar Combobox
        self.search_var=StringVar()
        combo_search_bar = ttk.Combobox(labelTableframeright,textvariable=self.search_var, width=30, state="readonly")
        combo_search_bar["values"] = ("Employee ID", "Name", "Post", "Salary", "Date_of_Birsth", "Gender", "Address", "Contact")
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

        self.Emp_details_table = ttk.Treeview(Details_table_frame, columns=("Employee ID", "Name", "Post", "Salary", "Date_of_Birth", "Gender", "Address", "Contact"), xscrollcommand=scrol_x.set, yscrollcommand=scrol_y.set)
        scrol_x.pack(side=BOTTOM, fill=X)
        scrol_y.pack(side=RIGHT, fill=Y)

        scrol_x.config(command=self.Emp_details_table.xview)
        scrol_y.config(command=self.Emp_details_table.yview)

    # Setting headings
        headings = ("Employee ID", "Name", "Post", "Salary", "Date_of_Birth", "Gender", "Address", "Contact")
        for i, heading in enumerate(headings):
            self.Emp_details_table.heading(i, text=heading)
            self.Emp_details_table.column(i, width=100)

        self.fetch_data()
        self.Emp_details_table["show"] = "headings"
        self.Emp_details_table.pack(fill=BOTH, expand=1)
        self.Emp_details_table.bind("<ButtonRelease-1>",self.get_cursor)
     

    # Validation for user
    def add_data(self):
        if self.var_EmployeeName.get() == "" or self.var_Employee_ID.get() == "":
            messagebox.showerror("Error", "Please Fill in All the Details", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="atulakulamul990", database="hotelmanagementsystem")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO Employee VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                                    (self.var_Employee_ID.get(), self.var_EmployeeName.get(), self.var_Post.get(), self.var_Salary.get(),
                                    self.var_EmployeeDOB.get(), self.var_Gender.get(), self.var_EmployeeAddress.get(), self.var_EmployeeContact.get()))
                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("Success", "Employee Added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="atulakulamul990", database="hotelmanagementsystem")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM Employee")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Emp_details_table.delete(*self.Emp_details_table.get_children())
            for i in rows:
                self.Emp_details_table.insert("", END, values=i)
            conn.commit()
        conn.close()
    #get the all entries in enrity frame and then we can delete and update the value
    def get_cursor(self, event=""):
        cursor_row = self.Emp_details_table.focus()
        content = self.Emp_details_table.item(cursor_row)
        row = content["values"]
        self.var_Employee_ID.set(row[0])
        self.var_EmployeeName.set(row[1])
        self.var_Post.set(row[2])
        self.var_Salary.set(row[3])
        self.var_EmployeeDOB.set(row[4])
        self.var_Gender.set(row[5])
        self.var_EmployeeAddress.set(row[6])
        self.var_EmployeeContact.set(row[7])

    def Update(self):
        if self.var_EmployeeContact.get() == "" or self.var_EmployeeName.get() == "":
            messagebox.showerror("Error", "Please Enter the Contact", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="atulakulamul990", database="hotelmanagementsystem")
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE Employee SET `Name`=%s, `Post`=%s, `Salary`=%s, `Date_of_Birth`=%s, `Gender`=%s, `Address`=%s, `Contact`=%s WHERE `Employee_ID`=%s", (
                self.var_EmployeeName.get(), self.var_Post.get(), self.var_Salary.get(),
                self.var_EmployeeDOB.get(), self.var_Gender.get(), self.var_EmployeeAddress.get(), self.var_EmployeeContact.get(), self.var_Employee_ID.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Employee Details have been updated", parent=self.root)

    def mDelete(self):
        mDelete = messagebox.askyesno("hotelmanagementsystem", "Do you want to delete this Customer", parent=self.root)
        if mDelete:
            conn = mysql.connector.connect(host="localhost", username="root", password="atulakulamul990", database="hotelmanagementsystem")
            my_cursor = conn.cursor()
            query = "DELETE FROM Employee WHERE `Employee_ID`=%s" 
            values = (self.var_Employee_ID.get(),)
            my_cursor.execute(query, values)
            conn.commit()
            self.fetch_data()
            conn.close()
        else:
            return  # return if the user chooses not to delete
        
    def reset(self):
        # self.var_Employee_ID.set(""),
        self.var_EmployeeName.set(""),
        self.var_Post.set(""),
        self.var_Salary.set(""),
        self.var_EmployeeDOB.set(""),
        self.var_Gender.set(""),
        self.var_EmployeeAddress.set(""),
        self.var_EmployeeContact.set("")
    
    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="atulakulamul990", database="hotelmanagementsystem")
        my_cursor = conn.cursor()

        # Removed unnecessary backticks around the column name
        my_cursor.execute("SELECT * FROM Employee WHERE `" + str(self.search_var.get()) + "` LIKE '%" + str(self.text_cSearchBar.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Emp_details_table.delete(*self.Emp_details_table.get_children())
            for i in rows:
                self.Emp_details_table.insert("", END, values=i)
            conn.commit()
        conn.close()



        
if __name__ == "__main__":
    root=Tk()
    obj = Emp_Win(root)
    root.mainloop()
