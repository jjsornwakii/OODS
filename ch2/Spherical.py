from math import pi 
class Spherical:

    def __init__(self,r):
        self.radius = r
        ### Enter Your Code Here ###

    def changeR(self,Radius):
        self.radius = Radius
        ### Enter Your Code Here ###

    def findVolume(self):
        return self.radius**2 * 3.1415926535897931 * 4
        ### Enter Your Code Here ###

    def findArea(self):
        ### ตำแหน่ง operation ก่อนหลัง มีผลต่อทศนิยม
        return (4.0 / 3.0) * 3.1415926535897931 * self.radius**3   
        ### Enter Your Code Here ###

    def __str__(self):
        '''
        print("Radius =",self.r,sep='',end='')
        print(" Valumn =",self.findArea(),end='')
        print(" Area =",self.findVolume()) '''
        
        strs = "Radius ="+str(self.radius)+" Volumn = "+str(self.findArea())+" Area = "+str(self.findVolume())

        return strs
        ### Enter Your Code Here ###

r1, r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(dir(R1))
print(R1)
R1.changeR(int(r2))
print(R1)