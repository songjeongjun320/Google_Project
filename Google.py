from asyncio.windows_events import NULL
from random import *
from re import I

from soupsieve import select
from Party import *
from Table import *

"""
4 tables with 4 seats
2 tables with 6 seats
"""

table_list_size4 = [] # List for the table (table_size = 4)
using_table_size4 = 0 # If there is avaialble size 4 table = True, If not = False
table_list_size6 = [] # List for the table (table_size = 6)
using_table_size6 = 0  # If there is avaialble size 6 table = True, If not = False
waiting_list = []  # List for the waiting the party

def select_table(table_size):
    if table_size == 4:
        out_table_number = randint(0,3)
    elif table_size == 6:
        out_table_number = randint(0,1)
    return out_table_number

def party_size(): # Function for Party's Size
    size = 0
    for i in range(len(table_list_size4)):
        size += table_list_size4[0].party_size
    return size

def join(party): # Function for Participating Party
    global using_table_size4
    global using_table_size6

    party_joined = False # for distinguishing that party could sit the table
                         # (False = Couldn't join, True = Could join)

    if party.waiting == False:
        print("{0}번 파티 그룹이 기다리지 않고 떠납니다.".format(party.party_number))
        waiting_list.pop(0)        
        return NULL

    if 4 < party.party_size and party.party_size <= 6: # if party size is over 4
        if using_table_size6 == 2: # All size6 tables are using
            out_table_number = select_table(6) # which size table will be empty
            using_table_size6 -= 1
            print(using_table_size6)
            remove(table_list_size6[out_table_number].party) # make empty this table
        else:
            for i in range(2): # search which table is empty (size6)
                if table_list_size6[i].table_availability == True: # If number i table is available
                    table_list_size6[i].table_join(party)
                    party_joined = True
                    print("{0}번 파티 그룹이 6-{1}번 테이블이 착석.".\
                    format(party.party_number, table_list_size6[i].table_number))
                    using_table_size6 += 1
                    print(using_table_size6)
                    waiting_list.pop(0)
                    break

    elif party.party_size <= 4:
        if using_table_size4 == 4: # All size4 tables are using
            out_table_number = select_table(4) # which table will be empty
            using_table_size4 -= 1
            print(using_table_size4)
            remove(table_list_size4[out_table_number].party) # make empty this table
        else:
            for i in range(4): # Search which table is empty 
                if table_list_size4[i].table_availability == True:
                    table_list_size4[i].table_join(party)
                    party_joined = True
                    print("{0}번 파티 그룹이 4-{1}번 테이블이 착석.".\
                    format(table_list_size4[i].party.party_number, table_list_size4[i].table_number))
                    using_table_size4 += 1
                    print(using_table_size4)
                    waiting_list.pop(0)
                    break

    if party_joined == False:
        pass
        

def remove(party): # Function for Leaving the party
    global using_table_size4
    global using_table_size6

    if party.party_size > 4:
        for i in range(len(table_list_size6)):
            if table_list_size6[i].party.party_number == party.party_number:
                table_list_size6[i].table_left()
                print("{0}번 파티가 6-{1}번 테이블에서 나감."\
                    .format(party.party_number, table_list_size6[i].table_number))
                using_table_size6 -= 1
                print(using_table_size6)
                break
    elif party.party_size <= 4:
        for i in range(len(table_list_size4)):
            if table_list_size4[i].party.party_number == party.party_number:
                table_list_size4[i].table_left()
                print("{0}번 파티가 4-{1}번 테이블에서 나감."\
                    .format(party.party_number, table_list_size4[i].table_number))
                using_table_size4 -= 1
                print(using_table_size4)
                break

def check_table_availability(tableSize):
    if tableSize == 4 and using_table_size4 < 4:
        return True
    elif tableSize == 4 and using_table_size4 == 4:
        return False
    elif tableSize == 6 and using_table_size6 < 2:
        return True
    elif tableSize == 6 and using_table_size6 == 2:
        return False

def nextLine(tableSize):
    return waiting_list[0]

# Creating Table(size4) instance
size4_table1 = Table(1,4)
size4_table2 = Table(2,4)
size4_table3 = Table(3,4)
size4_table4 = Table(4,4)

# Put the size4 tables in table_list_size4
table_list_size4.append(size4_table1)
table_list_size4.append(size4_table2)
table_list_size4.append(size4_table3)
table_list_size4.append(size4_table4)

# Creating Table(size6) instance
size6_table1 = Table(1,6)
size6_table2 = Table(2,6)

# Put the size6 tables in table_list_size6
table_list_size6.append(size6_table1)
table_list_size6.append(size6_table2)

# Creating Party instance
next_party = Party(0,0,True) # nextLine party group
party1 = Party(1,2,True)
party2 = Party(2,2,True)
party3 = Party(3,5,True)
party4 = Party(4,2,False)
party5 = Party(5,6,True)
party6 = Party(6,4,True)
party7 = Party(7,3,True)
party8 = Party(8,2,False)
party9 = Party(9,6,True)
party10 = Party(10,4,True)
party11 = Party(11,3,True)
party12 = Party(12,4,False)
party13 = Party(13,6,True)
party14 = Party(14,2,True)
party15 = Party(15,4,True)
party16 = Party(16,4,False)

# Put the parties in waiting_list
waiting_list.append(party1)
waiting_list.append(party2)
waiting_list.append(party3)
waiting_list.append(party4)
waiting_list.append(party5)
waiting_list.append(party6)
waiting_list.append(party7)
waiting_list.append(party8)
waiting_list.append(party9)
waiting_list.append(party10)
waiting_list.append(party11)
waiting_list.append(party12)
waiting_list.append(party13)
waiting_list.append(party14)
waiting_list.append(party15)
waiting_list.append(party16)

# party instances join the party
while True:
    next_party = nextLine(waiting_list[0].need_table_size())
    print(next_party.party_number)
    join(next_party)
