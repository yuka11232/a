class IterandGen:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return (x ** 2 for x in range(self.n))


obj = IterandGen(5)

for value in obj:
    print(value)
