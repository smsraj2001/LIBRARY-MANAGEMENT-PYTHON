import Return
import ListSplit
import dt
import Borrow
import admin

def start():
    while(True):
        print("--------------------------------------------------------------------------------------------")
        print("-----------------------------------WELCOME TO LIBRARY-------------------------------------")
        print("--------------------------------------------------------------------------------------------")
        print("ENTER 1. TO ENTER INTO THE ADMIN DEPARTMENT")
        print("ENTER 2. TO DISPLAY")
        print("ENTER 3. TO BORROW A BOOK")
        print("ENTER 4. TO RETURN A BOOK")
        print("ENTER 5. TO EXIT")
        
        a=int(input("Select a choice from 1-5: "))
        

        if(a==1):
            print("---------------WELCOME TO ADMIN DEPARTMENT---------------------")
            m=0
            while m==0:
                    print("---------------------------------------------------------------------------------")
                    n=0
                    while n==0:
                        print("ENTER 1. TO SIGN UP")
                        print("ENTER 2. TO LOGIN")
                        b=int(input("Select a choice: "))
                        if (b==1):
                              admin.signup()
                        elif b==2:
                            admin.login()
                        else:
                            print("Please enter a VALID CHOICE.")
                            n=0
                        n=1
                    m=1
                        
        elif(a==2):
            print("--------------------------------------------------------------------------------------------")
            f=open("Stock.txt","r",encoding='UTF8')
            lines=f.readlines()
            for line in lines:
                print(line)
                print("--------------------------------------------------------------------------------------------")
            f.close()
   
        elif(a==3):
            ListSplit.listSplit()
            n=0
            while n==0:
                print("ENTER 1. TO SIGN UP")
                print("ENTER 2. TO LOGIN")
                b=int(input("Select a choice: "))
                if (b==1):
                    Borrow.signup()
                elif b==2:
                    Borrow.login()
                else:
                    print("Please enter a VALID CHOICE.")
                    n=0
                n=1
        elif(a==4):
            ListSplit.listSplit()
            Return.returnBook()
        elif(a==5):
            print("Thank you for using our library management system!!!!VISIT AGAIN!!!!!!")
            break
        else:
            print("Please enter a valid choice from 1-5.")
            
start()
