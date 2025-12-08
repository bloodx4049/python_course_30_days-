from random import randint

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"ticket is booked in train no:{self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"train no:{self.trainNo} is running on time ")

    def getFare(self, fro, to):
        print(f"ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(234,5555)}")

t = Train(12399)
t.book("kasur", "lahore")
t.getStatus()
t.getFare("kasur", "lahore")