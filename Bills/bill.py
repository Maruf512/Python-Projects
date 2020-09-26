from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x750+0+0")
        self.root.title("Billing App")
        bg_color="#A28089"
        title=Label(self.root,text="Next Fashion Textile",bd=12,fg="white",relief=GROOVE,bg=bg_color,font=("times new roman",25,"bold"),pady=2).pack(fill=X)

        #==================================Variables=================================#
        #================Shawl====================#
        self.product_1=IntVar()
        self.product_2=IntVar()
        self.product_3=IntVar()
        self.product_4=IntVar()
        self.product_5=IntVar()
        self.product_6=IntVar()
        #================Maflar====================#
        self.product_7=IntVar()
        self.product_8=IntVar()
        self.product_9=IntVar()
        self.product_10=IntVar()
        self.product_11=IntVar()
        self.product_12=IntVar()
        #================Orna====================#
        self.product_13=IntVar()
        self.product_14=IntVar()
        self.product_15=IntVar()
        self.product_16=IntVar()
        self.product_17=IntVar()
        self.product_18=IntVar()
        #==============Total Product Price=======#
        self.shawl_price=StringVar()
        self.maflar_price=StringVar()
        self.orna_price=StringVar()
        #===============Buyir Details============#
        self.c_name=StringVar()
        self.c_phone=StringVar()

        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))

        self.search_bill=StringVar()

        #================Total Price +============#
        self.p_s_price=IntVar()
        self.p_m_price=IntVar()
        self.p_o_price=IntVar()

        #==================Customer Detail Frame=====================#
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_text=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=3,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

        cphone_lbl=Label(F1,text="Phone No.",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphone_text=Entry(F1,width=25,textvariable=self.c_phone,font="arial 15",bd=3,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=5)

        c_bill_lbl=Label(F1,text="Bill No.",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_text=Entry(F1,width=15,textvariable=self.search_bill,font="arial 15 bold",bd=3,relief=SUNKEN).grid(row=0,column=5,padx=10,pady=5)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)

        #================Shawl====================#
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Shawl",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=180,width=325,height=380)

        s1_lbl=Label(F2,text="Vomshawl PL",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        s1_txt=Entry(F2,width=10,textvariable=self.product_1,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        p2_lbl=Label(F2,text="Vomshawl D",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        p2_txt=Entry(F2,width=10,textvariable=self.product_2,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        s3_lbl=Label(F2,text="Jhilmil PL",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        s3_txt=Entry(F2,width=10,textvariable=self.product_3,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        s4_lbl=Label(F2,text="Jhilmil D",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        s4_txt=Entry(F2,width=10,textvariable=self.product_4,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        s5_lbl=Label(F2,text="Jants Shawl PL",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        s5_txt=Entry(F2,width=10,textvariable=self.product_5,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        s6_lbl=Label(F2,text="Jents Shawl D",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        s6_txt=Entry(F2,width=10,textvariable=self.product_6,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #================Maflar====================#
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Maflar",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=340,y=180,width=325,height=380)

        m1_lbl=Label(F3,text="Maflar D",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        m1_txt=Entry(F3,width=10,textvariable=self.product_7,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        m2_lbl=Label(F3,text="Maflar PL",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        m2_txt=Entry(F3,width=10,textvariable=self.product_8,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        m3_lbl=Label(F3,text="Maflar 1",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        m3_txt=Entry(F3,width=10,textvariable=self.product_9,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        m4_lbl=Label(F3,text="Maflar 2",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        m4_txt=Entry(F3,width=10,textvariable=self.product_10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        m5_lbl=Label(F3,text="Maflar 3",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        m5_txt=Entry(F3,width=10,textvariable=self.product_11,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        m6_lbl=Label(F3,text="Maflar 4",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        m6_txt=Entry(F3,width=10,textvariable=self.product_12,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #================Orna====================#
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Orna",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=670,y=180,width=325,height=380)

        o1_lbl=Label(F4,text="Orna 1",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        o1_txt=Entry(F4,width=10,textvariable=self.product_13,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        o2_lbl=Label(F4,text="Orna 2",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        o2_txt=Entry(F4,width=10,textvariable=self.product_14,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        o3_lbl=Label(F4,text="Orna 3",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        o3_txt=Entry(F4,width=10,textvariable=self.product_15,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        o4_lbl=Label(F4,text="Orna 4",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        o4_txt=Entry(F4,width=10,textvariable=self.product_16,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        o5_lbl=Label(F4,text="Orna 5",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        o5_txt=Entry(F4,width=10,textvariable=self.product_17,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        o6_lbl=Label(F4,text="Orna 6",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        o6_txt=Entry(F4,width=10,textvariable=self.product_18,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #=================Bill Area==================#
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=180,width=350,height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #===============ButtonFreame=================#
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=140)

        m1_lbl=Label(F6,text="Total Shawl Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.shawl_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl=Label(F6,text="Total Maflar Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.maflar_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_lbl=Label(F6,text="Total Orna Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.orna_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        c1_lbl=Label(F6,text="Shawl Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=18,textvariable=self.p_s_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2_lbl=Label(F6,text="Maflar Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=18,textvariable=self.p_m_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3_lbl=Label(F6,text="Orna Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F6,width=18,textvariable=self.p_o_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=750,width=580,height=105)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        GBill_btn=Button(btn_F,text="Genrate",command=self.bill_area,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_F,text="Exit",command=self.Exit_app,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()


    def total(self):
        s_price=self.p_s_price.get()
        m_price=self.p_m_price.get()
        o_price=self.p_o_price.get()
        #=================#
        self.s_p1_p=self.product_1.get()*s_price
        self.s_p2_p=self.product_2.get()*s_price
        self.s_p3_p=self.product_3.get()*s_price
        self.s_p4_p=self.product_4.get()*s_price
        self.s_p5_p=self.product_5.get()*s_price
        self.s_p6_p=self.product_6.get()*s_price

        self.total_shawl_price=float(
                            self.s_p1_p+
                            self.s_p2_p+
                            self.s_p3_p+
                            self.s_p4_p+
                            self.s_p5_p+
                            self.s_p6_p
                            )
        x=self.total_shawl_price
        self.shawl_price.set("Tk : "+str(x))



        self.m_p7_p=self.product_7.get()*m_price
        self.m_p8_p=self.product_8.get()*m_price
        self.m_p9_p=self.product_9.get()*m_price
        self.m_p10_p=self.product_10.get()*m_price
        self.m_p11_p=self.product_11.get()*m_price
        self.m_p12_p=self.product_12.get()*m_price

        self.total_maflar_price=float(
                            self.m_p7_p+
                            self.m_p8_p+
                            self.m_p9_p+
                            self.m_p10_p+
                            self.m_p11_p+
                            self.m_p12_p
                            )
        y=self.total_maflar_price
        self.maflar_price.set("Tk : "+str(y))

        self.o_p13_p=self.product_13.get()*o_price
        self.o_p14_p=self.product_14.get()*o_price
        self.o_p15_p=self.product_15.get()*o_price
        self.o_p16_p=self.product_16.get()*o_price
        self.o_p17_p=self.product_17.get()*o_price
        self.o_p18_p=self.product_18.get()*o_price

        self.total_orna_price=float(
                            self.o_p13_p+
                            self.o_p14_p+
                            self.o_p15_p+
                            self.o_p16_p+
                            self.o_p17_p+
                            self.o_p18_p
                            )
        z=self.total_orna_price
        self.orna_price.set("Tk : "+str(z))

        self.Total_bill =float(x+y+z)
        self.Total_bill=(str(self.Total_bill))

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tNext Fashion Textile\n")
        self.txtarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Buyir Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number : {self.c_phone.get()}")
        self.txtarea.insert(END,f"\n======================================")
        self.txtarea.insert(END,f"\n Products     QTY    S.Price    Price")
        self.txtarea.insert(END,f"\n======================================")

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Enter Buyir Derails.")

        elif self.shawl_price.get()=="Tk : 0.0" and self.maflar_price.get()=="Tk : 0.0" and self.orna_price.get()=="Tk : 0.0":
            messagebox.showerror("Error","Product or Price is not selected.")

        else:

            #=========Shawl========#
            self.welcome_bill()
            if self.product_1.get()!=0:
                self.txtarea.insert(END,f"\n Vomshawl Pl\t\t{self.product_1.get()}\t{self.p_s_price.get()}\t{self.s_p1_p}")

            if self.product_2.get()!=0:
                self.txtarea.insert(END,f"\n Vomshawl D\t\t{self.product_2.get()}\t{self.p_s_price.get()}\t{self.s_p2_p}")

            if self.product_3.get()!=0:
                self.txtarea.insert(END,f"\n Jhilmil PL\t\t{self.product_3.get()}\t{self.p_s_price.get()}\t{self.s_p3_p}")

            if self.product_4.get()!=0:
                self.txtarea.insert(END,f"\n Jhilmil D\t\t{self.product_4.get()}\t{self.p_s_price.get()}\t{self.s_p4_p}")

            if self.product_5.get()!=0:
                self.txtarea.insert(END,f"\n Jants Shawl PL\t\t{self.product_5.get()}\t{self.p_s_price.get()}\t{self.s_p5_p}")

            if self.product_6.get()!=0:
                self.txtarea.insert(END,f"\n Jants Shawl D\t\t{self.product_6.get()}\t{self.p_s_price.get()}\t{self.s_p6_p}")

    #=========Maflar========#
            if self.product_7.get()!=0:
                self.txtarea.insert(END,f"\n Maflar D\t\t{self.product_7.get()}\t{self.p_m_price.get()}\t{self.m_p7_p}")

            if self.product_8.get()!=0:
                self.txtarea.insert(END,f"\n Maflar PL\t\t{self.product_8.get()}\t{self.p_m_price.get()}\t{self.m_p8_p}")

            if self.product_9.get()!=0:
                self.txtarea.insert(END,f"\n Maflar 1\t\t{self.product_9.get()}\t{self.p_m_price.get()}\t{self.m_p9_p}")

            if self.product_10.get()!=0:
                self.txtarea.insert(END,f"\n Maflar 2\t\t{self.product_10.get()}\t{self.p_m_price.get()}\t{self.m_p10_p}")

            if self.product_11.get()!=0:
                self.txtarea.insert(END,f"\n Maflar 3\t\t{self.product_11.get()}\t{self.p_m_price.get()}\t{self.m_p11_p}")

            if self.product_12.get()!=0:
                self.txtarea.insert(END,f"\n Maflar 4\t\t{self.product_12.get()}\t{self.p_m_price.get()}\t{self.m_p12_p}")

    #=========Orna========#
            if self.product_13.get()!=0:
                self.txtarea.insert(END,f"\n Orna 1\t\t{self.product_13.get()}\t{self.p_o_price.get()}\t{self.o_p13_p}")

            if self.product_14.get()!=0:
                self.txtarea.insert(END,f"\n Orna 2\t\t{self.product_14.get()}\t{self.p_o_price.get()}\t{self.o_p14_p}")

            if self.product_15.get()!=0:
                self.txtarea.insert(END,f"\n Orna 3\t\t{self.product_15.get()}\t{self.p_o_price.get()}\t{self.o_p15_p}")

            if self.product_16.get()!=0:
                self.txtarea.insert(END,f"\n Orna 4\t\t{self.product_16.get()}\t{self.p_o_price.get()}\t{self.o_p16_p}")

            if self.product_17.get()!=0:
                self.txtarea.insert(END,f"\n Orna 5\t\t{self.product_17.get()}\t{self.p_o_price.get()}\t{self.o_p17_p}")

            if self.product_18.get()!=0:
                self.txtarea.insert(END,f"\n Orna 6\t\t{self.product_18.get()}\t{self.p_o_price.get()}\t{self.o_p18_p}")

            self.txtarea.insert(END,f"\n--------------------------------------")
            self.txtarea.insert(END,f"\n Total Bill : \t\t\t Tk: {self.Total_bill}")
            self.txtarea.insert(END,f"\n--------------------------------------")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("Bills Data/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close
            messagebox.showinfo("Saved",f"Bill no. : {self.bill_no.get()} saved Successfully")
        else:
            return

    def find_bill(self):
        present="no"
        for i in os.listdir("Bills Data/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"Bills Data/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")

    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you want to Clear the Data?")
        if op>0:
            #================Shawl====================#
            self.product_1.set(0)
            self.product_2.set(0)
            self.product_3.set(0)
            self.product_4.set(0)
            self.product_5.set(0)
            self.product_6.set(0)
            #================Maflar====================#
            self.product_7.set(0)
            self.product_8.set(0)
            self.product_9.set(0)
            self.product_10.set(0)
            self.product_11.set(0)
            self.product_12.set(0)
            #================Orna====================#
            self.product_13.set(0)
            self.product_14.set(0)
            self.product_15.set(0)
            self.product_16.set(0)
            self.product_17.set(0)
            self.product_18.set(0)
            #==============Total Product Price=======#
            self.shawl_price.set("")
            self.maflar_price.set("")
            self.orna_price.set("")
            #===============Buyir Details============#
            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()
            #================Total Price +============#
            self.p_s_price.set(0)
            self.p_m_price.set(0)
            self.p_o_price.set(0)

    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you want to exit?")
        if op>0:
            self.root.destroy()


root=Tk()
obj = Bill_App(root)
root.mainloop()
