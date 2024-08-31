from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
from tkinter import messagebox
import mysql.connector

class floor_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1306x530+220+255")

        #variable for msql
        self.var_Total_Rooms = StringVar()
        self.var_Rooms_Occupied = StringVar()
        self.var_Floor_Manager_ID = StringVar()
        x=random.randint(1000,9999)
        self.var_Floor_Manager_ID.set(str(x))
        self.var_Floor_Number = StringVar()
        self.var_Avalable_Rooms = StringVar()

        # Title of Project
        lbl_title = Label(self.root, text=" ADD Floor Details", font=("times new roman", 19, "bold"), bg="black", fg="white", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1306, height=50)

        # Logo of Hotel         
        img2 = Image.open("C:/Users/amulb/OneDrive/Desktop/DBMS project/photos/1633410403702hotel-images/hotel images/logoofhotel.jpeg")
        img2 = img2.resize((80, 43), Image.ADAPTIVE)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg2.place(x=5, y=3, width=80, height=43)

        # Label frame
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Floor Details", padx=2, font=("times new roman", 19, "bold"))
        labelframeleft.place(x=5, y=50, width=500, height=470)

        #Total Rooms
        lbl_Total_Rooms = Label(labelframeleft, text="Total Rooms -", padx=2, pady=6)
        lbl_Total_Rooms.grid(row=0, column=0, sticky=W)  

        eTotal_Rooms = ttk.Entry(labelframeleft,textvariable=self.var_Total_Rooms, width=25)
        eTotal_Rooms.grid(row=0, column=1)

        #Rooms Occupied
        lbl_Rooms_Occupied = Label(labelframeleft, text="Rooms Occupied -", padx=2, pady=6)
        lbl_Rooms_Occupied.grid(row=1, column=0, sticky=W)  

        eRooms_Occupied = ttk.Entry(labelframeleft,textvariable=self.var_Rooms_Occupied, width=25)
        eRooms_Occupied.grid(row=1, column=1)

        #Floor manager ID
        lbl_FloorManager_Id = Label(labelframeleft, text="Floor Manager ID -", padx=2, pady=6)
        lbl_FloorManager_Id.grid(row=2, column=0, sticky=W)  

        eFloorManager_Id = ttk.Entry(labelframeleft,textvariable=self.var_Floor_Manager_ID,state="readonly", width=25)
        eFloorManager_Id.grid(row=2, column=1)

        #Floor No
        lbl_FloorNO = Label(labelframeleft, text="Floor Numbers -", padx=2, pady=6)
        lbl_FloorNO.grid(row=3, column=0, sticky=W)  

        eFloorNO = ttk.Entry(labelframeleft,textvariable=self.var_Floor_Number, width=25)
        eFloorNO.grid(row=3, column=1)

        #Avalable Rooms
        lbl_Avalable_Rooms = Label(labelframeleft, text="Avalable Rooms -", padx=2, pady=6)
        lbl_Avalable_Rooms.grid(row=4, column=0, sticky=W)  

        eAvalable_Rooms = ttk.Entry(labelframeleft,textvariable=self.var_Avalable_Rooms, width=25)
        eAvalable_Rooms.grid(row=4, column=1)


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
        combo_search_bar["values"] = ("Total rooms", "Rooms Occupied", "Floor Manager ID", "Floor Number", "Avalable Rooms")
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

        self.Floor_details_table = ttk.Treeview(Details_table_frame, columns=("Total rooms", "Rooms Occupied", "Floor Manager ID", "Floor Number", "Avalable Rooms"), xscrollcommand=scrol_x.set, yscrollcommand=scrol_y.set)
        scrol_x.pack(side=BOTTOM, fill=X)
        scrol_y.pack(side=RIGHT, fill=Y)

        scrol_x.config(command=self.Floor_details_table.xview)
        scrol_y.config(command=self.Floor_details_table.yview)

        # Setting headings
        headings = ("Total rooms", "Rooms Occupied", "Floor Manager ID", "Floor Number", "Avalable Rooms")
        for i, heading in enumerate(headings):
            self.Floor_details_table.heading(i, text=heading)
            self.Floor_details_table.column(i, width=150)

        self.fetch_data()
        self.Floor_details_table["show"] = "headings"
        self.Floor_details_table.pack(fill=BOTH, expand=1)
        self.Floor_details_table.bind("<ButtonRelease-1>",self.get_cursor)

        # Validation for user
    def add_data(self):
        if self.var_Total_Rooms.get() == "" or self.var_Floor_Manager_ID.get() == "":
            messagebox.showerror("Error", "Please Fill in All the Details", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="atulakulamul990", database="hotelmanagementsystem")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO Floor VALUES (%s,%s,%s,%s,%s)",
                                    (self.var_Total_Rooms.get(), self.var_Rooms_Occupied.get(), self.var_Floor_Manager_ID.get(), self.var_Floor_Number.get(),
                                    self.var_Avalable_Rooms.get()
                                    ))
                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("Success", "Floor Added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="atulakulamul990", database="hotelmanagementsystem")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM Floor")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Floor_details_table.delete(*self.Floor_details_table.get_children())
            for i in rows:
                self.Floor_details_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.Floor_details_table.focus()
        content = self.Floor_details_table.item(cursor_row)
        row = content["values"]
        self.var_Total_Rooms.set(row[0])
        self.var_Rooms_Occupied.set(row[1])
        self.var_Floor_Manager_ID.set(row[2])
        self.var_Floor_Number.set(row[3])
        self.var_Avalable_Rooms.set(row[4])

    def Update(self):
        if self.var_Floor_Manager_ID.get() == "" or self.var_Rooms_Occupied.get() == "":
            messagebox.showerror("Error", "Please Enter the Contact", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="atulakulamul990", database="hotelmanagementsystem")
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE Floor SET `Total rooms`=%s, `Rooms Occupied`=%s, `Floor Number`=%s, `Avalable Rooms`=%s WHERE `Floor Manager ID`=%s", (
                self.var_Total_Rooms.get(), self.var_Rooms_Occupied.get(),  self.var_Floor_Number.get(),
                self.var_Avalable_Rooms.get(), self.var_Floor_Manager_ID.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Floor Details have been updated", parent=self.root)

            
    def mDelete(self):
        mDelete = messagebox.askyesno("hotelmanagementsystem", "Do you want to delete this Customer", parent=self.root)
        if mDelete:
            conn = mysql.connector.connect(host="localhost", username="root", password="atulakulamul990", database="hotelmanagementsystem")
            my_cursor = conn.cursor()
            query = "DELETE FROM Floor WHERE `Floor Manager ID`=%s" 
            values = (self.var_Floor_Manager_ID.get(),)
            my_cursor.execute(query, values)
            conn.commit()
            self.fetch_data()
            conn.close()
        else:
            return  # return if the user chooses not to delete
    
    def reset(self):
        self.var_Total_Rooms.set(""),
        self.var_Rooms_Occupied.set(""),
        # self.var_Floor_Manager_ID.set(""),
        self.var_Floor_Number.set(""),
        self.var_Avalable_Rooms.set("")

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="atulakulamul990", database="hotelmanagementsystem")
        my_cursor = conn.cursor()

        # Removed unnecessary backticks around the column name
        my_cursor.execute("SELECT * FROM Floor WHERE `" + str(self.search_var.get()) + "` LIKE '%" + str(self.text_cSearchBar.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Floor_details_table.delete(*self.Floor_details_table.get_children())
            for i in rows:
                self.Floor_details_table.insert("", END, values=i)
            conn.commit()
        conn.close()


if __name__ == "__main__":
    root=Tk()
    obj = floor_Win(root)
    root.mainloop()
