# -*- coding: utf-8 -*-
"""
Created on Thu May  5 18:05:44 2022

@author: Prasannakumar Swami
"""

import random
from datetime import *
et=[]

"""This function creates customized seating 
arrangements of library ,tables
 shows rows and seats for seats  per row"""
 
def create_slot(tables,seats):
    
    """seating_arrangement is a list of lists 
    with inner lists having initial value equal 
    to zero indicating no one is sitting on the seat currently."""
    
    seating_arrangement=[[0 for j in range(seats)] for i in range (tables)]
    return seating_arrangement



def display(arrangement):
    print("Seat No. ",end='   ')
    for j in range(len(arrangement[0])):
        print(f'      {j+1}      ',end='')
    print("\n")
    for i in range(len(arrangement)):
        print(f'Table no. {i+1}',end='  ')
        for j in range(len(arrangement[i])):
            if(arrangement[i][j]==0):
                print("[  Vacant  ]",end=' ')
            elif(arrangement[i][j]==-1):
                print(f'[ Requested ]',end=' ')
            else:
                print(f'[    {arrangement[i][j]}   ]',end=' ')
        print("\n")
                
    

def allot_seat(arrangement,slot,table_no,seat_no,user_id,status):
    if (status=="Book"):
        if (arrangement[slot-1][table_no-1][seat_no-1]==0)or(arrangement[slot-1][table_no-1][seat_no-1]==-1):
            arrangement[slot-1][table_no-1][seat_no-1]=user_id
            print(f'Row:{table_no} seat no.:{seat_no} successfully booked.') 
            return arrangement
        else:
            print(f'In row:{table_no} seat no.:{seat_no} is already booked please book another seat.')
            return arrangement
    elif(status=="Request"):
        if (arrangement[slot-1][table_no-1][seat_no-1]==0):
            arrangement[slot-1][table_no-1][seat_no-1]=-1
            print(f'Row:{table_no} seat no.:{seat_no} has been requested.') 
            return arrangement
        else:
            print(f'In row:{table_no} seat no.:{seat_no} is already booked please book another seat.')
            return arrangement
    elif(status=="Empty"):
        if (arrangement[slot-1][table_no-1][seat_no-1]!=0):
            arrangement[slot-1][table_no-1][seat_no-1]=0
            print(f'Row:{table_no} seat no.:{seat_no} has been vacant.') 
            return arrangement
        else:
            print(f'In row:{table_no} seat no.:{seat_no} is already empty.')
            return arrangement
        
        


def slots_creation(lib_start_time,lib_close_time,time_interval_slot):
    #intializing
    start=datetime.strptime(str(lib_start_time),"%H:%M:%S")
    end=datetime.strptime(str(lib_close_time),"%H:%M:%S")
    time_zero = datetime.strptime('00:00:00', '%H:%M:%S')

    
    time_interval = end- start
    time=datetime.strptime(str(time_interval) ,"%H:%M:%S")
    tm=(time.hour*60)+time.minute
    
    td=datetime.strptime(str(time_interval_slot) ,"%H:%M:%S")
    interval=(td.hour*60)+td.minute                               #time duaration in minutes
    #minutes=int((((end%1)-(start%1))*100)+60*(int(end)-int(start)))
    no_slots=int(tm/interval) # changed to minutes
    t3=start
    t4=start
    time_duration = datetime.strptime(str(time_interval_slot),"%H:%M:%S")  
    print("| SLOTS|    TIME            |")
    print("=============================")
    for i in range(no_slots):
         t4 = t3 - time_zero + time_duration
         et.append(t3.strftime("%H:%M:%S"))
         print("|slot"+str(i+1)+"  | "+t3.strftime("%H:%M:%S")+"--"+t4.strftime("%H:%M:%S")+"|")
         print("-----------------------------")
         t3=t4
    
    library_slots=[[] for i in range(no_slots)]     # slots creation
    
    return library_slots
    
    
def create_library(tables,seats_per_table,start,end,slot_duration):
    library=slots_creation(start, end, slot_duration)
    slot=create_slot(tables, seats_per_table)
    library=[[[0 for n in j] for j in slot  ] for s in library]
    return library

def main(info,schedule0,Id,status):
    print("Welcome to library Booking System\n\n\n")
    """tables=int(input("How much tables do library consist:"))
    seats=int(input("How much seats does one table serve:"))
    start=(input("What is your opening time of library:"))
    end=(input("What is your closing time of library:"))
    time_duration_of_slot=(input("Enter your time duration per slot:"))"""
    
    schedule=schedule0
    if(status=="Multiple"):
        slot=int(input(f'There are total {len(schedule)} slots . Enter your slot no. to book:'))
        
        display(schedule[slot-1])
        
        table_no=int(input("Enter your table no.:"))
        seat_no=int(input("Enter your seat no.:"))
        
        schedule=allot_seat(schedule,slot, table_no, seat_no,Id,"Book")
        info[Id]["slots"].extend([slot,table_no,seat_no])
        response="yes"
        while(response.lower()=="yes"):
            grp_id=int(input("Enter your friends Id: "))
            table_no=int(input("Enter your table no.:"))
            seat_no=int(input("Enter your seat no.:"))
            info[grp_id]["Notifications"].append([Id,slot,table_no,seat_no])
            schedule=allot_seat(schedule,slot, table_no, seat_no,grp_id,"Request")
            display(schedule[slot-1])
            response=input("Do you want to book additional seat:")
    else:
        slot=int(input(f'There are total {len(schedule)} slots . Enter your slot no. to book:'))
        display(schedule[slot-1])
        table_no=int(input("Enter your table no.:"))
        seat_no=int(input("Enter your seat no.:"))
        schedule=allot_seat(schedule,slot, table_no,seat_no, Id,"Book")
        info[Id]["slots"].extend([slot,table_no,seat_no])
        display(schedule[slot-1])
        
   
         # 10 mins checking in...........................
        
        
        
        
    
    return schedule
    
    




