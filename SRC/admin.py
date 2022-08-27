import ListSplit
#ADMIN LOGIN

email_list=[]
pwsd_list=[]
cont_list=[]
name_list=list()
global emailid
global phonenumber
global name
global pasw

def signup():
    print("---------------------------SIGN UP HERE------------------------")
    
    emailid=input("Enter your Email ID: ")
    
    phonenumber=int(input("Enter your 10 digit PHONE NUMBER: "))
    
    name=input("Enter your FULL NAME: ")
    flagphone = 0
    flagemail = 1
    alphacount = 0
    for i in emailid:
        if i == '@':
            alphacount += 1
        elif i<='Z' and i>='A':
            break
    if len(emailid) < 8 or alphacount != 1 or emailid[-1] == '@' or emailid[0] == '@':
        flagemail = 0
    if len(str(phonenumber)) == 10 and str(phonenumber)[0] != '0':
        flagphone = 1


    
    pasw=input("Enter your PASSWORD: ")
    digit = 0
    sletter = 0
    cletter = 0
    special = 0
    flag = 0
    paslen=len(pasw)

    for i in pasw:
        if i<='z' and i>='a':
            sletter += 1
        elif i<='Z' and i>='A':
            cletter += 1
        elif i<='9' and i>='0':
            digit += 1
        elif ((i<='&' and i>='!' and i!='"') or (i == '@')):
            special += 1
    

    while True:
        if paslen > 12 or paslen < 6:
            print('Length of password should be between 6 and 12')
            break
        elif digit <1:
            print('No Digits in your password')
            break
        elif sletter <1:
            print('No small letter in your password')
            break
        elif cletter <1:
            print('No capital letter in your password')
            break
        elif special <1:
            print('No Special characters in your password')
            break
        else:
            flag = 1
            with open("amem.txt","a+",encoding='UTF8') as f:
                
                S=emailid+","+pasw+","+str(phonenumber)+","+name+'\n'
                f.write(S)
                f.close()
            break
    print("SIGN UP SUCCESSFUL!!!!!")
    print("To LOGIN press Y else N.Enter your choice:-")
    choice=input()
    if choice.upper()=='Y':
        login()
    elif choice.upper=='N':
        return flag
    else:
        print("WRONG CHOICE!!!!")


def login():
    with open("amem.txt","r",encoding='UTF8') as f:
        
        lines=f.readlines()
        lines=[x.strip('\n') for x in lines]
        for i in range(len(lines)):
            ind=0
            for a in lines[i].split(','):
                if(ind==0):
                    email_list.append(a)
                elif(ind==1):
                    pwsd_list.append(a)
                elif(ind==2):
                    cont_list.append(a)
                elif(ind==3):
                    name_list.append(a)
                ind+=1
    print("-----------------------LOGIN HERE--------------------")
    success=0
    while success!=1:
        email = input("Enter your Email ID: ")
        pas = input('Password: ')
        flag = 0
        found=0
        if email in email_list and pas in pwsd_list:
            found=email_list.index(email)
            print("LOGIN SUCCESSFUL!!!!!")
            print("____________"+'\nWELCOME '+name_list[found].upper()+" :-"+"____________")
            print("________________"+"CONTACT: "+cont_list[found]+"____________________")
            success=1
        else:
            print('Username and password not present! Sign up before Login')
            signup()
    v=0
    while v==0:
        print("************************************************************")
        print("ENTER 1. ADD BOOKS IN THE STOCK")
        print("ENTER 2. DELETE BOOKS FROM THE STOCK")
        print("ENTER 3. TO EXIT THE DEPARTMENT")
        print("************************************************************")
        a=int(input("Select a choice from 1-3: "))

                    
        if(a==1):
            m=True
            while m:
                insert_bookdata()
                print("Enter Y to continue or N to exit:-")
                char=input("Enter your choice: ")
                if char=='N' or char=='n':
                    print("Thanks for adding the book.")
                    m=False
                else:
                    m=True
                
        elif(a==2):
            m=True
            while m:
                delete_bookdata()
                print("To continue deleting press Y else N:-")
                choice=input("Enter your choice: ")
                if choice.upper()=='N':
                    print("Thanks for deleting.")
                    m=False
                else:
                    m=True
                    
                
        elif(a==3):
                print("You have exited the admin department!!.")
                v=1
                
        else:
                print("You have entered the wrong choice")
                continue
        
   
def insert_bookdata():
        print("Enter the following book details:- ")
        bname = input('Enter name of the book: ')
        authname = input('Enter name of the author: ')
        price = input('Enter the price of book: ')
        try:
            quan=int(input("Enter the quantity of book: "))
        except:
            quan = None
            print('Number of books cant have characters! Please re register')
        S='\n'
        S=bname+","+authname+","+str(quan)+","+"₹"+str(price)+'\n'
        with open("Stock.txt","a+",encoding='UTF8') as f:
            f.write(S)
            f.close()
        print("~~~~~~~~~~~~~~~~Book successfully added!!~~~~~~~~~~~~~~~")
        

            
#CODE TO DELETE BOOK TO DB
def delete_bookdata():
        print("Please select a option below:")
        f=open("Stock.txt","r",encoding='UTF8')
        lines=f.readlines()
        f.close()
        c=0
        for i in lines:
            c=c+1
        print("---------------------------------------------------------------------------")
        for i in range(0,c):
            print("Enter", i, "to delete book and its data ", lines[i])
            print("---------------------------------------------------------------------------")
        ch=int(input("Enter your choice: "))
        del lines[ch]
        print("~~~~~~~~~~~~~~~Book successfully deleted!!~~~~~~~~~~~~")

        o=open("Stock.txt","w+",encoding='UTF8')

        for line in lines:
            o.write(line)
        o.close()
