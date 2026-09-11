# 사용자 정보 리스트
# 0번 슬롯 = credit (현재 보유 크레딧)
# 1번 슬롯 = event3 (이벤트 3 참여 여부)
usersss = [0, 0]

class EventQuiz:

    def __init__(self, usersss):

        # 전달받은 사용자 정보 리스트
        self.user = usersss

    def event_quiz(self):

        # usersss[1] = event3
        # 0이면 아직 이벤트에 참여하지 않은 상태
        if self.user[1] == 0:

            print('"주식시장에서 바보보다 주식이 많으면 사야 할때 이고,"')
            print('"주식이 아니라 바보가 많으면 팔아야 할때"라는 명언을 남긴 투자의 대가는?')

            print("1번 : 워렌버핏")
            print("2번 : 벤저민 그레이엄")
            print("3번 : 앙드레 코스톨라니")
            print("4번 : 피터 린치")
            print("5번 : 짐 로저스")

            # 정답
            answer = 3

            # 사용자에게 정답 입력받기
            aa = int(input("정답은?:"))

            # 정답을 맞힌 경우
            if aa == answer:

                print("정답입니다! 5000원 크레딧을 획득 하셨습니다.")

                # usersss[0] = credit
                # 기존 credit에 5000원 추가
                self.user[0] += 5000

            # 정답을 틀린 경우
            else:

                print("아쉽지만 틀렸습니다. 다음기회에 🥺")

            # usersss[1] = event3
            # 이벤트 참여 여부를 1로 변경
            self.user[1] += 1

        # 이미 이벤트에 참여한 경우
        else:

            print("이미 참여한 이벤트 입니다!")

        # 최종 credit 반환
        # usersss[0]에 들어있는 현재 크레딧을 반환
        return self.user[0]


# EventQuiz 객체 생성
# a = EventQuiz(usersss)

# 이벤트 실행 후 최종 credit을 변수에 저장
# credit = a.event_quiz()