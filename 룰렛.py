
import random


class RouletteEvent:

    def __init__(self):
        # 상품 정보
        self.prize = {
            1: "키움증권 100,000원 크래딧에 당첨되셨습니다! 축하드립니다!!!",
            2: "키움증권 50,000원 크래딧에 당첨되셨습니다!",
            3: "키움증권 10,000원 크래딧에 당첨되셨습니다!",
            4: "키움증권 5,000원 크래딧에 당첨되셨습니다!",
            5: "아쉽지만 당첨되지 못했습니다. 영웅문S#에서 승리하시길 바랍니다!"
        }

        # 당첨 확률
        self.probability = {
            1: 2,
            2: 5,
            3: 13,
            4: 30,
            5: 50
        }

        # 당첨 금액
        self.credit = {
            1: 100000,
            2: 50000,
            3: 10000,
            4: 5000,
            5: 0
        }

    # 프로그램 시작
    def start(self):

        print()
        print("===== 룰렛 이벤트 =====")
        print("1. 룰렛 돌리기")
        print("2. 종료")

        menu = input("번호를 선택하세요 : ")

        if menu == "1":

            credit = self.spin_roulette()

            return credit

        elif menu == "2":

            print("프로그램을 종료합니다.")
            return 0

        else:

            print("잘못된 번호입니다.")
            return 0

    # 룰렛 돌리기
    def spin_roulette(self):

        number = random.randint(1, 100)

        if number <= 2:
            rank = 1
        elif number <= 7:
            rank = 2
        elif number <= 20:
            rank = 3
        elif number <= 50:
            rank = 4
        else:
            rank = 5

        # 등수에 따른 당첨 금액
        credit = self.credit[rank]

        print()
        print("===== 룰렛 결과 =====")
        print(f"룰렛돌리기에서 {rank}등이 되셨습니다!")
        print(f"상품 : {self.prize[rank]}")
        print(f"당첨금액 : {credit:,}원")
        print("====================")

        # 당첨 금액 반환
        return credit


# 룰렛 프로그램 시작
roulette = RouletteEvent()
credit = roulette.start()
