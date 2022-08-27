import dt
import ListSplit


SRN_list=[]
pwsd_list=[]
name_list=list()
global SRN
global name
global pasw



def signup():
    print("---------------------------SIGN UP HERE------------------------")
    
    SRN=input("Enter your SRN: ")
    
    name=input("Enter your FULL NAME: ")
    success=True
    while success==True:
        if len(SRN)==13:
            success=False
        else:
            print("Wrong SRN....Enter again.")
            SRN=input("Enter your SRN: ")
            success=True
        
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
            print('Length of password should be between 6 and 12.')
            break
        elif digit <1:
            print('No Digits in your password.')
            break
        elif sletter <1:
            print('No small letter in your password.')
            break
        elif cletter <1:
            print('No capital letter in your password.')
            break
        elif special <1:
            print('No Special characters in your password.')
            break
        else:
            flag = 1
            with open("borrower.txt","a+",encoding='UTF8') as f:
                
                S=SRN+","+pasw+","+name+'\n'
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
    with open("borrower.txt","r",encoding='UTF8') as f:        
        lines=f.readlines()
        lines=[x.strip('\n') for x in lines]
        for i in range(len(lines)):
            ind=0
            for a in lines[i].split(','):
                if(ind==0):
                    SRN_list.append(a)
                elif(ind==1):
                    pwsd_list.append(a)
                elif(ind==2):
                    name_list.append(a)
                ind+=1
    print("-----------------------LOGIN HERE--------------------")
    success=0
    while success!=1:
        srn = input("Enter your SRN: ")
        pas = input('Password: ')
        if srn in SRN_list and pas in pwsd_list:
            found=SRN_list.index(srn)
            print("LOGIN SUCCESSFUL!!!!!")
            print("____________"+'\nWELCOME '+name_list[found].upper()+" :-"+"____________")
            global nm
            nm=name_list[found].upper()
            borrowBook()
            success=1
            
        else:
            print('Username and password not present! Sign up before Login')
            signup()

def borrowBook():
    success=False
            
    t="Borrow-"+nm+".txt"
    with open(t,"w+",encoding='UTF8') as f:
        f.write("------------------LIBRARY MANAGEMENT SYSTEM---------------------  \n")
        f.write("~~~~~~~~~~~~~~~~~~~BORROWED BY: "+nm+"~~~~~~~~~~\n")
        f.write("    DATE: " + dt.getDate()+"    TIME:"+ dt.getTime()+"\n\n")
        f.write("S.N. \t\t\t Bookname \t\t      Authorname \n" )
    
    while success==False:
        print("Please select a option below:")
        for i in range(len(ListSplit.bookname)):
            print("Enter", i, "to borrow book", ListSplit.bookname[i])
    
        try:   
            a=int(input())
            try:
                if(int(ListSplit.quantity[a])>0):
                    print("!!CONGRATS.....Book is available......")
                    with open(t,"a",encoding='UTF8') as f:
                        f.write("1. \t\t"+ ListSplit.bookname[a]+"\t\t  "+ListSplit.authorname[a]+"\n")

                    ListSplit.quantity[a]=int(ListSplit.quantity[a])-1
                    with open("Stock.txt","a+",encoding='UTF8') as f:

                    #multiple book borrowing code
                        
                        loop=True
                    count=1
                    while loop==True:
                        choice=str(input("Do you want to borrow more books? However you cannot borrow same book twice. \nPress Y for YES and N for NO."))
                        print("Fine will be charged for borrowing the same book again.!!")
                        if(choice.upper()=="Y"):
                            count=count+1
                            print("Please select an option below:-")
                            for i in range(len(ListSplit.bookname)):
                                print("Enter", i, "to borrow book", ListSplit.bookname[i])
                            a=int(input())
                            if(int(ListSplit.quantity[a])>0):
                                print("Book is available")
                                with open(t,"a",encoding='UTF8') as f:
                                    f.write(str(count) +". \t\t"+ ListSplit.bookname[a]+"\t\t  "+ListSplit.authorname[a]+"\n")

                                ListSplit.quantity[a]=int(ListSplit.quantity[a])-1
                                """with open("Stock.txt","a+",encoding='UTF8') as f:
                                    for i in range(3):
                                        f.write(ListSplit.bookname[i]+","+ListSplit.authorname[i]+","+str(ListSplit.quantity[i])+","+"$"+ListSplit.cost[i]+"\n")"""
                                        #success=False
                            else:
                                loop=False
                                break
                        elif (choice.upper()=="N"):
                            print ("!!Thank you for borrowing books from us......!! ")
                            print("")
                            loop=False
                            success=True
                        else:
                            print("Please choose as instructed")
                        
                else:
                    print("Sorry!!!Book is not available!!!")
                    borrowBook()
                    success=False
            except IndexError:
                print("")
                print("Please choose book acording to their number.")
        except ValueError:
            print("")
            print("Please choose as suggested.")
