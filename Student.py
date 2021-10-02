class Student:


        def __init__(self):
            self.avg = 0.0
        def readData(self):
            self.name= (input("Please Enter name :"))
            self.stNo= (input("Please Enter Student id :"))
            self.avg= (input("Please Enter Avrage :"))
        def getAvr(self):
            return  self.avg

        def DSP(self):
            print("name is = ",self.name)
            print("stNo is = ",self.stNo)
            print("avg is = ",self.avg)


st = Student()
st.readData()
st.DSP()