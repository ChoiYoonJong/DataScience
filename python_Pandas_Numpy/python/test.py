print("지금부터 타이머 시작을 누르고 문제를 풀어보세요")
second =int(input("문제를 해결하셨나요? 총 몇초가 걸렸나요? >>>"))

minute = second // 60
remainder = second % 60

print(f"총 {minute}분 {remainder}초만에 문제를 해결 하셨군요!")