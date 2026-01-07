from tkinter import *
import time 
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import pymysql
import pandas



def act():
    global hst,usr,pas
    try:
       hst=hostentry.get()
       usr=userentry.get() 
       pas=psdentry.get() 
       ct= pymysql.connect(host=hst,user=usr,password=pas)
       mycur=ct.cursor()
       messagebox.showinfo("Sucess","Data base Connection Sucessfully!")
       #reglable.config(state="normal")
    except:
        messagebox.showerror("Error","Enter Correct Details!")


def cod(tit,But_txt,com,ab=""):
    try:
        global mycur
        ct= pymysql.connect(host=hst,user=usr,password=pas)
        mycur=ct.cursor()
        qry="use studentdetails"
        mycur.execute(qry)
        global ident,nameent,agent,addrent,mobent,genent,dobent,scr_win
    
    
        scr_win=Toplevel()
        scr_win.title(tit)
        scr_win.grab_set()
        scr_win.resizable(0,0)
    
        idlable=Label(scr_win,text="Id",font=("times new roman",15,"bold"))
        idlable.grid(row=0,column=0,padx=30,pady=15,sticky=W)
        ident=Entry(scr_win,font=("times new roman",15),width=20)
        ident.grid(row=0,column=1,pady=10,padx=15)
    
        namelable=Label(scr_win,text="Name",font=("times new roman",15,"bold"))
        namelable.grid(row=1,column=0,padx=30,pady=15,sticky=W)
        nameent=Entry(scr_win,font=("times new roman",15),width=20)
        nameent.grid(row=1,column=1,pady=10,padx=15)
    
        agelable=Label(scr_win,text="Age",font=("times new roman",15,"bold"))
        agelable.grid(row=2,column=0,padx=30,pady=15,sticky=W)
        agent=Entry(scr_win,font=("times new roman",15),width=20)
        agent.grid(row=2,column=1,pady=10,padx=15)
    
        addrlable=Label(scr_win,text="Address",font=("times new roman",15,"bold"))
        addrlable.grid(row=3,column=0,padx=30,pady=15,sticky=W)
        addrent=Entry(scr_win,font=("times new roman",15),width=20)
        addrent.grid(row=3,column=1,pady=10,padx=15)
    
        moblable=Label(scr_win,text="Mobile no",font=("times new roman",15,"bold"))
        moblable.grid(row=4,column=0,padx=30,pady=15,sticky=W)
        mobent=Entry(scr_win,font=("times new roman",15),width=20)
        mobent.grid(row=4,column=1,pady=10,padx=15)
    
        genlable=Label(scr_win,text="Gender",font=("times new roman",15,"bold"))
        genlable.grid(row=5,column=0,padx=30,pady=15,sticky=W)
        genent=Entry(scr_win,font=("times new roman",15),width=20)
        genent.grid(row=5,column=1,pady=10,padx=15)
    
        doblable=Label(scr_win,text="D.O.B",font=("times new roman",15,"bold"))
        doblable.grid(row=6,column=0,padx=30,pady=15,sticky=W)
        dobent=Entry(scr_win,font=("times new roman",15),width=20)
        dobent.grid(row=6,column=1,pady=10,padx=15)
        
        st_but=ttk.Button(scr_win,text=But_txt,command=com)
        st_but.grid(row=7,columnspan=2,pady=15)
        if com==add_datas:
            table.delete(*table.get_children())
        
        if com==update_:
            try:
                messagebox.showinfo("Values","Id can't change !",parent=scr_win)
                index=table.focus()
                cont=table.item(index)
                ls=cont["values"]
                ident.insert(0,ls[0])
                nameent.insert(0,ls[1])
                agent.insert(0,ls[2])
                addrent.insert(0,ls[3])
                mobent.insert(0,ls[4])
                genent.insert(0,ls[5])
                dobent.insert(0,ls[6])

            except:
                pass
    except:
        pass
            
      
def exi():
        re=messagebox.askyesno("Confirm","Sure,do you want exit ?")
        if re:
            rt.destroy()
        else:
            pass

def expo():
    try:
        path=filedialog.asksaveasfilename(defaultextension=".csv")
        indexing=table.get_children()
        nls=[]
        for i in indexing:
            conte=table.item(i)
            data=conte["values"]
            nls.append(data)
        new=(pandas.DataFrame(nls,columns=["Id","Name","Age","Address","Mobile no","Gender","D.O.B"],))
        new.to_csv(path,index=False)
        messagebox.showinfo("Save","Data Saved Sucessfully!")
    except:
        pass
            

def update_():
    
        if nameent.get()=="" or agent.get()==""or addrent.get()=="" or mobent.get()=="" or genent.get()=="" or dobent.get()=="" or ident.get()=="":
            messagebox.showerror("Warning!","Please selcet the valid detail !",parent=scr_win)   
        else:
            ct= pymysql.connect(host=hst,user=usr,password=pas)
            mycur=ct.cursor()
            qry="use studentdetails"
            mycur.execute(qry)
            qry= "update studentsinfo set name=%s,age=%s,address=%s,mobile_no=%s,gender=%s,dob=%s where id=%s"
            mycur.execute(qry,(nameent.get(),agent.get(),addrent.get(),mobent.get(),genent.get(),dobent.get(),ident.get()))
            ct.commit()
            messagebox.showerror("Sucess",f"id {ident.get()} changed",parent=scr_win)
            scr_win.destroy()
            sho()
        


def sho():
        ct= pymysql.connect(host=hst,user=usr,password=pas)
        mycur=ct.cursor()
        qry="use studentdetails"
        mycur.execute(qry)
        qry="select * from studentsinfo"
        mycur.execute(qry) 
        table.delete(*table.get_children())       
        fe=mycur.fetchall()
        for da in fe:
            dat_list=list(da)    
            table.insert("",END,values=dat_list)
            

    
              
    
       
def de():
    try:
        ct= pymysql.connect(host=hst,user=usr,password=pas)
        mycur=ct.cursor()
        qry="use studentdetails"
        mycur.execute(qry)
        ind=table.focus()
        cont=table.item(ind)
        con_id=cont["values"][0]   
        qry = "delete from studentsinfo where id =%s"  
        mycur.execute(qry,con_id) 
        ct.commit()
        qry= "select * from studentsinfo"
        mycur.execute(qry)
        fec=mycur.fetchall()
        table.delete(*table.get_children())
        for d in fec:
            table.insert("",END,values=d)
    except:
        pass                                    


    
def srch_datas():
    qry="select * from studentsinfo where id=%s or name=%s or age=%s  or address=%s  or mobile_no=%s  or gender=%s  or dob=%s"
    mycur.execute(qry,(ident.get(),nameent.get(),agent.get(),addrent.get(),mobent.get(),genent.get(),dobent.get()))
    table.delete(*table.get_children())
    feched_data=mycur.fetchall()
    for datas in feched_data:
        data_list=(datas)    
        table.insert("",END,values=data_list)


    
def add_datas():
    try:
        ct= pymysql.connect(host=hst,user=usr,password=pas)
        mycur=ct.cursor()
        if ident.get()=="" or nameent.get()=="" or agent.get()=="" or addrent.get()== "" or mobent.get()=="" or genent.get()=="" or dobent.get()=="":
            messagebox.showerror("Error","All Feilds are rquired",parent=scr_win)
        else:
            qry="use studentdetails"
            mycur.execute(qry)
            qry="insert into studentsinfo values(%s,%s,%s,%s,%s,%s,%s)"
            mycur.execute(qry,(ident.get(),nameent.get(),agent.get(),addrent.get(),mobent.get(),genent.get(),dobent.get()))
            ct.commit()
            res=messagebox.askyesno("Confirm","Data added succesfully.Do you want clear?",parent=scr_win)
            if res:
                ident.delete(0,END)
                nameent.delete(0,END)
                agent.delete(0,END)
                addrent.delete(0,END)
                mobent.delete(0,END)
                genent.delete(0,END)
                dobent.delete(0,END)
                
                qry="select *from studentsinfo"
                mycur.execute(qry)
                fetch_d=mycur.fetchall() 
                table.delete(*table.get_children())      
                for dat in fetch_d:
                    dat_list=list(dat)    
                    table.insert("",END,values=dat_list)
                else:
                    pass  
    except:
        pass

def dbs():
    global hostentry,userentry,psdentry
    
    db=Toplevel()  
    db.title("Databse Feilds")
    db.grab_set()
    db.resizable(0,0) 
    
    hostname=Label(db,text="host",font=("times new roman",15,"bold"))
    hostname.grid(row=0,column=0,padx=10, pady=10)
    hostentry=Entry(db,font=("times new roman",15,"bold"),width=20)
    hostentry.grid(row=0,column=1,padx=10,pady=10)

    userlbl=Label(db,text="user",font=("times new roman",15,"bold"))
    userlbl.grid(row=1,column=0,padx=10,pady=10)
    userentry=Entry(db,font=("times new roman",15,"bold"),width=20)
    userentry.grid(row=1,column=1,padx=10,pady=10)

    psd=Label(db,text="Password",font=("times new roman",15,"bold"))
    psd.grid(row=2,column=0,padx=10,pady=10)
    psdentry=Entry(db,font=("times new roman",15,"bold"),width=20)
    psdentry.grid(row=2,column=1,padx=10,pady=10)
    
    connect=ttk.Button(db,text="Connect",width=10,cursor="hand2",command=act)
    connect.grid(row=3,columnspan=2,padx=10,pady=10)

  
def clock():
    date=time.strftime("%d/%m/%y")
    currtime=time.strftime("%H:%M:%S")
    datetimelable.config(text=f"  TIME:{currtime}")
    datetimelable.after(1,clock)
    


rt=ttkthemes.ThemedTk()
rt.get_themes()
rt.set_theme("yaru")

rt.geometry("1174x680+0+0")
rt.resizable(0,0)
rt.title("Student Management System")




datetimelable=Label(rt,font=("Arial",16,),fg="red")
datetimelable.place(x=150,y=15)
clock()

head=Label(text="------ STUDENT DETAILS ------",font=("",27,"bold"),fg="green")
head.place(x=360,y=5)

leftframe=Frame(rt,bg="brown")
leftframe.place(x=150,y=80,width=924,height=35)
rightframe=Frame(rt)
rightframe.place(x=10,y=130,width=1150,height=550)



   

logoimage=PhotoImage(file="sts.png" or "siva/sts.png" ) 

logoimagelable=Label(rt,image=logoimage)
logoimagelable.place(x=10,y=5,)

addbutton=ttk.Button(leftframe,text="Add Details",width=14,state="",cursor="hand2",command=lambda:cod("Add Datas","Submit",add_datas))
addbutton.grid(row=0,column=1,padx=2)

searchbutton=ttk.Button(leftframe,text="Search Students",width=14,state="",cursor="hand2",command=lambda:cod("Search","Search",srch_datas))
searchbutton.grid(row=0,column=2,padx=2)

deletebutton=ttk.Button(leftframe,text="Delete Datas",width=14,cursor="hand2",command=de)
deletebutton.grid(row=0,column=3,padx=2)

updatebutton=ttk.Button(leftframe,text="Update Datas",width=14,state="",cursor="hand2",command=lambda:cod("Update datas","update",update_))
updatebutton.grid(row=0,column=4,padx=2)

showbutton=ttk.Button(leftframe,text="View All",width=14,state="",cursor="hand2",command=sho)
showbutton.grid(row=0,column=5,padx=2)

exportbutton=ttk.Button(leftframe,text="Export Datas",width=14,state="",cursor="hand2",command=expo)
exportbutton.grid(row=0,column=6,padx=2)

exitbutton=ttk.Button(leftframe,text="Exit",width=14,cursor="hand2",command=exi)
exitbutton.grid(row=0,column=7,padx=2)

db=ttk.Button(rt,text="CONNECT TO DATABASE",cursor="hand2",command=dbs)
db.place(x=990,y=10)

scbarx=Scrollbar(rightframe,orient="horizontal")
scbary=Scrollbar(rightframe,orient="vertical")


table=ttk.Treeview(rightframe,columns=("Id","Name","Age","Address","Mobile No","Gender","D.O.B"),xscrollcommand=scbarx.set,yscrollcommand=scbary.set)


scbarx.config(command=table.xview,cursor="hand2")
scbary.config(command=table.yview,cursor="hand2")

scbarx.pack(side=BOTTOM,fill=X)
scbary.pack(side=RIGHT,fill=Y)

table.pack(fill="both",expand=1)


table.heading("Id",text="Id")
table.heading("Name",text="Name")
table.heading("Age",text="Age")
table.heading("Address",text="Address")
table.heading("Mobile No",text="Mobile No")
table.heading("Gender",text="Gender")
table.heading("D.O.B",text="D.O.B")
table.config(show="headings")

table.column("Id",width=50,anchor=CENTER)
table.column("Name",width=200,anchor=CENTER)
table.column("Age",width=50,anchor=CENTER)
table.column("Address",width=300,anchor=CENTER)
table.column("Mobile No",width=200,anchor=CENTER)
table.column("Gender",width=70,anchor=CENTER)
table.column("D.O.B",width=100,anchor=CENTER)

styl=ttk.Style()
styl.configure("Treeview",rowheight=30,font=("arial",11))
styl.configure("Treeview.Heading",font=("arial",11,"bold"))



try:
    rt.mainloop()
except KeyboardInterrupt:
    print("Program closed manually")
