# 사용자 정보 리스트
# 0번 슬롯 = credit (현재 보유 크레딧)
# 1번 슬롯 = event3 (이벤트 3 참여 여부)
class EventQuiz:
    def __init__(self, usersss):
        self.user = usersss

    def event_quiz(self):
        if self.user[1] == 0:
            print('\n"주식시장에서 바보보다 주식이 많으면 사야 할때 이고,"')
            print(
                '"주식이 아니라 바보가 많으면 팔아야 할때"라는 명언을 남긴 투자의 대가는?'
            )

            print("1번 : 워렌버핏")
            print("2번 : 벤저민 그레이엄")
            print("3번 : 앙드레 코스톨라니")
            print("4번 : 피터 린치")
            print("5번 : 짐 로저스")

            answer = 3

            try:
                aa = int(input("정답은?: "))
            except ValueError:
                print("숫자 형식으로 정답을 입력해 주세요.")
                return self.user[0]

            if aa == answer:
                print("정답입니다! 5,000원 크레딧을 획득하셨습니다.")
                self.user[0] += 5000
            else:
                print("아쉽지만 틀렸습니다. 다음 기회에 🥺")

            self.user[1] = 1
        else:
            print("\n이미 참여한 이벤트입니다!")

        return self.user[0]

# EventQuiz 객체 생성
# a = EventQuiz(usersss)

# 이벤트 실행 후 최종 credit을 변수에 저장
# credit = a.event_quiz()