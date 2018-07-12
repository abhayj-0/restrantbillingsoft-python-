from tkinter import *
import tkinter.messagebox
import sqlite3
conn = sqlite3.connect('menu')
conn.execute('''CREATE TABLE IF NOT EXISTS DRINKS_1(
D_ID INTEGER PRIMARY KEY,
D_NAME CHAR(50) NOT NULL,
D_PRICE REAL NOT NULL)''')
#conn.execute("DROP TABLE IF EXISTS DRINKS_1")
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
#conn.execute("DROP TABLE IF EXISTS NORTH , COFFE , DESSETS") giving error
# print("all tables created")
#
# conn.execute("INSERT INTO DRINKS_1(D_NAME,D_PRICE) VALUES('KINGFISHER BEER',1000)")
# conn.execute("INSERT INTO DRINKS_1(D_NAME,D_PRICE) VALUES('TUBORG BEER',100)")
# conn.execute("INSERT INTO DRINKS_1(D_NAME,D_PRICE) VALUES('KARLSBERG BEER',500)")

# conn.execute("INSERT INTO NORTH(N_ID,N_NAME,N_PRICE) VALUES(1,'TAWA ROTI',12)")
# conn.execute("INSERT INTO NORTH(N_ID,N_NAME,N_PRICE) VALUES(2,'SPECIAL THALI',50)")
# conn.execute("INSERT INTO NORTH(N_ID,N_NAME,N_PRICE) VALUES(3,'SHAHI PANEER',200)")
#
# conn.execute("INSERT INTO COFFE(C_ID,C_NAME,C_PRICE) VALUES(1,'CAFE FRAPPE',184)")
# conn.execute("INSERT INTO COFFE(C_ID,C_NAME,C_PRICE) VALUES(2,'ICEBURG',200)")
# conn.execute("INSERT INTO COFFE(C_ID,C_NAME,C_PRICE) VALUES(3,'CRUNCHY FRAPPE',300)")
#
# conn.execute("INSERT INTO DESSETS(DE_ID,DE_NAME,DE_PRICE) VALUES(1,'VANILLA',60)")
# conn.execute("INSERT INTO DESSETS(DE_ID,DE_NAME,DE_PRICE) VALUES(2,'CHOCOLATE',100)")
# conn.execute("INSERT INTO DESSETS(DE_ID,DE_NAME,DE_PRICE) VALUES(3,'BUTTERSCOTCH',40)")


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

    def addNorthIndian(self):
        print("s")
    def addDrink(self):
        conn.execute("INSERT INTO DRINKS_1(D_NAME,D_PRICE) VALUES('SCOTCH',779)")
        conn.commit()
        dri = conn.execute("SELECT * from DRINKS_1")
        print(dri.fetchall())
    def addCoffe(self):
        print("advagw")
    def addDessert(self):
        print("advagw")


root = Tk()
root.title("Billing_sys")
a = c_menu(root)


root.mainloop()
