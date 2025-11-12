class Ohms:
     def __init__(self):
     #data members
           self.cur = 0.0
           self.res = 0.0
           self.volts = 0.0 

     #set methods
     def setcur(self,c):
           self.cur = c
     def setres(self,r):
           self.res = r
     def setvolts(self,v):
          self.volts = v
     
     #get methods
     def getcur(self):
          return self.cur
     def getres(self):
          return self.cur
     def getvolts(self):
          return self.cur
     
     #mutator methods
     def calccur(self):
          self.cur = self.volts / self.res
     def calcvolts(self):
          self.volts = self.cur * self.res
     def calcres(self):
          self.res = self.volts / self.cur
