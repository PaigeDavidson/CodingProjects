from time import time


class FakeTimer:
    def __init__(self):
        self.baseTime = time()

    def getElapsedTime(self):
        return time() - self.baseTime

    def resetBaseTime(self):
        self.baseTime = time()