import sqlite3
from only import onlyint
con=sqlite3.connect('AtMan783H.sqlite')
cur=con.cursor()

		
def lsd():
    n=onlyint('Enter percentage constraint :')
    de=cur.execute('SELECT REGNO,NAME,MARKS,ATTEN,PNO FROM CAMU')
    print('Students with less than '+str(n)+'% marks are :/n')
    print('RegsNo       Name           Marks    Attendance   ContactNumber ')
    for t in de:
        if (t[2]<n):
            print(t)
def upa():
    cur.execute('SELECT REGNO,NAME,MARKS,ATTEN FROM CAMU')
    com=cur.fetchall()
    for i in range(0,onlyint('Enter No of Students :')):
        n=input('Enter RegsNo :')
        m=onlyint('Enter No of classes present till date :')
        m=(m/60)*100
        if m>0:
            for l in com:
                l=list(l)
                if(l[0]==n):
                    l[3]=m
                print(tuple(l))


def um():
    cur.execute('SELECT REGNO,NAME,MARKS,ATTEN FROM CAMU')
    com=cur.fetchall()
    for i in range(0,onlyint('Enter No of Students :')):
        n=input('Enter RegsNo :')
        m=onlyint('Enter Marks :')
        for l in com:
            l=list(l)
            if(l[0]==n):
                l[2]=m
            print(tuple(l))
    

def alsd():
    cur.execute('SELECT REGNO,NAME,MARKS,ATTEN,PNO FROM CAMU')
    for r in cur:
        print(r)
def signup():
	un=input('Enter Username :')
	pd=input('Enter Password :')
	cur.execute('SELECT REGNO,PSWD FROM CAMU')
	ver=cur.fetchall()
	bo=False
	for t in ver:
		if(t[0]==un and t[1]==pd):
			bo=True
			print('\nLOGIN SUCCESS')
			amv(un)
            
            
	if bo==False:
		print('INVALID USERNAME OR PASSWORD')
		
def amv(un):
	cur.execute('SELECT REGNO,NAME,MARKS,ATTEN FROM CAMU')
	for t in cur:
		if(t[0]==un):
			print('Name 		: ',t[1])
			print('Marks 		: ',t[2])
			print('Attendance 	: ',t[3])
			
def av():
	signup()
def ssd():
    un=input('Enter Username :')
    cur.execute('SELECT REGNO FROM CAMU')
    ver=cur.fetchall()
    bo=False
    for t in ver:
        if(t[0]==un):
            bo=True
            print('\nLOGIN SUCCESS')
            ampv(un)
            break
    if bo==False:
        print('INVALID USERNAME')
def ampv(un):
    cur.execute('SELECT REGNO,NAME,MARKS,ATTEN,PNO FROM CAMU')
    for t in cur:
        if(t[0]==un):
            print('Name 		: ',t[1])
            print('Marks 		: ',t[2])
            print('Attendance 	: ',t[3])
            print('Phone Number : ',t[4])

def atc():
    print('\nSTUDENTS WITH LESS THAN 75% ATTENDENCE')
    cur.execute('SELECT REGNO,NAME,MARKS,ATTEN,PNO FROM CAMU WHERE ATTEN<75')
    de=cur.fetchall()
    print('RegsNo       Name           Marks    Attendance   ContactNumber ')
    for t in de:
        print(t)
    ic=onlyint('''Do you want to send messages to student parents 
               1.Yes
               2.No
               :''')
    if ic==1:
        f=open('msg.txt','w+')
        for t in de:
            st='\nYour Child  ' +t[1]+' of Regs no '+t[0]+' has less than 75% attendance  i.e '+str(t[3])+' % please check'
            f.write(st)
            print('Message sent to parent of '+t[1])

    
print('WELCOME TO BEC ATTENDANCE MANAGMENT')
while(True):
    print('''
    0.Exit
    1.Students
    2.Mentor
    3.Parent
    4.Subject Faculty
    
    ''')
    ch=onlyint('Choose your Category : ')
    if ch==1:
        print('YOU ARE STUDENT')
        print('''	1.login  in your login.
    	2.view their attendance percentage and Marks''')
        
        c=onlyint('Choose your Category : ')
        if c==1:
            print('STUDENT login PAGE')
            signup()
        elif c==2:
            print('VIEWING ATTENDANCE :')
            av()
        else :
            print('INVALID CHOICE')
    
    elif ch==2:
        
        print('YOU ARE MENTOR')
        print('''
        1.View their student status
        2.If attendance is below 75% he need to send a message to the
        parent mobile number
        3.Identify the less scoring students in examinations
        ''')
        
        c=onlyint('Choose your Category : ')
        if c==1:
            print('VIEWING STUDENT DETAILS')
            ic=onlyint('''
        Choose 1 to View all Student Details 
        Choose 2 to View a Particular Student Details ''')
            if ic==1:
                print('ALL STUDENT DETAILS')
                alsd()
            elif ic==2:
                print('ENTER SINGLE STUDENT USERNAME')
                ssd()
        elif c==2:
             atc()
        elif c==3 :
             lsd()
        else :
             print()
    elif ch==3 :
        print('YOU ARE PARENT')
        print('''1.Viewing your child’s attendance and marks
        ''')
        
        c=onlyint('Choose your Category : ')
        if c==1:
             print('Enter your childs :')
             signup()
        else :
             print('INVALID CHOICE')
    elif ch==4:
        print('YOU ARE FACULTY')
        print('''
              1.Enter the marks of all students
              2.Post the attendance for every period   
        ''')
        c=onlyint('Choose your Category : ')
        if c==1:
             um()
        elif c==2:
             upa()
        else :
             print('INVALID CHOICE!!!!')
    
    elif ch==0:
        break
    else:
        print('INVALID CHOICE!!!!!')
    	
