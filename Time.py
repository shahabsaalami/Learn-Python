class Time:
    def __init__(self, h=0, m=0, s=0):
        self.hour = h if h >= 0 and h < 24 else 0
        self.minute = m if m >= 0 and m < 60 else 0
        self.seccond = s if s >= 0 and s < 60 else 0

    def printStandard(self):
        if self.hour == 0 or self.hour == 12:
            print(12, end="")
        else:
            print(self.hour % 12, end="")
        print(":", end="")
        if self.minute < 10:
            print("0", end="")
        print(self.minute, end="")
        print(":", end="")

        if self.seccond < 10:
            print("0", end="")

        print(self.seccond, end="")
        print(":", end="")

        if self.hour < 12:
            print("AM")
        else:
            print("PM")


dm = Time()
dm.printStandard()
dm.hour = 2
dm.minute = 12
dm.seccond = 3
dm.printStandard()
