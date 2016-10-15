from Tkinter import *
import sqlite3
global cursor
global con
global passdepo
global passwith


con = sqlite3.connect("brunosystem.db")
cursor = con.cursor()
#cursor.execute("CREATE TABLE useraccount (id INTEGER PRIMARY KEY AUTOINCREMENT,username varchar,password varchar)")
#cursor.execute("INSERT INTO useraccount VALUES (2,'bruno','mars')")
#cursor.execute("CREATE TABLE userprofile (id INTEGER PRIMARY KEY AUTOINCREMENT,firstname varchar,lastname varchar,country varchar,savings int)")

root = Tk()


#################functions




def formadd():  #addform
    add = Tk()
    add.geometry("450x350+100+10")
    add.title("BANKINGSYSTEM - ADD ACCOUNT")

    lbl_fname = Label(add,text="FIRST NAME:")
    lbl_lname = Label(add,text="LAST NAME:")
    lbl_contact = Label(add,text="CONTACT NO.:")
    lbl_country = Label(add,text="COUNTRY:")
    lbl_initdeposit = Label(add,text="INITIAL DEPOSIT(PHP):")
    entry_fname =  Entry(add)
    entry_lname =  Entry(add)
    entry_contact =  Entry(add)
    entry_country =  Entry(add)
    entry_initdeposit =  Entry(add)
    btn_clearadd = Button(add,text="RESET")
    btn_confirmadd = Button(add,text="ADD ACCOUNT")
    entry_initdeposit.insert(END,"0")

    entry_fname.place(x=250,y=60)
    entry_lname.place(x=250,y=100)
    entry_contact.place(x=250,y=140)
    entry_country.place(x=250,y=180)
    entry_initdeposit.place(x=250,y=220)
    lbl_fname.place(x=90,y=60)
    lbl_lname.place(x=90,y=100)
    lbl_contact.place(x=90,y=140)
    lbl_country.place(x=90,y=180)
    lbl_initdeposit.place(x=90,y=220)
    btn_confirmadd.place(x=250,y=280)
    btn_clearadd.place(x=90,y=280)
    def addreset(event):
        entry_fname.delete(0,END)
        entry_lname.delete(0,END)
        entry_contact.delete(0,END)
        entry_country.delete(0,END)
        entry_initdeposit.delete(0,END)
        entry_fname.focus_set()
        return
    def addaccount(event):
        fname=entry_fname.get()
        lname=entry_lname.get()
        contact=entry_contact.get()
        country=entry_country.get()
        depo=entry_initdeposit.get()
        cursor.execute("INSERT INTO userprofile (firstname,lastname,contact,country,savings) VALUES('{}','{}','{}','{}',{})".format(fname,lname,contact,country,depo))
        con.commit()
        tkinter.messagebox.showinfo('SUCCESS','ACCOUNT HAS BEEN SUCCESSFULLY ADDED!')
        addreset(event)

    btn_clearadd.bind("<Button-1>",addreset)
    btn_confirmadd.bind("<Button-1>",addaccount)



def formwithdraw(event):
    withdraw = Tk()
    withdraw.geometry("450x350+100+10")
    withdraw.title("BANKINGSYSTEM - WITHDRAW ACCOUNT")




def formupdate():
    update = Tk()
    update.geometry("700x350+100+10")
    update.title("BANKINGSYSTEM - UPDATE ACCOUNT")

    def selwith():
        entry_withdraw.config(state='normal')
        entry_deposit.config(state='disabled')
        entry_deposit.delete(0,END)
        entry_withdraw.delete(0,END)
        passdepo=entry_deposit.insert(END,'0')
        entry_withdraw.insert(END,'0')

        R1.deselect()
        R2.select()
    def seldepo():
        entry_deposit.config(state='normal')
        passwith=entry_withdraw.config(state='disabled')
        entry_deposit.delete(0,END)
        entry_withdraw.delete(0,END)
        passdepo=entry_deposit.insert(END,'0')
        entry_withdraw.insert(END,'0')
        R2.deselect()
        R1.select()
    var = IntVar()
    R1 = Radiobutton(update, text="DEPOSIT",variable = var, value=1,command = seldepo)
    R2 = Radiobutton(update, text="WITHDRAW",variable = var, value=1,command = selwith)
    lbl_fname1 = Label(update,text="FIRST NAME:")
    lbl_lname1 = Label(update,text="LAST NAME:")
    lbl_contact1 = Label(update,text="CONTACT NO.:")
    lbl_country1 = Label(update,text="COUNTRY:")
    lbl_initdeposit1 = Label(update,text="SAVINGS(PHP):", font="Verdana 12 bold")
    lbl_withdraw = Label(update,text="WITHDRAW(PHP):")
    lbl_deposit = Label(update,text="DEPOSIT(PHP):")

    entry_deposit = Entry(update,state='disabled')
    entry_withdraw =  Entry(update,state='disabled')
    entry_search = Entry(update)
    entry_fname1 =  Entry(update,state='disabled')
    entry_lname1 =  Entry(update,state='disabled')
    entry_contact1 =  Entry(update,state='disabled')
    entry_country1 =  Entry(update,state='disabled')
    lbl_initdeposit2 =  Label(update,text="0", font="Verdana 12 bold")

    btn_search = Button(update,text="SEARCH ACCOUNT NUMBER")
    btn_delete = Button(update,text="DELETE ACCOUNT")
    btn_confirmupdate = Button(update,text="UPDATE ACCOUNT")
    lbl_initdeposit2.config(text="0")

    entry_search.place(x=90,y=30)
    entry_fname1.place(x=250,y=110)
    entry_lname1.place(x=250,y=150)
    entry_contact1.place(x=250,y=190)
    entry_country1.place(x=250,y=230)
    lbl_initdeposit2.place(x=550,y=100)
    entry_withdraw.place(x=550,y=190)
    lbl_fname1.place(x=90,y=110)
    lbl_lname1.place(x=90,y=150)
    lbl_contact1.place(x=90,y=190)
    lbl_country1.place(x=90,y=230)
    btn_search.place(x=300,y=27)
    lbl_initdeposit1.place(x=400,y=100)
    lbl_withdraw.place(x=400,y=190)
    lbl_deposit.place(x=400,y=230)
    entry_deposit.place(x=550,y=230)

    def retupdateaccount(event):
        updatereset(event)
        lbl_initdeposit2.config(text="0")
        search=entry_search.get()
        cursor.execute("SELECT firstname,lastname,contact,country,savings FROM userprofile where id='{}'".format(search))
        con.commit()
        try:

            for num in cursor.fetchall():
                val1=num[0]
                val2=num[1]
                val3=num[2]
                val4=num[3]
                val5=num[4]


            entry_fname1.config(state='normal')
            entry_lname1.config(state='normal')
            entry_contact1.config(state='normal')
            entry_country1.config(state='normal')

            entry_fname1.insert(END,str(val1))
            entry_lname1.insert(END,str(val2))
            entry_contact1.insert(END,str(val3))
            entry_country1.insert(END,str(val4))
            lbl_initdeposit2.config(text=str(val5))
            btn_confirmupdate.place(x=400,y=300)
            btn_delete.place(x=190,y=300)
            R1.place(x=400,y=150)
            R2.place(x=550,y=150)
            entry_deposit.delete(0,END)
            entry_withdraw.delete(0,END)
            entry_withdraw.insert(END,'0')
            entry_deposit.insert(END,'0')
        except:
            R1.place_forget()
            R2.place_forget()
            entry_withdraw.config(state='disabled')
            entry_fname1.config(state='disabled')
            entry_lname1.config(state='disabled')
            entry_contact1.config(state='disabled')
            entry_country1.config(state='disabled')
            entry_deposit.config(state='disabled')
            lbl_initdeposit2.config(text="0")
            btn_confirmupdate.place_forget()
            btn_delete.place_forget()
            entry_deposit.delete(0,END)
            entry_withdraw.delete(0,END)
            entry_withdraw.insert(END,'0')
            entry_deposit.insert(END,'0')
            tkinter.messagebox.showinfo('ERROR','ACCOUNT DOES NOT EXIST!')

    def updatereset(event):
        entry_fname1.delete(0,END)
        entry_lname1.delete(0,END)
        entry_contact1.delete(0,END)
        entry_country1.delete(0,END)
        lbl_initdeposit2.config(text="0")
        entry_fname1.focus_set()
        return




    def deleteaccount(event):
        search= entry_search.get()
        if tkinter.messagebox.askokcancel("NOTICE","DO YOU REALLY WANT TO DELETE THIS ACCOUNT?"):
            cursor.execute("DELETE FROM userprofile WHERE id='{}'".format(search))
            con.commit()
            updatereset(event)
            tkinter.messagebox.showinfo('SUCCESS','ACCOUNT HAS BEEN DELETED SUCCESSFULLY!')


    def updateaccount(event):

        passwith=lbl_initdeposit2.cget("text")
        tempvar2=entry_withdraw.get()
        save=int(passwith)-int(tempvar2)

        passdepo=lbl_initdeposit2.cget("text")
        tempvar3=entry_deposit.get()
        save=int(passdepo)+ int(tempvar3)



        fname1=entry_fname1.get()
        lname1=entry_lname1.get()
        contact1=entry_contact1.get()
        country1=entry_country1.get()
        search= entry_search.get()

        cursor.execute("UPDATE userprofile SET firstname='{}',lastname='{}',contact='{}',country='{}',savings='{}' WHERE id='{}'".format(fname1,lname1,contact1,country1,save,search))
        con.commit()
        tkinter.messagebox.showinfo('SUCCESS','ACCOUNT HAS BEEN UPDATED SUCCESSFULLY!')
        updatereset(event)
        retupdateaccount(event)
        save=0
        entry_withdraw.delete(0,END)
    btn_delete.bind("<Button-1>",deleteaccount)
    btn_confirmupdate.bind("<Button-1>",updateaccount)
    btn_search.bind("<Button-1>",retupdateaccount)

def formdeposit(event):
    delete = Tk()
    delete.geometry("800x500+100+10")
    delete.title("BANKINGSYSTEM - DEPOSIT CASH")

################################## MAIN FORM #######################################
def form2main():
    main = Tk()
    main.geometry("800x400+100+10")
    main.title("BANKINGSYSTEM - MAIN")
    def logoutexit():
        if tkinter.messagebox.askokcancel("NOTICE","DO YOU REALLY WANT TO EXIT?"):
            main.withdraw()
            root.deiconify()
            entryPassword.delete(0,END)



    #menu_bar

    menu = Menu(main)
    main.config(menu=menu)
    file= Menu(menu)
    file.add_command(label='ADD ACCOUNT', command=formadd)
    file.add_command(label='UPDATE ACCOUNT', command=formupdate)
    menu.add_cascade(label='ADMIN', menu=file)

    logout= Menu(menu)
    logout.add_command(label='EXIT',command=logoutexit)
    menu.add_cascade(label='LOGOUT', menu=logout)




def clearfields(event): #clear
    entryPassword.delete(0,END)
    entryUsername.delete(0,END)
    entryUsername.focus_set()
    return

def logincond(event):
    username = entryUsername.get()
    password = entryPassword.get()
    cursor.execute("SELECT count(*) FROM useraccount where username='{}'and password='{}'".format(username,password))
    con.commit()
    for i in cursor.fetchall():
        num=i
        if(num[0]>0):
           tkinter.messagebox.showinfo('LOGIN','WELCOME')
           root.withdraw()
           form2main()
        else:
           tkinter.messagebox.showinfo('LOGIN','INVALID USERNAME/PASSWORD!')
           clearfields(event)



root.title("LOGIN")
root.geometry("+400+200")
lblUsername = Label (root, text= "USERNAME: ")
lblPassword = Label (root, text= "PASSWORD: ")

###############textbox
entryUsername = Entry(root)
entryUsername.focus_set()
entryPassword = Entry(root)
entryPassword.config(show="*")


#login button func
btnLogin = Button(root, text = "LOGIN")
btnLogin.bind("<Button-1>",logincond) #event on mouse left click
btnClear = Button(root, text = "CLEAR")
btnClear.bind("<Button-1>",clearfields)
#checkbox
checkKeep = Checkbutton(root,text = "Remember me?", onvalue=1,offvalue=0)

#design coord
lblUsername.grid(row=0,sticky=E)
lblPassword.grid(row=1,sticky=E)
entryUsername.grid(row=0,column=1)
entryPassword.grid(row=1,column=1)
btnLogin.grid(row=3,column=1)
btnClear.grid(row=3,column=0)
checkKeep.grid(row=2,columnspan=2)



root.mainloop()
