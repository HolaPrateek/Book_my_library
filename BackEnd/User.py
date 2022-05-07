# -*- coding: utf-8 -*-
"""
Created on Sat May  7 10:44:55 2022

@author: Prasanna , Manju
"""
from  Booking_system import *


def Notifications(info,Id,schedule1):
    schedule=schedule1
    for i in info[Id]["Notifications"]:
        print(f'{info[i[0]]["Name"]} invited for group study \n \nin {i[1]} slot at table no. {i[2]} and seat no. {i[3]}\n')
        decision=input(f'Do you want to join {info[i[0]]["Name"]} group study')
        if (decision.lower()=="yes"):
            schedule=allot_seat(schedule,i[1], i[2], i[3],Id,"Book")
        else:
            schedule=allot_seat(schedule,i[1], i[2], i[3],Id,"Empty")
    return schedule


def check_in(Id,info,schedule1):
    schedule=schedule1
    entry=input("enter your entry time(HH:MM:SS):  " )
    slot1=info[Id]["slots"][0]
    time_zero = datetime.strptime('00:00:00', '%H:%M:%S')
    entry=datetime.strptime(str(entry),"%H:%M:%S")
    start=datetime.strptime(str(et[slot1-1]),"%H:%M:%S")
    diff=entry- start
    diff=datetime.strptime(str(diff) ,"%H:%M:%S")
    diff=(diff.hour*60)+diff.minute                           
    diff=int(diff)
    d=random.randint(1,100000)
    print("Unique pass(shown in library and changes every 5 minutes):",d)
    check_in_pass=int(input("\nEnter the unique pass of library: "))
    if(check_in_pass==d  and   diff <=10):
        print("\n----------- YOUR ARE PERMITTED-------------\n")
        print("\n----------- HAPPY READING \(^-^)/----------\n")
        return schedule
    else:
        schedule=allot_seat(schedule,info[Id]["slots"][0],info[Id]["slots"][1],info[Id]["slots"][2], Id,"Empty")
        print("-----------SORRY YOUR NOT PERMITTED------------")
        return schedule  
    
def login(info):
    
        Id=int(input("Enter your Identification number:"))
        if Id in info.keys():
            for i in range(3):
                password=int(input("Enter your password:"))
                if (password==info[Id]["password"]):
                    print("Login successful")
                    return True,Id
                elif(i==2):
                    print("Can't attempt sign in anymore")
                    return False
                else:
                    print(f'Wrong password,you have {2-i} chances left')
                    pass
        else:
            print("Enter correct User Id")
            return False,-1
        
#def notifications(info):
"""def Check_in():
    d=random.randint(1,100000)
    print("Unique pass(shown in library and changes every 5 minutes):",d)
    check_in_pass=int(input("\nEnter the unique pass of librry: "))
    if(check_in_pass==d):
        return True
    else:
        return False """  
        
def window(info,schedule):
    schedule1=schedule
    Login,Id=login(info)
    while Login==True:
        choice=int(input(" 1) Book seat for individual\n\n 2) Book seat for Group study\n\n 3) Notifications\n\n 4)Check-in library\n\n 5) Sign out\n\n"))
        if (choice==1):
            schedule1=main(info,schedule,Id,"Single")
            back=input("Do you want to go back to main menu.")
            if(back.lower()=="yes"):
                pass
            else:
                return schedule1
        elif(choice==2):
            
            schedule1=main(info,schedule,Id,"Multiple")
            if(back.lower()=="yes"):
                pass
            else:
                return schedule1
            return schedule1
        elif(choice==3):
            schedule1=Notifications(info,Id,schedule)
            return schedule1
        elif(choice==4):
            schedule1=check_in(Id,info,schedule)
            if(back.lower()=="yes"):
                pass
            else:
                return schedule1
            return schedule1
        if(choice==5):
            Login=False
        else:
            print("Please enter a valid choice.")
        
    
    
    
info={123: {'password': 123, 'Name': 'Prasanna', 'slots': [], 'Notifications': []}, 124: {'password': 124, 'Name': 'Manju', 'books': [], 'Notifications': [[123, 4, 4, 2]]}}
schedule=create_library(5, 6, "8:30:00", "20:00:00", "01:30:00")
schedule=window(info,schedule)
#print(schedule)