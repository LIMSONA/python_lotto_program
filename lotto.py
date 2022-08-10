import os
import sys
import pickle
import random
import time
from datetime import datetime

class Inform:
    def __init__(self,rnd,date,nums):
        self.rnd = rnd
        self.date = date
        self.nums = nums

        #기록 넣기
        record[rnd]={"date":date, "nums":nums}

class Play:

    #1번 번호추첨
    def draw():
        randoms = random.sample(range(1, 46), 6) #타입은 리스트
        for i in randoms:
            print(i,end=" ")
            time.sleep(1)
        ymd = str(datetime.now()).split() # ymd[0]  ex)2022-01-20 문자열
        if len(list(record.keys()))!=0: rnd = max(list(record.keys()))+1
        else: rnd = 1
        Inform(rnd, ymd[0], randoms)

        record[rnd]["date"]=ymd[0]
        record[rnd]["nums"]=randoms

        time.sleep(1)
        print("\n{}   :   {}회차 추첨번호는 {} 입니다.\n".format(ymd[0],rnd,randoms))

    #2번 추첨기록 (원하는 회차)
    def record_want():
        print("원하는 회차의 추첨기록을 조회할 수 있습니다.")
        select = int(input("원하는 회차 입력 ▷▶▷▶  "))
        print("{}   :   {}회차 추첨번호는 {}입니다.\n".format( record[select]['date'], select, record[select]['nums']))

    #3번 추첨기록 (전체 회차)
    def record_all():
        print("전체 회차 추첨기록\n")
        for k,v in record.items():
            print("{}   :   {}회차 추첨번호는 {} 입니다.".format(v['date'],k,v['nums']))


class NDsystem:
    def first():
        print("\n★ 웰컴 ★\n1~45까지의 숫자 중 6개를 뽑는 프로그램입니다! ^.^")
        print("원하시는 메뉴를 입력 해주세요!")
        print(" [1] 번호 추첨 \n [2] 추첨 기록(원하는 회차) \n [3] 추첨 기록(전체 회차) \n [4] 프로그램 종료\n")
        select = int(input("번호 입력 ▷▶▷▶  "))

        #1번 번호 추첨
        if select==1:
            print("========================\n     [1] 번호 추첨\n========================")
            print("긴장감을 위해 숫자 하나하나씩 보여집니다.")
            time.sleep(1)
            Play.draw()
            print("\n>>> 첫 화면으로 이동합니다    ")
            time.sleep(2)

        #2번 추첨 기록(원하는 회차)
        elif select==2:
            print("========================\n [2] 추첨 기록(원하는 회차)\n========================")
            print("현재까지 추첨된 번호의 기록은 다음과 같습니다\n")
            Play.record_want()
            print("\n>>> 첫 화면으로 이동합니다    ")
            time.sleep(1)

        #3번 추첨 기록(전체 회차)
        elif select==3:
            print("========================\n [3] 추첨 기록(전체 회차)\n========================")
            print()
            Play.record_all()
            print("\n>>> 첫 화면으로 이동합니다    ")
            time.sleep(1)

        #4번 프로그램 종료
        elif select==4:
            print("프로그램을 종료합니다! \n  GOOD LUCK ♣")
            with open("number_record","wb") as f:
                pickle.dump(record,f)
            sys.exit()


record = {}

if __name__ == "__main__":
    if os.path.isfile("number_record"):
        with open("number_record","rb") as f:
            record = pickle.load(f)

    while True: NDsystem.first()
