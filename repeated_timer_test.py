from repeated_timer import RepeatedTimer


class Amazing:
    def __init__(self):
        self.i = RepeatedTimer(2, self.increment, 1)
        self.j = RepeatedTimer(10, self.decrement, 2)

    def increment(self, i):
        print(i)

    def decrement(self, j):
        print(j)


well = Amazing()
