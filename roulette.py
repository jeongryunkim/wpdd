import random


class RouletteEvent:

    def __init__(self):
        self.prize = {
            1: "키움증권 100,000원 크레딧에 당첨되셨습니다! 축하드립니다!!!",
            2: "키움증권 50,000원 크레딧에 당첨되셨습니다!",
            3: "키움증권 10,000원 크레딧에 당첨되셨습니다!",
            4: "키움증권 5,000원 크레딧에 당첨되셨습니다!",
            5: "아쉽지만 당첨되지 못했습니다. 영웅문S#에서 승리하시길 바랍니다!"
        }

        self.credit = {1: 100000, 2: 50000, 3: 10000, 4: 5000, 5: 0}
        self.is_played = False

    def start(self):
        if self.is_played:
            print("\n룰렛 이벤트는 이미 참여하셨습니다.")
            return 0

        print("\n===== 룰렛 이벤트 =====")
        print("1. 룰렛 돌리기")
        print("2. 돌아가기")

        menu = input("번호를 선택하세요 : ")

        if menu == "1":
            self.is_played = True
            return self.spin_roulette()
        else:
            print("이벤트를 취소합니다.")
            return 0

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

        credit = self.credit[rank]

        print("\n===== 룰렛 결과 =====")
        print(f"룰렛돌리기에서 {rank}등이 되셨습니다!")
        print(f"상품 : {self.prize[rank]}")
        print(f"당첨금액 : {credit:,}원")
        print("====================")

        return credit