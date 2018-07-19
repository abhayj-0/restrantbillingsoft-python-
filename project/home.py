from tkinter import *
from tkinter import simpledialog,messagebox,ttk,Tcl
import sqlite3
conn = sqlite3.connect('menu')
conn.execute('''CREATE TABLE IF NOT EXISTS TOTA(
ID INTEGER PRIMARY KEY,
TR REAL NOT NULL,
ST REAL NOT NULL,
SP REAL NOT NULL,
R REAL NOT NULL,
KB REAL NOT NULL,
TU REAL NOT NULL,
KA REAL NOT NULL,
VO REAL NOT NULL,
CF REAL NOT NULL,
IC REAL NOT NULL,
CRF REAL NOT NULL,
VAN REAL NOT NULL,
CHO REAL NOT NULL,
BUTT REAL NOT NULL,
total REAL NOT NULL,
tax REAL NOT NULL,
subt REAL NOT NULL)''')
conn.execute('''CREATE TABLE IF NOT EXISTS CATEGORY(
CA_ID INTEGER PRIMARY KEY,
CA_NAME CHAR(50) NOT NULL )''')
conn.execute('''CREATE TABLE IF NOT EXISTS DRINKS_1(
D_ID INTEGER PRIMARY KEY,
D_NAME CHAR(50) NOT NULL,
D_PRICE REAL NOT NULL)''')
#conn.execute("DROP TABLE IF EXISTS NORTH")
conn.execute('''CREATE TABLE IF NOT EXISTS NORTH(
N_ID INTEGER PRIMARY KEY,
N_NAME CHAR(50) NOT NULL,
N_PRICE REAL NOT NULL)''')
conn.execute('''CREATE TABLE IF NOT EXISTS COFFE(
C_ID INTEGER PRIMARY KEY,
C_NAME CHAR(50) NOT NULL,
C_PRICE REAL NOT NULL)''')
conn.execute('''CREATE TABLE IF NOT EXISTS DESSETS(
DE_ID INTEGER PRIMARY KEY,
DE_NAME CHAR(50) NOT NULL,
DE_PRICE REAL NOT NULL)''')

#conn.execute("DROP TABLE IF EXISTS TOTA")
#conn.execute("DROP TABLE IF EXISTS NORTH")
#conn.execute("DROP TABLE IF EXISTS DESSETS")
#conn.execute("DROP TABLE IF EXISTS COFFE")
#conn.execute("DROP TABLE IF EXISTS NORTH , COFFE , DESSETS") giving error
print("all tables created")
# conn.execute("INSERT INTO CATEGORY(CA_NAME) VALUES('North Indian')")
# conn.execute("INSERT INTO CATEGORY(CA_NAME) VALUES('Drinks')")
# conn.execute("INSERT INTO CATEGORY(CA_NAME) VALUES('Coffee')")
# conn.execute("INSERT INTO CATEGORY(CA_NAME) VALUES('Deserts')")
#
# conn.execute("INSERT INTO DRINKS_1(D_NAME,D_PRICE) VALUES('KINGFISHER BEER',1000)")
# conn.execute("INSERT INTO DRINKS_1(D_NAME,D_PRICE) VALUES('TUBORG BEER',100)")
# conn.execute("INSERT INTO DRINKS_1(D_NAME,D_PRICE) VALUES('KARLSBERG BEER',500)")
#
# conn.execute("INSERT INTO NORTH(N_NAME,N_PRICE) VALUES('TAWA ROTI',12)")
# conn.execute("INSERT INTO NORTH(N_NAME,N_PRICE) VALUES('SPECIAL THALI',50)")
# conn.execute("INSERT INTO NORTH(N_NAME,N_PRICE) VALUES('SHAHI PANEER',200)")
#
# conn.execute("INSERT INTO COFFE(C_NAME,C_PRICE) VALUES('CAFE FRAPPE',184)")
# conn.execute("INSERT INTO COFFE(C_NAME,C_PRICE) VALUES('ICEBURG',200)")
# conn.execute("INSERT INTO COFFE(C_NAME,C_PRICE) VALUES('CRUNCHY FRAPPE',300)")
#
# conn.execute("INSERT INTO DESSETS(DE_NAME,DE_PRICE) VALUES('VANILLA',60)")
# conn.execute("INSERT INTO DESSETS(DE_NAME,DE_PRICE) VALUES('CHOCOLATE',100)")
# conn.execute("INSERT INTO DESSETS(DE_NAME,DE_PRICE) VALUES('BUTTERSCOTCH',40)")
# conn.commit()

class c_menu:
    def __init__(self,master):
        self.menu1 = Menu(master)
        master.config(menu=self.menu1)
        self.Submenu = Menu(self.menu1)
        self.menu1.add_cascade(label = "Add",menu=self.Submenu)
        self.Submenu.add_command(label="Add Drinks",command=self.addDrink)
        self.Submenu.add_separator()
        self.Submenu.add_command(label="Add North Indian Food", command=self.addNorthIndian)
        self.Submenu.add_separator()
        self.Submenu.add_command(label="Add Coffee", command=self.addCoffe)
        self.Submenu.add_separator()
        self.Submenu.add_command(label="Add Desserts", command=self.addDessert)

    def addCommand(self):
        com = str(simpledialog.askstring("Input", "Enter the name of category?"))

        if com is not None:
            conn.execute("INSERT INTO CATEGORY(CA_NAME) VALUES(?,?)",(com))
            conn.commit()
            dri = conn.execute("SELECT * FROM CATEGORY")
            print(dri.fetchall())
        else:
            messagebox.showinfo('Data Error', 'No Data Entered!!!\n No Change')
    def addNorthIndian(self):
        nans = str(simpledialog.askstring("Input", "Enter the name of item?"))
        nans1 = float(simpledialog.askstring("Input", "Enter teh price?"))
        if nans and nans1 is not None:
            conn.execute("INSERT INTO NORTH(N_NAME,N_PRICE) VALUES(?,?)", (nans, nans1))
            conn.commit()
            dri = conn.execute("SELECT * FROM NORTH")
            print(dri.fetchall())
        else:
            messagebox.showinfo('Data Error', 'No Data Entered!!!\n No Change')
    def addDrink(self):
        answer = str(simpledialog.askstring("Input", "Enter the name of item?"))
        answer1 = float(simpledialog.askstring("Input", "Enter teh price?"))
        if answer and answer1 is not None:
            conn.execute("INSERT INTO DRINKS_1(D_NAME,D_PRICE) VALUES(?,?)",(answer,answer1))
            conn.commit()
            dri = conn.execute("SELECT * FROM DRINKS_1")
            print(dri.fetchall())
        else:
            messagebox.showinfo('Data Error','No Data Entered!!!\n No Change')
            # print("You didn't have entered the values")
            # print("nochnge")

    def addCoffe(self):
        Cans = str(simpledialog.askstring("Input", "Enter the name of item?"))
        Cans1 = float(simpledialog.askstring("Input", "Enter teh price?"))
        if Cans and Cans1 is not None:
            conn.execute("INSERT INTO COFFE(C_NAME,C_PRICE) VALUES(?,?)", (Cans, Cans1))
            conn.commit()
            dri = conn.execute("SELECT * FROM COFFE")
            print(dri.fetchall())
        else:
            messagebox.showinfo('Data Error', 'No Data Entered!!!\n No Change')
    def addDessert(self):
        DEans = str(simpledialog.askstring("Input", "Enter the name of item?"))
        DEans1 = float(simpledialog.askstring("Input", "Enter teh price?"))
        if DEans and DEans1 is not None:
            conn.execute("INSERT INTO DESSETS(DE_NAME,DE_PRICE) VALUES(?,?)", (DEans, DEans1))
            conn.commit()
            dri = conn.execute("SELECT * FROM DESSETS")
            print(dri.fetchall())
        else:
            messagebox.showinfo('Data Error', 'No Data Entered!!!\n No Change Made')


root = Tk()
root.title("Billing_sys")
a = c_menu(root)
nb = ttk.Notebook(root)  # Create Tab Control
tab1 = ttk.Frame(nb)  # Create a tab
tab2 = ttk.Frame(nb)
tab3 = ttk.Frame(nb)
tab4 = ttk.Frame(nb)
tab5 = ttk.Frame(nb)
nb.add(tab5, text='Total')  # Add the tab
nb.add(tab1, text='North Indian')  # Add the tab
nb.add(tab2, text='Drinks')  # Add the tab
nb.add(tab3, text='Coffe')  # Add the tab
nb.add(tab4, text='Desserts')  # Add the tab
nb.pack(expand=1, fill="both")
label1=Label(tab5,text="Tawa Roti")
label1.grid(row=1,column=0)
label3 = Label(tab5, text="Special Thali")
label3.grid(row=3,column=0)
label4 = Label(tab5, text="Shahi Paneer")
label4.grid(row=6,column=0)
label5 = Label(tab5, text="Raita")
label5.grid(row=8,column=0)
bu1=Entry(tab5)
bu1.grid(row=1,column=1)
bu2 = Entry(tab5)
bu2.grid(row=3, column=1)
bu3 = Entry(tab5)
bu3.grid(row=6, column=1)
bu4 = Entry(tab5)
bu4.grid(row=8, column=1)
label5 = Label(tab5, text="kingfisher beer")
label5.grid(row=1, column=2)
label6 = Label(tab5, text="tuborg beer")
label6.grid(row=3, column=2)
label7 = Label(tab5, text="Karlsberg Beer")
label7.grid(row=6, column=2)
label8 = Label(tab5, text="Vodka")
label8.grid(row=8, column=2)
bu5 = Entry(tab5)
bu5.grid(row=1, column=3)

bu6 = Entry(tab5)
bu6.grid(row=3, column=3)
bu7 = Entry(tab5)
bu7.grid(row=6, column=3)
bu8 = Entry(tab5)
bu8.grid(row=8, column=3)
label9 = Label(tab5, text="Caffee Frappe")
label9.grid(row=1, column=4)
label10 = Label(tab5, text="iceburg")
label10.grid(row=3, column=4)
label11 = Label(tab5, text="Crunchy Frappe")
label11.grid(row=6, column=4)
label12 = Label(tab5, text="Vanilla")
label12.grid(row=8, column=4)

bu9 = Entry(tab5,)
bu9.grid(row=1, column=5)

bu10 = Entry(tab5)
bu10.grid(row=3, column=5)

bu11 = Entry(tab5)
bu11.grid(row=6, column=5)
bu12 = Entry(tab5)
bu12.grid(row=8, column=5)
label13 = Label(tab5, text="Chocolate")
label13.grid(row=1, column=6)
label14 = Label(tab5, text="Butterscortch")
label14.grid(row=3, column=6)

bu13 = Entry(tab5)
bu13.grid(row=1, column=7)

bu14 = Entry(tab5)
bu14.grid(row=3, column=7)
def totalp():

    sumo = int(bu1.get())*12 + int(bu2.get())*50 + int(bu3.get())*200 + int(bu4.get())*20 + int(bu5.get())*10000 + int(bu6.get())*100 + int(bu7.get())*500 + int(bu8.get())*780 + int(bu9.get())*184 + int(bu10.get())*200 + int(bu11.get())*300 + int(bu12.get())*60 + int(bu13.get())*100 + int(bu14.get())*40

    tax=(2/100)*sumo
    surv=(3/100)*100
    subt=surv+tax+sumo
    totta=sumo+subt
    labe1 = Label(tab5, text=str(tax))
    labe1.grid(row=11, column=3)
    labe2 = Label(tab5, text=str(subt))
    labe2.grid(row=13, column=3)
    labe = Label(tab5,text=str(totta))
    labe.grid(row=10,column=3)
    conn.execute("INSERT INTO TOTA(TR,ST,SP,R,KB,TU,KA,VO,CF,IC,CRF,VAN,CHO,BUTT,total,tax,subt) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(int(bu1.get()),int(bu2.get()),int(bu3.get()),int(bu4.get()),int(bu5.get()),int(bu6.get()),int(bu7.get()),int(bu8.get()),int(bu9.get()),int(bu10.get()),int(bu11.get()),int(bu12.get()),int(bu13.get()),int(bu14.get()),totta,tax,subt))
    conn.commit()
    #l.config(text="answer = %s" % sumo)
def res():
    bu1.delete(0,END);bu1.insert(END,0)
    bu2.delete(0, END);bu2.insert(END, 0)
    bu3.delete(0, END);bu3.insert(END, 0)
    bu4.delete(0, END);bu4.insert(END, 0)
    bu5.delete(0, END);bu5.insert(END, 0)
    bu6.delete(0, END);bu6.insert(END, 0)
    bu7.delete(0, END);bu7.insert(END, 0)
    bu8.delete(0, END);bu8.insert(END, 0)
    bu9.delete(0, END);bu9.insert(END, 0)
    bu10.delete(0, END);bu10.insert(END, 0)
    bu11.delete(0, END);bu11.insert(END, 0)
    bu12.delete(0, END);bu12.insert(END, 0)
    bu13.delete(0, END);bu13.insert(END, 0)
    bu14.delete(0, END);bu14.insert(END, 0)
bu15 = Button(tab5,text="Total",command=totalp)
bu15.grid(row=10,column=2)
bu156 = Button(tab5,text="Reset",command=res)
bu156.grid(row=10,column=5)

label15 = Label(tab5, text="Tax")
label15.grid(row=11, column=2)
label6 = Label(tab5, text="Subtotal")
label6.grid(row=13, column=2)
h = conn.execute("SELECT * FROM NORTH")
for i in h:
                g = Label(tab1,text=i[1])
                g.grid(rowspan=2,column=10)
                q = Label(tab1,text=i[2])
                q.grid(rowspan=3,column=40)
hu = conn.execute("SELECT * FROM DRINKS_1")
for i in hu:
                g = Label(tab2, text=i[1])
                g.grid(rowspan=2, column=10)
                q = Label(tab2, text=i[2])
                q.grid(rowspan=3, column=40)
hIU = conn.execute("SELECT * FROM COFFE")
for i in hIU:
                g = Label(tab3, text=i[1])
                g.grid(rowspan=2, column=10)
                q = Label(tab3, text=i[2])
                q.grid(rowspan=3, column=40)
hA = conn.execute("SELECT * FROM DESSETS")
for i in hA:
                g = Label(tab4, text=i[1])
                g.grid(rowspan=2, column=10)
                q = Label(tab4, text=i[2])
                q.grid(rowspan=3, column=40)

root.mainloop()
