from tkinter import*
from tkinter import ttk
# import random
# import time
# import datetime
from tkinter import messagebox
import mysql.connector



    
class Hospital:
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        self.NameofTablets =StringVar()
        self.ref =StringVar()
        self.Dose =StringVar()
        self.NumberofTablets =StringVar()
        self.Lot =StringVar()
        self.Issuedate =StringVar()
        self.Expdate =StringVar()
        self.DailyDose =StringVar()
        self.sideEffect =StringVar()
        self.FurtherInformation =StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingfUsingMachine =StringVar()
        self.HowtoUseMedication =StringVar()
        self.PatientId =StringVar()
        self.nhsNumber =StringVar()
        self.PatientName =StringVar()
        self.DateOfBirth =StringVar()
        self.PatientAddress=StringVar()
      
        self.search_var=StringVar()


        lbltitle=Label(self.root,bd=10,relief = RIDGE,text = "+ HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font =("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        #search frame
        SearchFrame = Frame(self.root,bd=5,relief=RIDGE)
        SearchFrame.place(x=0,y=100,width=800,height=40)

        # Search By Label
        cSearchbar = Label(SearchFrame, text="Search By",font="bold", fg="black")
        cSearchbar.grid(row=0, column=0, sticky=W, padx=2)  

        # Search Bar Combobox
        combo_search_bar = ttk.Combobox(SearchFrame,textvariable=self.search_var, width=30, state="readonly")
        combo_search_bar["values"] = ("Name of Tablets", "ref", "dose", "No_of_tablets", "lot", "issuedate", "expdate", "dailydose", "storage", "nhsnumber", "pname", "Dob", "PatientAddress",)
        combo_search_bar.grid(row=0, column=1, padx=2)

        # Entry field for combo box
        self.text_cSearchBar=StringVar()
        textcSearchBar = ttk.Entry(SearchFrame,textvariable=self.text_cSearchBar, width=30)
        textcSearchBar.grid(row=0, column=2, padx=2)

        # Search Button
        btnSearch = Button(SearchFrame,command=self.search, text="Search", font=("Arial", 12), bg="white", fg="black", width=15)
        btnSearch.grid(row=0, column=3, padx=1)

        # Show all Button
        btnShow_all = Button(SearchFrame,command=self.fetch_data, text="Show all", font=("Arial", 12), bg="white", fg="black", width=15)
        btnShow_all.grid(row=0, column=4, padx=1)


        # ==========================Data frame=================
        Dataframe = Frame(self.root,bd=10,relief=RIDGE)
        Dataframe.place(x=0,y=140,width=1500,height=390)

        DataframeLeft = LabelFrame(Dataframe,bd=5,relief=RIDGE,padx=10,
                                  font =("arial",12,"bold"),text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=980,height=350)

        DataframeRight = LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                  font =("arial",12,"bold"),text="Prescription")
        DataframeRight.place(x=990,y=5,width=345,height=350)
        
        #=======================buttons frame=========================
        Buttonframe = Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1500,height=70)

        #======================details frame====================
        Detailsframe = Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1500,height=190)

        #======================Dataframeleft=========================================
        lblNameTablet=Label(DataframeLeft,text="Name of Tablets",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)

        comNametablet= ttk.Combobox(DataframeLeft,textvariable=self.NameofTablets,state = "readonly",font=("arial",12,"bold"),
                                    width = 33)
        comNametablet["values"]=("Acetaminophen","Corona Vacacine","Adderall","Amitriptyline","Amiodipine","Amoxicillin",
                                 "Ativan","Atorvastatin","Azithromycin,")
        comNametablet.current(0)
        comNametablet.grid(row=0,column=1)

        lblref=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Reference No:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataframeLeft,font=("times new roman",13,"bold"),textvariable=self.ref,width=35)
        txtref.grid(row=1,column=1)


        lblDose=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Dose:",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataframeLeft,font=("times new roman",13,"bold"),textvariable=self.Dose,width=35)
        txtDose.grid(row=2,column=1)

        lblNoOftablets=Label(DataframeLeft,font=("times new roman",12,"bold"),text="No of Tablets:",padx=2,pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets=Entry(DataframeLeft,font=("times new roman",13,"bold"),textvariable=self.NumberofTablets,width=35)
        txtNoOftablets.grid(row=3,column=1)

        lblLot=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Lot:",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataframeLeft,font=("times new roman",13,"bold"),textvariable=self.Lot,width=35)
        txtLot.grid(row=4,column=1)

        
        lblissueDate=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate=Entry(DataframeLeft,font=("times new roman",13,"bold"),textvariable=self.Issuedate,width=35)
        txtissueDate.grid(row=5,column=1)

        lblExpDate=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Exp Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataframeLeft,font=("times new roman",13,"bold"),textvariable=self.Expdate,width=35)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Daily Dose:",padx=2,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataframeLeft,font=("times new roman",13,"bold"),textvariable=self.DailyDose,width=35)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataframeLeft,font=("times new roman",13,"bold"),textvariable=self.sideEffect,width=35)
        txtSideEffect.grid(row=8,column=1)

        lblFurtherinfo=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Further Information:",padx=2)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        txtFurtherinfo=Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.FurtherInformation,width=35)
        txtFurtherinfo.grid(row=0,column=3)

        lblDrivingfUsingMachine=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Blood Pressure:",padx=2,pady=6)
        lblDrivingfUsingMachine.grid(row=1,column=2,sticky=W)
        txtDrivingfUsingMachine=Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.DrivingfUsingMachine,width=35)
        txtDrivingfUsingMachine.grid(row=1,column=3)

        lblStorage=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Storage Advice:",padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.StorageAdvice,width=35)
        txtStorage.grid(row=2,column=3)

        lblHowtoUseMedication=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Medication",padx=2,pady=6)
        lblHowtoUseMedication.grid(row=3,column=2,sticky=W)
        txtHowtoUseMedication=Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.HowtoUseMedication,width=35)
        txtHowtoUseMedication.grid(row=3,column=3,sticky=W)

        lblPatientId=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Patient Id:",padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.PatientId,width=35)
        txtPatientId.grid(row=4,column=3)

        lblNhsNumber=Label(DataframeLeft,font=("times new roman",12,"bold"),text="NHS Number:",padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber=Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.nhsNumber,width=35)
        txtNhsNumber.grid(row=5,column=3)

        lblPatientname=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Patient Name:",padx=2,pady=6)
        lblPatientname.grid(row=6,column=2,sticky=W)
        txtPatientname=Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.PatientName,width=35)
        txtPatientname.grid(row=6,column=3)

        lblDateOfBirth=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Date of Birth:",padx=2,pady=6)
        lblDateOfBirth.grid(row=7,column=2,sticky=W)
        txtDateOfBirth=Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.DateOfBirth,width=35)
        txtDateOfBirth.grid(row=7,column=3)

        lblPatientAddress=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Patient Address:",padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.PatientAddress,width=35)
        txtPatientAddress.grid(row=8,column=3)

        #====================================dataframeright==============================================
        self.txtPrescription=Text(DataframeRight,font=("times new roman",12,"bold"),width=37,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        #==========================================buttons====================================================
        btnPrescription= Button(Buttonframe,font=("arial",12,"bold"), command=self.iprecription , text="Prescription",bg="green",fg="white",width=30,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData= Button(Buttonframe,command=self.iPrescriptionData,text="Prescription Data",bg="green",fg="white",font=("arial",12,"bold"),width=21,padx=2,pady=6)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate= Button(Buttonframe,command=self.update_data,text="Update",bg="green",fg="white",font=("arial",12,"bold"),width=21,padx=2,pady=6)
        btnUpdate.grid(row=0,column=2)

        btnDelete= Button(Buttonframe,command=self.idelete,text="Delete",bg="green",fg="white",font=("arial",12,"bold"),width=21,padx=2,pady=6)
        btnDelete.grid(row=0,column=3)

        btnClear= Button(Buttonframe,command=self.clear,text="Clear",bg="green",fg="white",font=("arial",12,"bold"),width=21,padx=2,pady=6)
        btnClear.grid(row=0,column=4)

        btnExit= Button(Buttonframe,command=self.iExit ,text="Exit",bg="green",fg="white",font=("arial",12,"bold"),width=21,padx=2,pady=6)
        btnExit.grid(row=0,column=5)

            #=======================================Scrollbar==========================================


        scroll_x= ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y= ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table= ttk.Treeview(Detailsframe,column=("Name of Tablets","ref","dose","No_of_tablets","lot","issuedate",
                                                               "expdate","dailydose","storage","nhsnumber","pname",
                                                               "Dob","PatientAddress"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side =BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill= Y)

        scroll_x= ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y= ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("Name of Tablets",text="Name of Tablets")
        self.hospital_table.heading("ref",text="Reference No:")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("No_of_tablets",text="No of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("Dob",text="DOB")
        self.hospital_table.heading("PatientAddress",text="Address")

        self.hospital_table["show"]="headings"
    
        self.hospital_table.column("Name of Tablets",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("No_of_tablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("Dob",width=100)
        self.hospital_table.column("PatientAddress",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

        #==========================================Functinality declration==========================

    def iPrescriptionData(self):
        if self.NameofTablets.get() == "" or self.ref.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="atulakulamul990", database="mydata")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO hospital VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.NameofTablets.get(),
                    self.ref.get(),
                    self.Dose.get(),
                    self.NumberofTablets.get(),
                    self.Lot.get(),
                    self.Issuedate.get(),
                    self.Expdate.get(),
                    self.DailyDose.get(),
                    self.StorageAdvice.get(),
                    self.nhsNumber.get(),
                    self.PatientName.get(),
                    self.DateOfBirth.get(),
                    self.PatientAddress.get()))
                conn.commit()
                messagebox.showinfo("Success", "Data inserted successfully")
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")
            finally:
                if conn.is_connected():
                    my_cursor.close()
                    conn.close()
                    
    
    def update_data(self):
                conn = mysql.connector.connect(host="localhost", username="root", password="atulakulamul990", database="mydata")
                my_cursor = conn.cursor()
                my_cursor.execute(" update hospital set nameoftablets=%s,Dose=%s,Numberoftablet=%s,Lot=%s,issuedate=%s,ExpDate=%s,Dailydose=%s,storage=%s,nhsnumber=%s,patientName=%s,DOB=%s,patientAddress=%s where refnumber=%s",(
                            self.NameofTablets.get(),
                            self.Dose.get(),
                            self.NumberofTablets.get(),
                            self.Lot.get(),
                            self.Issuedate.get(),
                            self.Expdate.get(),
                            self.DailyDose.get(),
                            self.StorageAdvice.get(),
                            self.nhsNumber.get(),
                            self.PatientName.get(),
                            self.DateOfBirth.get(),
                            self.PatientAddress.get(),
                            self.ref.get(),
                            ))
                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo(" Update","Patient has been Update successfully")
        
                
                
                
    def fetch_data(self):
                conn = mysql.connector.connect(host="localhost", username="root", password="atulakulamul990", database="mydata")
                my_cursor = conn.cursor()
                my_cursor.execute(" select * from hospital")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.hospital_table.delete(*self.hospital_table.get_children())
                    for i in rows:
                        self.hospital_table.insert("",END,values=i)
                conn.commit()
                conn.close()

    def get_cursor(self,event=""):
                cursor_row=self.hospital_table.focus()
                content=self.hospital_table.item(cursor_row)
                row=content["values"]
                self.NameofTablets.set(row[0])
                self.ref.set(row[1])
                self.Dose.set(row[2])
                self.NumberofTablets.set(row[3])
                self.Lot.set(row[4])
                self.Issuedate.set(row[5])
                self.Expdate.set(row[6])
                self.DailyDose.set(row[7])
                self.StorageAdvice.set(row[8])
                self.nhsNumber.set(row[9])
                self.PatientName.set(row[10])
                self.DateOfBirth.set(row[11])
                self.PatientAddress.set(row[12])
    
    def iprecription(self):
        self.txtPrescription.insert(END," name of tablets: \t\t\t"+self.NameofTablets.get()+ "\n")
        self.txtPrescription.insert(END,"Reference No:\t\t\t" + self.ref.get()+ "\n")
        self.txtPrescription.insert(END," Dose:\t\t\t" + self.Dose.get() + "\n")
        self.txtPrescription.insert(END," Number of tablets: \t\t\t" + self.NumberofTablets.get() + "\n")
        self.txtPrescription.insert(END, " Lot: \t\t\t"+ self.Lot.get ()+"\n")
        self.txtPrescription.insert(END,"Issue Date : \t\t\t" + self.Issuedate.get() + "\n")
        self.txtPrescription.insert(END," Exp Date: \t\t\t"+self.Expdate.get()+ "\n")
        self.txtPrescription.insert(END," daily Dose : \t\t\t"+self.DailyDose.get()+ "\n")
        self.txtPrescription.insert(END," Side Effect: \t\t\t"+self.sideEffect.get()+ "\n")
        self.txtPrescription.insert(END," Futher Information: \t\t\t"+self.FurtherInformation.get()+ "\n")
        self.txtPrescription.insert(END," Storage Advice: \t\t\t"+self.StorageAdvice.get()+ "\n")
        self.txtPrescription.insert(END,"DrivingUsingMachine: \t\t\t"+self.DrivingfUsingMachine.get()+ "\n")
        self.txtPrescription.insert(END," patientID: \t\t\t"+self.PatientId.get()+ "\n")
        self.txtPrescription.insert(END," NHSNumber: \t\t\t"+self.nhsNumber.get()+ "\n")    
        self.txtPrescription.insert(END," PatientName: \t\t\t"+self.PatientName.get()+ "\n")
        self.txtPrescription.insert(END," Date OF Birth: \t\t\t"+self.DateOfBirth.get()+ "\n")
        self.txtPrescription.insert(END," Patient Address: \t\t\t"+self.PatientAddress.get()+ "\n")
                      
                
    def idelete(self):
                conn = mysql.connector.connect(host="localhost", username="root", password="atulakulamul990", database="mydata")
                my_cursor = conn.cursor()
                query= " delete from hospital where  refnumber=%s "
                value=(self.ref.get(),)
                my_cursor.execute(query,value)
                
                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo(" Delete","Patient has been deleted successfully")
                
    def clear(self):
                self.NameofTablets.set("")
                self.ref.set("")
                self.Dose.set("")
                self.NumberofTablets.set("")
                self.Lot.set("")
                self.Issuedate.set("")
                self.Expdate.set("")
                self.DailyDose.set("")
                self.sideEffect.set("")
                self.FurtherInformation.set("")
                self.StorageAdvice.set("")
                self.DrivingfUsingMachine.set("")
                self.HowtoUseMedication.set("")
                self.PatientId.set("")
                self.nhsNumber.set("")
                self.PatientName.set("")
                self.DateOfBirth.set("")
                self.PatientAddress.set("")
                self.txtPrescription.delete("1.0",END)
    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="atulakulamul990", database="mydata")
        my_cursor = conn.cursor()

        # Remove the double quotes around the column name
        my_cursor.execute("SELECT * FROM hospital WHERE `" + str(self.search_var.get()) + "` LIKE '%" + str(self.text_cSearchBar.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("", END, values=i)
            conn.commit()
        conn.close()
                
    def iExit(self):
                iExit=messagebox.askyesno("Hospital Management System"," Confirm you want to exit")
                if iExit>0:
                    root.destroy()
                    return
        
                
    
        

        
    




    

root = Tk()
ob = Hospital(root)
root.mainloop()
