from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class Rooms_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1306x530+220+255")

        #variable for msql
        self.var_Room_Number = StringVar()
        self.var_Room_Type = StringVar()
        self.var_Room_Prize = StringVar()
        self.var_Floor = StringVar()
        self.var_Statue = StringVar()

        # Title of Project
        lbl_title = Label(self.root, text="ADD Rooms Details", font=("times new roman", 19, "bold"), bg="black", fg="white", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1306, height=50)

        # Logo of Hotel         
        img2 = Image.open("C:/Users/amulb/OneDrive/Desktop/DBMS project/photos/1633410403702hotel-images/hotel images/logoofhotel.jpeg")
        img2 = img2.resize((80, 43), Image.ADAPTIVE)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg2.place(x=5, y=3, width=80, height=43)

        # Label frame
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Rooms Details", padx=2, font=("times new roman", 19, "bold"))
        labelframeleft.place(x=5, y=50, width=500, height=470)

        #Rooms no
        lbl_Rooms_no= Label(labelframeleft, text="Rooms Number -", padx=2, pady=6)
        lbl_Rooms_no.grid(row=0, column=0, sticky=W)  

        eRooms_no = ttk.Entry(labelframeleft,textvariable=self.var_Room_Number, width=25)
        eRooms_no.grid(row=0, column=1)

        #room type
        lbl_Room_type = Label(labelframeleft, text="Rooms Type -", padx=2, pady=6)
        lbl_Room_type.grid(row=1, column=0, sticky=W)  

        combo_search_bar = ttk.Combobox(labelframeleft,textvariable=self.var_Room_Type, width=22, state="readonly")
        combo_search_bar["values"] = ("AC", "Non AC", "Delux","Super Delux")
        combo_search_bar.grid(row=1, column=1, padx=2)

        #Prize of Rooms
        lbl_Rooms_prize = Label(labelframeleft, text="Rooms Prize -", padx=2, pady=6)
        lbl_Rooms_prize.grid(row=2, column=0, sticky=W)  

        eRooms_prize = ttk.Entry(labelframeleft,textvariable=self.var_Room_Prize, width=25)
        eRooms_prize.grid(row=2, column=1)

        #Foor of the room
        lbl_Floor_of_the_room = Label(labelframeleft, text="Floor -", padx=2, pady=6)
        lbl_Floor_of_the_room.grid(row=3, column=0, sticky=W)  

        eFloor_of_the_room = ttk.Entry(labelframeleft,textvariable=self.var_Floor, width=25)
        eFloor_of_the_room.grid(row=3, column=1)

        #Satus of floor
        lbl_Status = Label(labelframeleft, text="Status -", padx=2, pady=6)
        lbl_Status.grid(row=4, column=0, sticky=W)  

        combo_Status = ttk.Combobox(labelframeleft, width=22,textvariable=self.var_Statue, state="readonly")
        combo_Status["values"]= ("Occupied", "Unoccupied")
        combo_Status.grid(row=4, column=1)


        #button
        btn_frame = Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=10,y=300,width=400,height=35)

        #add button
        btnAdd= Button(btn_frame,text= "Add",command=self.add_data,font=( "Arial",12),bg="black",fg="white",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        #Delete button
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
        combo_search_bar["values"] = ("Room Number", "Room Type", "Room Prize", "Floor", "Status")
        combo_search_bar.grid(row=0, column=1, padx=2)

        # Entry field for combo box
        self.text_cSearchBar=StringVar()
        textcSearchBar = ttk.Entry(labelTableframeright, textvariable=self.text_cSearchBar,width=30)
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

        self.Rooms_details_table = ttk.Treeview(Details_table_frame, columns=("Room Number", "Room Type", "Room Prize", "Floor", "Status"), xscrollcommand=scrol_x.set, yscrollcommand=scrol_y.set)
        scrol_x.pack(side=BOTTOM, fill=X)
        scrol_y.pack(side=RIGHT, fill=Y)

        scrol_x.config(command=self.Rooms_details_table.xview)
        scrol_y.config(command=self.Rooms_details_table.yview)

        # Setting headings
        headings = ("Room Number", "Room Type", "Room Prize", "Floor", "Status")
        for i, heading in enumerate(headings):
            self.Rooms_details_table.heading(i, text=heading)
            self.Rooms_details_table.column(i, width=150)

        self.Rooms_details_table["show"] = "headings"
        self.Rooms_details_table.pack(fill=BOTH, expand=1)
        self.Rooms_details_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    # Fetch data from the database
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="atulakulamul990", database="hotelmanagementsystem")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM Room")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Rooms_details_table.delete(*self.Rooms_details_table.get_children())
            for i in rows:
                self.Rooms_details_table.insert("", END, values=i)
            conn.commit()
        conn.close()
        
    # Function to add data
    def add_data(self):
        if self.var_Room_Number.get() == "" or self.var_Floor.get() == "":
            messagebox.showerror("Error", "Please Fill All Details", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="atulakulamul990", database="hotelmanagementsystem")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO Rooms VALUES (%s,%s,%s,%s,%s)",
                                    (self.var_Room_Number.get(), self.var_Room_Type.get(), self.var_Room_Prize.get(), self.var_Floor.get(),
                                    self.var_Statue.get()
                                    ))
                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("Success", "Rooms Added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="atulakulamul990", database="hotelmanagementsystem")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM Rooms")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Rooms_details_table.delete(*self.Rooms_details_table.get_children())
            for i in rows:
                self.Rooms_details_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.Rooms_details_table.focus()
        content = self.Rooms_details_table.item(cursor_row)
        row = content["values"]
        self.var_Room_Number.set(row[0])
        self.var_Room_Type.set(row[1])
        self.var_Room_Prize.set(row[2])
        self.var_Floor.set(row[3])
        self.var_Statue.set(row[4])

    def Update(self):
        if self.var_Room_Number.get() == "" or self.var_Statue.get() == "":
            messagebox.showerror("Error", "Please Enter the Contact", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="atulakulamul990", database="hotelmanagementsystem")
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE Rooms SET `Room Type`=%s, `Room Prize`=%s, `Floor`=%s, `Status`=%s WHERE `Room Number`=%s", (
                self.var_Room_Type.get(), self.var_Room_Prize.get(), self.var_Floor.get(),
                self.var_Statue.get(), self.var_Room_Number.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Rooms Details have been updated", parent=self.root)

    def mDelete(self):
        mDelete = messagebox.askyesno("hotelmanagementsystem", "Do you want to delete this Customer", parent=self.root)
        if mDelete:
            conn = mysql.connector.connect(host="localhost", username="root", password="atulakulamul990", database="hotelmanagementsystem")
            my_cursor = conn.cursor()
            query = "DELETE FROM Rooms WHERE `Room Number`=%s" 
            values = (self.var_Room_Number.get(),)
            my_cursor.execute(query, values)
            conn.commit()
            self.fetch_data()
            conn.close()
        else:
            return  # return if the user chooses not to delete

    def reset(self):
        self.var_Room_Number.set(""),
        self.var_Room_Type.set(""),
        self.var_Room_Prize.set(""),
        self.var_Floor.set(""),
        self.var_Statue.set("")

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="atulakulamul990", database="hotelmanagementsystem")
        my_cursor = conn.cursor()

        # Removed unnecessary backticks around the column name
        my_cursor.execute("SELECT * FROM Rooms WHERE `" + str(self.search_var.get()) + "` LIKE '%" + str(self.text_cSearchBar.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Rooms_details_table.delete(*self.Rooms_details_table.get_children())
            for i in rows:
                self.Rooms_details_table.insert("", END, values=i)
            conn.commit()
        conn.close()


if __name__ == "__main__":
    root=Tk()
    obj = Rooms_Win(root)
    root.mainloop()