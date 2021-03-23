# import math
# import itertools
# import numpy as np
mod = 10 ** 9 + 7
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]


def solution(A):
    past_sign = 0  # 0:不明 1:＋　-1:-
    count = 0
    for i in range(len(A) - 1):
        # 前の木の高さとの差をとって符号を決定する
        if (A[i] - A[i + 1] < 0):
            sign = -1
        else:
            sign = 1

        # 前回の符号と同じか判定
        if past_sign == sign:
            count += 1
            sign = sign * -1

        past_sign = sign

    return count


def main():
    A = [5,6,7,8,9,10]
    ans = solution(A)
    print(ans)


if __name__ == "__main__":
    main()