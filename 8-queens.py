
import random


def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i]-nextX) in (0, nextY-i):
            return True
    return False


def queens(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num-1:
                yield (pos,)
            else:
                for result in queens(num, state+(pos,)):
                    yield (pos,) + result


def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '. ' * (pos)+'X '+'. ' * (length-pos-1)
    for pos in solution:
        print(line(pos))


m = list(queens(int(input("几个皇后？"))))


print("有{:^4d}种".format(len(m)))
prettyprint(random.choice(m))
input("That's it!")
