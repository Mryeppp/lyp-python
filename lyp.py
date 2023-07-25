
'''
import time
class CLOCK(object):
     def __init__(self,hour,min,sec) -> None:
          self.hour=hour
          self.min=min
          self.sec=sec
     def run(self):
          self.sec+=1
          if self.sec==60:
               self.sec=0
               self.min+=1
               if self.min==60:
                    self.min=0
                    self.hour+=1
                    if self.hour==24:
                         self.hour=0
     def show(self):
          return '%d:%d:%d'%(self.hour,self.min,self.sec)
def main():
 clock=CLOCK(23,59,58)
 while(1):
     print(clock.show())
     time.sleep(1)
     clock.run()
main()
'''   



# import timeit 
# popzero=timeit.Timer("x.pop(0)","from __main__ import x")
# popend=timeit.Timer("x.pop()","from __main__ import x")
# x=list(range(2000000))
# timex1=popzero.timeit(number=1000)
# x=list(range(2000000))
# timex2=popend.timeit(number=1000)
# print(f"15.5%f,15.5%f",(timex1,timex2))
