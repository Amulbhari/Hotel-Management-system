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
      


        lbltitle=Label(self.root,bd=20,relief = RIDGE,text = "+ HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font =("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        # ==========================Data frame=================
        Dataframe = Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1500,height=400)

        DataframeLeft = LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
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
        comNametablet["values"]=("Nice","Corona Vacacine","Acetaminophen","Adderall","Amlodipine","Ativan")
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
        btnPrescription= Button(Buttonframe,font=("arial",12,"bold"),text="Prescription",bg="green",fg="white",width=21,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData= Button(Buttonframe,command=self.iPrescriptionData,text="Prescription Data",bg="green",fg="white",font=("arial",12,"bold"),width=21,padx=2,pady=6)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate= Button(Buttonframe,text="Update",bg="green",fg="white",font=("arial",12,"bold"),width=21,padx=2,pady=6)
        btnUpdate.grid(row=0,column=2)

        btnDelete= Button(Buttonframe,text="Delete",bg="green",fg="white",font=("arial",12,"bold"),width=21,padx=2,pady=6)
        btnDelete.grid(row=0,column=3)

        btnClear= Button(Buttonframe,text="Clear",bg="green",fg="white",font=("arial",12,"bold"),width=21,padx=2,pady=6)
        btnClear.grid(row=0,column=4)

        btnExit= Button(Buttonframe,text="Exit",bg="green",fg="white",font=("arial",12,"bold"),width=21,padx=2,pady=6)
        btnExit.grid(row=0,column=5)

            #=======================================Scrollbar==========================================


        scroll_x= ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y= ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table= ttk.Treeview(Detailsframe,column=("Name of Tablets","ref","dose","Nooftablets","lot","issuedate",
                                                               "expdate","dailydose","storage","nhsnumber","pname",
                                                               "Dob","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side =BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill= Y)

        scroll_x= ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y= ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("Name of Tablets",text="Name of Tablets")
        self.hospital_table.heading("ref",text="Reference No:")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("Nooftablets",text="No of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("Dob",text="DOB")
        self.hospital_table.heading("Address",text="Address")

        self.hospital_table["show"]="headings"
    
        self.hospital_table.column("Name of Tablets",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("Nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("Dob",width=100)
        self.hospital_table.column("Address",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)

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



root = Tk()
ob = Hospital(root)
root.mainloop()
