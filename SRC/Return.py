import ListSplit
import dt
global data
def returnBook():
    data=""
    name=input("Enter name of BORROWER: ")
    a="Borrow-"+name+".txt"
    try:
        with open(a,"r",encoding='UTF8') as f:
            lines=f.readlines()
            lines=[a.strip(" ") for a in lines]
    
        with open(a,"r",encoding='UTF8') as f:
            data=f.readlines()
           
    except:
        print("The borrower name is incorrect!!!")
        returnBook()

    b="Return-"+name+".txt"
    with open(b,"w+",encoding='UTF8')as f:
        f.write("--------------------LIBRARY MANAGEMENT SYSTEM--------------------- \n")
        f.write(" ~~~~~~~~~~~~~~~~~~~ RETURNED BY: "+ name+"~~~~~~~~~~~~~~~~~~\n")
        f.write("    DATE: " + dt.getDate()+"    TIME:"+ dt.getTime()+"\n\n")
        f.write("S.N.\t\t\t BOOKNAME \t\t\t AUTHOR NAME\n")


    total=0.0
    with open("Return-"+name+".txt","a+",encoding='UTF8') as f:
        with open(a,"r",encoding='UTF8') as t:
            lines=t.readlines()
            for i in range(5,len(lines)):
                f.write(lines[i]+'\n')
                #ListSplit.quantity[i]=int(ListSplit.quantity[i])+1
                #total+=float(ListSplit.cost[i])
            
    print("\t\t\t\t\t\t\t"+"₹"+str(total))
    print("Is the book return date EXPIRED?")
    print("Press Y for Yes and N for No")
    stat=input()
    if(stat.upper()=="Y"):
        print("By how many days was the book returned late?")
        day=int(input())
        fine=2*day
        with open(b,"a",encoding='UTF8')as f:
            f.write("\t\t\t\t\tFine: ₹"+ str(fine)+"\n")
        total=total+fine
    


    print("Final Total: "+ "₹"+str(total))
    with open(b,"a",encoding='UTF8')as f:
        f.write("\t\t\t\t\tTOTAL FINE: ₹"+ str(total))


