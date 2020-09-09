class CollatzSequence:
    def __init__(self, numberUser):
        self.numberUser = numberUser
        self.ans = numberUser % 2

    def evenOrOdd(self):
        if self.numberUser % 2 != 0:
            return self.numberUser * 3 + 1
        else:
            return self.numberUser / 2

    def untilOne(self):
        if self.ans == 1:
            return 'Es one'
        else:
            self.ans //= 2
            print(self.ans)
            return self.untilOne()


if __name__ == '__main__':
    try:
        user = int(input('Number: '))

        collatzS = CollatzSequence(user)

        print(collatzS.evenOrOdd())
    except ValueError:
        print('Broooooo')

