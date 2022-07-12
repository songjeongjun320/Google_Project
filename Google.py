from random import *
from queue import *
from Party import *

party_list = []  # List for participating the party
waiting_list = []  # List for the waiting the party

Maximum_Party = 10 # Party Maximum, Party members can't over the Maximum_Party

party1 = Party(2)
party2 = Party(2)
party3 = Party(5)
party4 = Party(2)

waiting_list.append(party1)
waiting_list.append(party2)
waiting_list.append(party3)
waiting_list.append(party4)


print(len(waiting_list))
