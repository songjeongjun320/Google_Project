from random import *
from Party import *

party_list = []  # List for participating the party
waiting_list = []  # List for the waiting the party

Maximum_Party = 10 # Party Maximum, Party members can't over the Maximum_Party

def party_size(): # Function for Party's Size
    size = 0
    for i in range(len(party_list)):
        size += party_list[0].party_size
    return size

def join(party): # Function for Participating Party
    if party_size() < 10:
        party_list.append(party)
        print("{0}번 파티 그룹이 참여합니다.".format(party.ticket))
        waiting_list.pop(0) # erase the team which participate the party in waiting list
    else:
        pass


def remove(party): # Function for Leaving the party
    party_list.pop(0)
    print("{0}번 파티 그룹이 떠납니다.".format(party.ticket))

def nextLine(tableSize):
    pass

# Creating Party instance
party1 = Party(2,1)
party2 = Party(2,2)
party3 = Party(5,3)
party4 = Party(2,4)

# Put the parties in waiting_list
waiting_list.append(party1)
waiting_list.append(party2)
waiting_list.append(party3)
waiting_list.append(party4)

# party instances join the party
join(party1)
join(party2)
join(party3)
join(party4)

remove(party1)
remove(party2)
remove(party3)
remove(party4)