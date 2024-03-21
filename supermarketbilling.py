from datetime import datetime

name=input("Enter Your name: ")
print(25*'*','WelCome To Our Market ',25*'*')
print(29*' ',name.upper(),29*'')

lists='''
         DairyMilk     50rs
         MilkyDair     30rs
         KitKat        25rs
         Five*         10rs
         Munch         10rs
         Perk          5rs'''
option=int(input("To watch the menu pls press 1: "))
if option!=1:
    print("Pls enter 1 only")
    option=int(input("To watch the menu pls press 1: "))
if  option==1:
    print(lists)

dic={ "DairyMilk":50,
         "MilkyDair":30,
         "KitKat":25,
         "Five*":10,
         "Munch":10,
         "Perk":5} 

for i in range(len(dic)):
    item=input("Choose Your item: ")
    if item=='x':
        break
    if item in dic.keys():
        quantity=int(input("enter your quantity: "))
        choice=input("Are u ready to see bill process:y/n ")
        if choice=='y':
            s=dic[item]
            price=quantity*s
            gst=(price*5)/100
            final=price+gst
            print("------------------------------------------------------------------------------")
            print('Name: ',name,25*' ',"Date: ",datetime.now())
            print("-------------------------------------------------------------------------------")
            print("ITEM ",25*' ',"QUANTITY",15*' ',"PRICE")
            print(item,25*' ',quantity,23*' ',price)
            print(47*' ',"GST",4*' ',gst)
            print("---------------------------------------------------------------------------------")
            print(47*' ',"TotalPrice=",final)
            print("---------------------------------------------------------------------------------")
            print(35*' ',"Thanks For Visiting")
            
        else:
            break  
    else:
        print("Pls choose carefully for this menu only")      
    
#exit=input("press 1 for proceed or press 2 for exit")         