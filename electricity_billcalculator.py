while True:
  name = str(input("Enter your name :"))
 unit=float(input("Enter your unit: "))


 if(unit<=100):
  bill=unit*1.5
 elif(unit>100 and unit<=200):
  bill=(unit - 100)*2.5 + 100*1.5
 elif(unit>200 and unit<=300):
  bill=(unit-200)*4 + 100*4
 else :
  bill=(unit-300)*6 +100*8


 if (bill>1000):
  bill=bill-bill*0.05
 
 print("your name is ",name)
 print("your total bill is ",bill)
 print("your total consumed unit is ", unit)
