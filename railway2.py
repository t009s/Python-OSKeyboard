#Railway Reservation System + On-Screen Keyboard
import pyautogui
from Tkinter import *
from tkMessageBox import *
import sqlite3

con=sqlite3.Connection('rdb')
cur=con.cursor()
cur.execute("create table if not exists rail(eid varchar(20) primary key,fname varchar(20),pass varchar(20),gen varchar(20))")
root=Tk()
root.iconbitmap('capture.ico')

fr1=Frame(root)
fr1.pack()
fr2=Frame(root)
fr2.pack()
fr2.configure(background="red")
root.title('Railway Database')
s1=showinfo(title="Tushar Sharma",message='''Project Name:-

***** RAILWAY RESERVATION SYSTEM + ON-SCREEN KEYBOARD *****''')
s2=showinfo(title="Tushar Sharma",message='''
Project Submitted By:-  TUSHAR SHARMA
                                                151433  B7
                                                
Project Submitted To:-  Dr. MAHESH KUMAR''')
Label(fr1,text="RAILWAY RESERVATION SYSTEM + ON-SCREEN KEYBOARD",bg='red',fg='white',width=70,font="Arial 12 bold").grid(row=0,columnspan=15)

#****************************** CLASS OSKEY FOR ON-SCREEN KEYBOARD BY USING PYAUTOGUI MODULE ******************************
class oskey:
    
    def __init__(self):
        
        self.btn = [
        'Esc','`','1','2','3','4','5','6','7','8','9','0','-','=','<<==',
        'Tab','q','w','e','r','t','y','u','i','o','p','[',']','Enter','Del',
        'Caps','a','s','d','f','g','h','j','k','l',';','\'','\\','up','Shift',
        'Shift','z','x','c','v','b','n','m',',','.','/','Alt','left','down','right',
        'Space','Write'
         ]

        self.Shift = [
        'Esc','~','!','@','#','$','%','^','&','*','(',')','_','+','<<==',
        'Tab',  'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}','Enter','Del',
        'Caps', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"','|','up','Shift',
        'Shift','Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?','Alt','left','down','right',
        'Space','Write'
         ]

        self.Caps = [
        'Esc','`','1','2','3','4','5','6','7','8','9','0','-','=','<<==',
        'Tab',  'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']','Enter','Del',
        'Caps', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', '\'','\\','up','Shift',
        'Shift','Z', 'X', 'C', 'V', 'B', 'N', 'M',',','.','/','Alt','left','down','right',
        'Space','Write'
         ]

        self.keys = 1
    def select(self,but):
        if self.keys == 2:
            self.body(1)
            self.keys = 1
        if but == "Esc":
            pyautogui.hotkey('esc')
        if but == "<<==":
            pyautogui.hotkey('backspace')
        if but == "Enter":
            pyautogui.hotkey('enter')
        if but == "Del":
            pyautogui.hotkey('delete')
        if but == "Caps":
            if self.keys == 1:
                self.body(3)
                self.keys = 3
            elif self.keys == 3 or self.keys == 2:
                self.body(1)
                self.keys = 1
        if but == "Shift":
            self.body(2)
            self.keys = 2
        if but == "Ctrl":
            pyautogui.hotkey('ctrl')
        if but == "Alt":
            pyautogui.hotkey('altleft')
        if but == "left":
            pyautogui.hotkey('left')
        if but == "down":
            pyautogui.hotkey('down')
        if but == "right":
            pyautogui.hotkey('right')
        if but == "Space":
            pyautogui.hotkey('space')
        if but == "`":
            pyautogui.typewrite('`')
        if but == "1":
            pyautogui.typewrite('1')
        if but == "2":
            pyautogui.typewrite('2')
        if but == "3":
            pyautogui.typewrite('3')
        if but == "4":
            pyautogui.typewrite('4')
        if but == "5":
            pyautogui.typewrite('5')
        if but == "6":
            pyautogui.typewrite('6')
        if but == "7":
            pyautogui.typewrite('7')
        if but == "8":
            pyautogui.typewrite('8')
        if but == "9":
            pyautogui.typewrite('9')
        if but == "0":
            pyautogui.typewrite('0')
        if but == "-":
            pyautogui.typewrite('-')
        if but == "=":
            pyautogui.typewrite('=')
       
        if but == "Tab":
            pyautogui.hotkey('tab')
        if but == "q":
            pyautogui.typewrite('q')
        if but == "w":
            pyautogui.typewrite('w')
        if but == "e":
            pyautogui.typewrite('e')
        if but == "r":
            pyautogui.typewrite('r')
        if but == "t":
            pyautogui.typewrite('t')
        if but == "y":
            pyautogui.typewrite('y')
        if but == "u":
            pyautogui.typewrite('u')
        if but == "i":
            pyautogui.typewrite('i')
        if but == "o":
            pyautogui.typewrite('o')
        if but == "p":
            pyautogui.typewrite('p')
        if but == "[":
            pyautogui.typewrite('[')
        if but == "]":
            pyautogui.typewrite(']')
       
        if but == "a":
            pyautogui.typewrite('a')
        if but == "s":
            pyautogui.typewrite('s')
        if but == "d":
            pyautogui.typewrite('d')
        if but == "f":
            pyautogui.typewrite('f')
        if but == "g":
            pyautogui.typewrite('g')
        if but == "h":
            pyautogui.typewrite('h')
        if but == "j":
            pyautogui.typewrite('j')
        if but == "k":
            pyautogui.typewrite('k')
        if but == "l":
            pyautogui.typewrite('l')
        if but == ";":
            pyautogui.typewrite(';')
        if but == "'":
            pyautogui.typewrite("'")
        if but == "up":
            pyautogui.hotkey('up')
       
        if but == "z":
            pyautogui.typewrite('z')
        if but == "x":
            pyautogui.typewrite('x')
        if but == "c":
            pyautogui.typewrite('c')
        if but == "v":
            pyautogui.typewrite('v')
        if but == "b":
            pyautogui.typewrite('b')
        if but == "n":
            pyautogui.typewrite('n')
        if but == "m":
            pyautogui.typewrite('m')
        if but == ",":
            pyautogui.typewrite(',')
        if but == ".":
            pyautogui.typewrite('.')
        if but == "/":
            pyautogui.typewrite('/')
       
        if but == "Q":
            pyautogui.typewrite('Q')
        if but == "W":
            pyautogui.typewrite('W')
        if but == "E":
            pyautogui.typewrite('E')
        if but == "R":
            pyautogui.typewrite('R')
        if but == "T":
            pyautogui.typewrite('T')
        if but == "Y":
            pyautogui.typewrite('Y')
        if but == "U":
            pyautogui.typewrite('U')
        if but == "I":
            pyautogui.typewrite('I')
        if but == "O":
            pyautogui.typewrite('O')
        if but == "P":
            pyautogui.typewrite('P')
        if but == 'A':
            pyautogui.typewrite('A')
        if but == "S":
            pyautogui.typewrite('S')
        if but == "D":
            pyautogui.typewrite('D')
        if but == "F":
            pyautogui.typewrite('F')
        if but == "G":
            pyautogui.typewrite('G')
        if but == "H":
            pyautogui.typewrite('H')
        if but == "J":
            pyautogui.typewrite('J')
        if but == "K":
            pyautogui.typewrite('K')
        if but == "L":
            pyautogui.typewrite('L')
        if but == "Z":
            pyautogui.typewrite('Z')
        if but == "X":
            pyautogui.typewrite('X')
        if but == "C":
            pyautogui.typewrite('C')
        if but == 'V':
            pyautogui.typewrite('V')
        if but == "B":
            pyautogui.typewrite('B')
        if but == "N":
            pyautogui.typewrite('N')
        if but == "M":
            pyautogui.typewrite('M')
        if but == "~":
            pyautogui.typewrite('~')
        if but == "!":
            pyautogui.typewrite('!')
        if but == "@":
            pyautogui.typewrite('@')
        if but == "#":
            pyautogui.typewrite('#')
        if but == "$":
            pyautogui.typewrite('$')
        if but == "%":
            pyautogui.typewrite('%')
        if but == "^":
            pyautogui.typewrite('^')
        if but == "&":
            pyautogui.typewrite('&')
        if but == '*':
            pyautogui.typewrite('*')
        if but == "(":
            pyautogui.typewrite('(')
        if but == ")":
            pyautogui.typewrite(')')
        if but == "_":
            pyautogui.typewrite('_')
        if but == "+":
            pyautogui.typewrite('+')
        if but == "{":
            pyautogui.typewrite('{')
        if but == "}":
            pyautogui.typewrite('}')
        if but == "|":
            pyautogui.typewrite('|')
        if but == ":":
            pyautogui.typewrite(':')
        if but == '"':
            pyautogui.typewrite('"')
        if but == '<':
            pyautogui.typewrite('<')
        if but == ">":
            pyautogui.typewrite('>')
        if but == "?":
            pyautogui.typewrite('?')

    def body(self,mtyp):
        if mtyp == 1:
            key = self.btn
        elif mtyp == 2:
            key = self.Shift
        elif mtyp == 3:
            key = self.Caps
        Label(fr2,text="************************************************ On-Screen Keyboard ************************************************",bg='red',fg='Black',width=76,font="Arial 11 bold").grid(row=10,columnspan=15)
        varRow=13
        varCol=0
        for button in key:
            if button != "Space" and button != "Write":
                Button(fr2,text=button,width=5,bg='black',fg='white',activebackground='#ff3300',cursor='hand2',command=lambda x=button: self.select(x)).grid(row=varRow,column=varCol)
            if button == "Space":
                Button(fr2,text=button,width=99,bg='black',fg='white',activebackground='#ff3300',cursor='hand2',command=lambda x=button: self.select(x)).grid(row=18,columnspan=16)
            
            varCol += 1
            if varCol > 14 and varRow == 13:
                varCol = 0
                varRow += 1
            if varCol > 14 and varRow == 14:
                varCol = 0
                varRow += 1
            if varCol > 14 and varRow == 15:
                varCol = 0
                varRow += 1
            if varCol > 14 and varRow == 16:
                varCol = 0
                varRow += 1

#****************************** CLASS RAIL FOR RAILWAY RESERVATION SYSTEM ******************************
class rail:
    def __init__(self):
        self.button=[
        'Home','SignIn','SignUp','About'
        ]

    def select(self,but):
        if but == "Home":
            self.body1(1)
        if but == "SignIn":
            self.body1(2)
        if but == "SignUp":
            self.body1(3)
        if but == "About":
            self.body1(4)

    def body1(self,mtyp):
        def insert():
            user_exist = eid.get()
            cur.execute("select eid from rail where eid=(?)",(user_exist,))
            b=cur.fetchall()
            if b!=[]:
                showerror('Error','Username Already Exists')
            else:
                if pas.get() == cpas.get():
                    l=(eid.get(),fname.get(),pas.get(),gen.get())
                    cur.execute("insert into rail values(?,?,?,?)",l)
                    con.commit()
                    showinfo('Account',"Account Successfully Created")
                    eid.delete(0,24)
                    fname.delete(0,24)
                    pas.delete(0,24)
                    cpas.delete(0,24)
                    gen.delete(0,24)
                else:
                    showerror('Error','Passwords not matched')
        def show():
            d=eid.get()
            e=pas.get()
            cur.execute("select * from rail where eid=(?) and pass=(?)",(d,e,))
            a=cur.fetchall()
            if a==[]:
                showerror('Error','Email ID or Password is Incorrect')
            else:
                showinfo(title='Data display',message='''Email ID: %r

Fullname: %r

Password: %r

Gender: %r''' %(a[0]))
                pas.delete(0,24)
        if mtyp == 1:
            Label(fr1,text="*****Welcome to Railways*****",width=78,bg='red',fg='white',font="Arial 11 bold").grid(row=2,columnspan=15)
            img = PhotoImage(file='train1.gif')
            panel = Label(fr1, image = img,width=700,height=250)
            panel.image = img
            panel.grid(row=3,columnspan=15)
            Label(fr1,text="Project Submitted By:-",font=('comic sans ms','10')).grid(row=4,column=0)
            Label(fr1,text="TUSHAR SHARMA 151433 B7",font=('comic sans ms','9')).grid(row=4,column=1)
            Label(fr1,text="Project Submitted To:-",font=('comic sans ms','10')).grid(row=5,column=0)
            Label(fr1,text="    Dr. MAHESH KUMAR",width=20,font=('comic sans ms','10')).grid(row=5,column=1)
            Label(fr1,text="                               ").grid(row=6,column=0)
            Label(fr1,text="                               ",width=24).grid(row=6,column=1)
            Label(fr1,text="                                   ").grid(row=7,column=0)
            Label(fr1,text="                               ",width=24).grid(row=7,column=1)
            Label(fr1,text="                               ").grid(row=8,column=0)
            Label(fr1,text="                               ",width=24).grid(row=8,column=1)
            Label(fr1,text="                               ",width=20,height=2,font="Arial 10 bold").grid(row=9,column=1)

        elif mtyp == 2:
            img = PhotoImage(file='train2.gif')
            panel = Label(fr1, image = img,width=700,height=250)
            panel.image = img
            panel.grid(row=3,columnspan=15)
            Label(fr1,text="             Email ID             ",font=('comic sans ms','10')).grid(row=4,column=0)
            eid=Entry(fr1,justify="left",width=27)
            eid.grid(row=4,column=1)
            Label(fr1,text="             Password             ",font=('comic sans ms','10')).grid(row=5,column=0)
            pas=Entry(fr1,justify="left",width=27,show="*")
            pas.grid(row=5,column=1)
            Label(fr1,text="                               ").grid(row=6,column=0)
            Label(fr1,text="                               ",width=24).grid(row=6,column=1)
            Label(fr1,text="                                   ").grid(row=7,column=0)
            Label(fr1,text="                               ",width=24).grid(row=7,column=1)
            Label(fr1,text="                               ").grid(row=8,column=0)
            Label(fr1,text="                               ",width=24).grid(row=8,column=1)
            Button(fr1,text="SignIn ",width=15,bg='black',fg='white',font=('comic sans ms','10','bold'),command=lambda:show()).grid(row=9,column=1)
            
        elif mtyp == 3:
            img = PhotoImage(file='train3.gif')
            panel = Label(fr1, image = img,width=700,height=250)
            panel.image = img
            panel.grid(row=3,columnspan=15)
            Label(fr1,text="             Email ID             ",font=('comic sans ms','10')).grid(row=4,column=0)
            eid=Entry(fr1,justify="left",width=27)
            eid.grid(row=4,column=1)
            Label(fr1,text="             Password             ",font=('comic sans ms','10')).grid(row=5,column=0)
            pas=Entry(fr1,justify="left",width=27,show="*")
            pas.grid(row=5,column=1)
            Label(fr1,text="Enter Full Name",font=('comic sans ms','10')).grid(row=6,column=0)
            fname=Entry(fr1,justify="left",width=27)
            fname.grid(row=6,column=1)
            Label(fr1,text="Confirm Password",font=('comic sans ms','10')).grid(row=7,column=0)
            cpas=Entry(fr1,justify="left",width=27,show="*")
            cpas.grid(row=7,column=1)
            Label(fr1,text="Gender(M/F/T)",font=('comic sans ms','10')).grid(row=8,column=0)
            gen=Entry(fr1,justify="left",width=27)
            gen.grid(row=8,column=1)
            Button(fr1,text="SignUp",width=15,bg='black',fg='white',font=('comic sans ms','10','bold'),command=lambda:insert()).grid(row=9,column=1)

        elif mtyp == 4:
            img = PhotoImage(file='train1.gif')
            panel = Label(fr1, image = img,width=700,height=250)
            panel.image = img
            panel.grid(row=3,columnspan=15)
            Label(fr1,text="Project Submitted By:-",font=('comic sans ms','10')).grid(row=4,column=0)
            Label(fr1,text="TUSHAR SHARMA 151433 B7",font=('comic sans ms','9')).grid(row=4,column=1)
            Label(fr1,text="Project Submitted To:-",font=('comic sans ms','10')).grid(row=5,column=0)
            Label(fr1,text="    Dr. MAHESH KUMAR",width=20,font=('comic sans ms','10')).grid(row=5,column=1)
            Label(fr1,text="                               ").grid(row=6,column=0)
            Label(fr1,text="                               ",width=24).grid(row=6,column=1)
            Label(fr1,text="                                   ").grid(row=7,column=0)
            Label(fr1,text="                               ",width=24).grid(row=7,column=1)
            Label(fr1,text="                               ").grid(row=8,column=0)
            Label(fr1,text="                               ",width=24).grid(row=8,column=1)
            Label(fr1,text="                               ",width=20,height=2,font="Arial 10 bold").grid(row=9,column=1)

        varRow=1
        varCol=0
        for but in self.button:
            Button(fr1,text=but,width=24,bg='black',fg='white',activebackground='#ff3300',cursor='hand2',font=('comic sans ms','9'),command=lambda x=but: self.select(x)).grid(row=varRow,column=varCol)
            varCol+=1
    
#****************************** CREATING OBJECTS OF CLASS RAIL AND OSKEY ******************************        
var=rail()
var.body1(1)
var1=oskey()
var1.body(1)   
root.mainloop()
