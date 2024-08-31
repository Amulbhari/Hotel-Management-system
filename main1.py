from tkinter import *
from PIL import Image, ImageTk
from customer import Cust_Win
from Employee import Emp_Win
from Floor import floor_Win
from Payment import Payment_Win
from Rooms import Rooms_Win

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1800x800+0+0")

        # Title of Project
        lbl_title = Label(self.root, text="Hotel Management System", font=("times new roman", 40, "bold"), bg="black", fg="white", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1550, height=50)

        # Image1
        img1 = Image.open(r"C:\Users\amulb\OneDrive\Desktop\DBMS project\photos\1633410403702hotel-images\hotel images\hotel1.png")
        img1 = img1.resize((1555, 145), Image.ADAPTIVE)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lblimg = Label(self.root, image=self.photoimg1, bd=2, relief=RIDGE)
        lblimg.place(x=0, y=50, width=1555, height=145)

        # Logo of Hotel         
        img2 = Image.open(r"C:\Users\amulb\OneDrive\Desktop\DBMS project\photos\1633410403702hotel-images\hotel images\logoofhotel.jpeg")
        img2 = img2.resize((230, 200), Image.ADAPTIVE)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(self.root, image=self.photoimg2, bd=2, relief=RIDGE)
        lblimg2.place(x=0, y=2, width=230, height=200)

        # Main frame in this frame we add some stuff like (menu, customer, rooms etc)
        main_frame = Frame(self.root, bd=2, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1800, height=600)

        # Label menu in main frame 
        lbl_menu = Label(main_frame, text="Menu", font=("times new roman", 20, "bold"), bg="black", fg="white", bd=2, relief=RIDGE, cursor="hand2")
        lbl_menu.place(x=0, y=0, width=225, height=40)

        # Button frame (in main frame in this button we create a another button like (customer, rooms, floor etc))
        btn_frame = Frame(main_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=225, y=0, width=1306, height=38)

        # 1 button in button frame(Customer)
        cust_btn = Button(btn_frame, text="CUSTOMER", command=self.cust_details, width=23, font=("times new roman", 14, "bold"), bg="black", fg="white", bd=0, relief=RIDGE, cursor="hand2")
        cust_btn.grid(row=0, column=0, pady=1)

        # 2 button in button frame (Employee)
        Room_btn = Button(btn_frame, text="Employee", command=self.Emp_details, width=23, font=("times new roman", 14, "bold"), bg="black", fg="white", bd=0, relief=RIDGE, cursor="hand2")
        Room_btn.grid(row=0, column=1, pady=1)

        # 3 button in button frame(Floor)
        Details_btn = Button(btn_frame, text="Floor", command=self.Floor_details, width=23, font=("times new roman", 14, "bold"), bg="black", fg="white", bd=0, relief=RIDGE, cursor="hand2")
        Details_btn.grid(row=0, column=2, pady=1)
        
        # 4 button in button frame (Payments)
        Report_btn = Button(btn_frame, text="Payments",command=self.Payment_details, width=23, font=("times new roman", 14, "bold"), bg="black", fg="white", bd=0, relief=RIDGE, cursor="hand2")
        Report_btn.grid(row=0, column=3, pady=1)

        # 5 button in button frame (Rooms)
        Logout_btn = Button(btn_frame, text="Rooms",command=self.Rooms_details, width=24, font=("times new roman", 14, "bold"), bg="black", fg="white", bd=0, relief=RIDGE, cursor="hand2")
        Logout_btn.grid(row=0, column=4, pady=1)

        # right side image 
        img3 = Image.open(r"C:\Users\amulb\OneDrive\Desktop\DBMS project\photos\1633410403702hotel-images\hotel images\hotelphoto.webp")
        img3 = img3.resize((1310, 560), Image.ADAPTIVE)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=225, y=40, width=1310, height=560)

        # image of myh
        img4 = Image.open(r"C:\Users\amulb\OneDrive\Desktop\DBMS project\photos\1633410403702hotel-images\hotel images\swimming.webp")
        img4 = img4.resize((230, 210), Image.ADAPTIVE)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg1 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=40, width=228, height=200)

        # image of food
        img5 = Image.open(r"C:\Users\amulb\OneDrive\Desktop\DBMS project\photos\1633410403702hotel-images\hotel images\food22.jpeg")
        img5 = img5.resize((230,190), Image.ADAPTIVE)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg1 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=200, width=228, height=200)

        # image of bed
        img6 = Image.open(r"C:\Users\amulb\OneDrive\Desktop\DBMS project\photos\1633410403702hotel-images\hotel images\hotelroom.jpeg")
        img6 = img6.resize((230,190), Image.ADAPTIVE)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        lblimg1 = Label(main_frame, image=self.photoimg6, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=400, width=228, height=200)


    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)


    def Emp_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Emp_Win(self.new_window)


    def Floor_details(self):
        self.new_window = Toplevel(self.root)
        self.app = floor_Win(self.new_window)


    def Rooms_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Rooms_Win(self.new_window)


    def Payment_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Payment_Win(self.new_window)

root = Tk()
obj = HotelManagementSystem(root)
root.mainloop()
