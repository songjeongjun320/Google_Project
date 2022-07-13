class Party:
    def __init__(self, party_number, party_size, waiting):
        self.party_size = party_size
        self.party_number = party_number
        self.waiting = waiting

    def need_table_size(self):
        if self.party_size > 4:
            return 6
        else:
            return 4

"""
waiting list를 만드는 문제입니다. 
group of people 이 party 이고 이 그룹들이 
waiting list 에서 table 이 available 할때까지 기다리고 있습니다.
 테이블의 갯수, Party 의 사이즈는 real-life 로 생각하여 자신이 
 define 하고 Party class 또한 자신이 define 하세요

Party 라는 클라스를 만들고 아래 3개의 function 을 구현하세요

void join(Party party)
void remove(Party party)
Party nextLine(int tableSize)

고객이 waiting list 에서 원할떄 언제든이 떠날 수 있습니다
"""