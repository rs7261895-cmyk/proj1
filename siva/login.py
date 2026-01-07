from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import ttkthemes
from tkinter import ttk
import pymysql



global mycur,ct


    

"""        
def reg():
    
    def regcli():
        try:
            ct= pymysql.connect(host=hst,user=usr,password=pas)
            mycur=ct.cursor()
        
            if nameentry.get()!="" and passentry.get()!="":
                qry="create database infou"
                mycur.execute(qry)
                qry="use infou"
                mycur.execute(qry)
                qry="create table upuesers(u_id varchar(100) primary key,u_pas varchar(100))"
                mycur.execute(qry)
                qry= "insert into upuesers values(%s,%s)"
                mycur.execute(qry,(nameentry.get(),passentry.get()))
                ct.commit()
                sh=messagebox.showinfo("Done!","Register suceccfully")
                if sh:
                    nameentry.delete(0,END)
                    passentry.delete(0,END)
    
            else:
                messagebox.showerror("Error","Somthing went Wrong!",parent=new)
                #ct.commit()
        except:
            qry="use infou"
            mycur.execute(qry)
            qry= "insert into upuesers values(%s,%s)"
            mycur.execute(qry,(nameentry.get(),passentry.get()))
            ct.commit()
            sh=messagebox.showinfo("Done!","Register suceccfully",parent=new)
            if sh:
                nameentry.delete(0,END)
                passentry.delete(0,END)
                ig= mycur.fetchall()
                for i in ig :
                    dat_list=list(i)
                    print(dat_list)

 
    new=Toplevel()
    new.title("Register")
    new.grab_set()
    new.resizable(0,0)
    
    lblname=Label(new,text="Userid",font=("times new roman",15,"bold"))
    lblname.grid(row=0,column=0,padx=10, pady=10)
    nameentry=Entry(new,font=("times new roman",15,"bold"),width=20)
    nameentry.grid(row=0,column=1,padx=10,pady=10)
    
    lblpass=Label(new,text="Password",font=("times new roman",15,"bold"))
    lblpass.grid(row=1,column=0,padx=10,pady=10)
    passentry=Entry(new,font=("times new roman",15,"bold"),width=20)
    passentry.grid(row=1,column=1,padx=10,pady=10)
    
    regbutt=ttk.Button(new,text="Submit",width=25,cursor="hand2",command=regcli)
    regbutt.grid(row=2,columnspan=2,padx=10,pady=10)
    

"""
 
"""
def login():
    try: 
        ct= pymysql.connect(host=hst,user=usr,password=pas)
        mycur=ct.cursor()
        
        qry= "use infou"
        mycur.execute(qry)
        qry="select * from upuesers where u_id=%s and u_pas=%s"
        mycur.execute(qry,(usernameentry.get(),passwordentry.get()))
        ig= mycur.fetchone()
    
        if usernameentry.get()=="" or passwordentry.get()=="":
            messagebox.showerror("Erorr","Feilds are Required!")

        elif ig == None:
            messagebox.showerror("Erorr","Invalid username or password")

        else:
            messagebox.showinfo("Successful","Welcome to the page")
        
            ct= pymysql.connect(host=hst,user=usr,password=pas)
            #mycur=ct.cursor()
            try:
                qry="create database studentdetails"
                mycur.execute(qry)  
                qry="use studentdetails"
                mycur.execute(qry)
                qry="create table studentsinfo(id int not null primary key, name varchar(30),age int, address varchar(30),\
                    mobile_no varchar(10), gender varchar(10), dob varchar (20))"  
                mycur.execute(qry)
                win.destroy()
                import source
               
               
    
        
            except: 
                qry="use studentdetails"
                mycur.execute(qry)
                win.destroy()
                import source
                
               
               
               
   
    except: 
        messagebox.showerror("Erorr","Invalid username or password")     
         
"""

def login():
    if usernameentry.get()=="user" and passwordentry.get()=="123":
        messagebox.showinfo("Successful","Welcome to the page")
        win.destroy()
        import source
        
    elif usernameentry.get()=="" or passwordentry.get()=="":
        messagebox.showerror("Erorr","Feilds are Required!")
        
    else:
        messagebox.showerror("Invalid","Recheck your Id or Password")
        
        
        
         


    
win=ttkthemes.ThemedTk()
win.get_themes()
win.set_theme("yaru")

win.geometry("1280x717+0+0")
win.title("Login page")

win.resizable(False,False)

backgroundimage=ImageTk.PhotoImage(file="bg.jpg" or "siva/bg.jpg")

bglable=Label(win,image=backgroundimage)
bglable.place(x=0,y=0)

loginframe=Frame(win,bg="white")
loginframe.place(x=400,y=150,height=430)

logoimage=PhotoImage(file="logo.png" or "siva/logo.png")

logolable=Label(loginframe,image=logoimage)
logolable.grid(row=0,column=1,columnspan=2,pady=20)



usernamelable=Label(loginframe, text="Username",compound=LEFT,font=("times new roman",20,"bold"),bg="white")
usernamelable.grid(row=1,column=0,pady=20,padx=10)

usernameentry=Entry(loginframe,font=("times new roman",20),bd=5,fg="black",bg="white")
usernameentry.grid(row=1,column=1,pady=10,padx=10)

passwordlable=Label(loginframe, text="Password",compound=LEFT,font=("times new roman",20,"bold"),bg="white")
passwordlable.grid(row=2,column=0,pady=20,padx=10)

passwordentry=Entry(loginframe,font=("times new roman",20),bd=5,fg="black",bg="white")
passwordentry.grid(row=2,column=1,pady=10,padx=10)

loginbutton=ttk.Button(loginframe,text="Login",width=25,cursor="hand2",command=login) 
loginbutton.grid(row=4,column=1,pady=10)

#reglable=ttk.Button(loginframe, text="Register",cursor="hand2",state="disable",command=reg)
#reglable.place(x=240,y=370)



win.mainloop()

