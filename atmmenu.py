#data
name1="a"
id1=12345
pin1=1234
bal1=1000
name2="b"
id2=12346
pin2=1235
bal2=1034
name3="c"
id3=12347
pin3=1236
bal3=1045


wrong=0



while True:
      print("welcome to the bank \n")
      id=int(input("enter your 5 digit bank id \n "))
      pin=int(input("enter your 4 digit pin \n"))
      isreal=False

      if (id==id1 and pin==pin1):
        print("your name is ", name1)
        isreal= True
      elif(id==id2 and pin==pin2):
        print("your name is ", name2)
        isreal= True
      elif(id==id3 and pin==pin3):
        print("your name is ", name3)
        isreal= True
      else:
        print("invalid id or pin \n")
        wrong+=1
        print(3-wrong,"attempts left \n")

      if(wrong>=3):
        print("you have entered an invalid info \n")
        break
      else:
       while True:
         print("1.Check Balance \n2.Withdraw Money \n3.Deposit Money \n4.Exit")

         choice=int(input("enter your choice"))
         if(isreal):
          if(choice==1):
           if(id==id1):
            print("your balance is ", bal1)
           elif(id==id2):
            print("your balance is ", bal2)
           elif(id==id3):
            print("your balance is ", bal3)
          elif(choice==2):
            withdraw=int(input("enter the amount you want to withdraw"))
            if(withdraw>5000):
             print("withdraw limit exceeded")
            else:
              if(id==id1):
               if(withdraw>bal1):
                print("insufficient balance")
               else:
                bal1-=withdraw
                print("your balance is ", bal1)
              elif(id==id2):
                if(withdraw>bal2):
                 print("insufficient balance")
                else:
                 bal2-=withdraw
                 print("your balance is ", bal2)
              else:
                if(withdraw>bal3):
                 print("insufficient balance")
                else:
                 bal3-=withdraw
                 print("your balance is ", bal3)
          elif(choice==3):     
            deposit=int(input("enter the amount you want to deposit"))
            if(id==id1):
              bal1+=deposit
              print("your balance is ", bal1)
            elif(id==id2):
              bal2+=deposit
              print("your balance is ", bal2)
            elif(id==id3):
              bal3+=deposit
              print("your balance is ", bal3)
          elif(choice==4):
            break
          else:
            print("invalid choice")

