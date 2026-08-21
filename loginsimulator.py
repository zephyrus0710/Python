import time
balance=10000
pin="7391"
pinc=1
wrpin=1

ndepo=0 
nwitdrw=0
high_depo=0
high_withdrw=0
total_depo=0
total_withdrw=0


while True:
    print("===== BANK ATM =====")
    ipin=input("enter your pin :\n")

    while pin != ipin:
        print("incorrect pin")
        time.sleep(1)
        ipin=input("enter your pin again : \n")
        pinc+=1
        if(pinc==3):
         print("Too many incorrect attempts ")
         quit()
    start=time.time()
    pinc=1
    while True:
       print("""========== ATM ==========
 1. Check Balance
 2. Deposit
 3. Withdraw
 4. Change PIN
 5. Transaction Summary
 6. Logout
==========================""")

       c1=int(input("enter your choice :\n"))

       if c1==1 :
          print(f"Current Balance: {balance:,.2f}")
       elif c1==2 :
          depo=int(input("enter deposit amount : \n"))
          if depo <=0:
             print("enter correct amount")
             break
          elif depo % 100 != 0:
             print("amount must be multiple of 100")
             break
          else:
             print("processing...")
             time.sleep(2)
             print("Deposit Successful ")
             ndepo+=1
             total_depo+=depo
             latest_depo=depo
             if latest_depo>high_depo:
                high_depo=latest_depo
             balance += depo
             print(f"New Balance: {balance:,.2f}")

       elif c1==3 :
          withdrw =int(input("enter withdrawal amount : \n"))
          if withdrw <=0:
             print("enter correct amount")
             break
          elif withdrw % 100 != 0:
             print("amount must be multiple of 100")
             break
          elif withdrw >=balance:
             print("not enough balance")
             break
          else:
             print("processing...")
             time.sleep(2)
             print("Withdrawal Successful ")
             nwitdrw+=1
             latest_withdrw=withdrw
             if latest_withdrw>high_withdrw:
                high_withdrw=latest_withdrw
             balance -= withdrw
             total_withdrw+=withdrw
             print(f"Remaining Balance: {balance:,.2f}")
             c2=input("Print receipt? (y/n):")
             c2=c2.lower()
             while c2!="y" and c2!="n" :
                c2=input("enter a valid choice")
                c2=c2.lower()
             if c2=="y":
                print("========== RECEIPT ==========")
                print("Date:",time.strftime("%d/%m/%Y"))
                print("Time:",time.strftime("%H:%M:%S"))
                print(f"Withdrawal Amount:{withdrw:,.2f}")
                print(f"Balance:{balance:,.2f}")
                print("==============================")
             else:
                break

       elif c1==4 :
          pin1=input("Enter your current pin : \n")
          while pin1 != pin:
             print("invalid pin")
             wrpin+=1
             pin1=input("Enter your current pin: \n")
             if wrpin==3:
                print("too many incorrect attempts")
                break
          newpin=input("Enter the new pin: \n")
          wrpin=1
          while True:
             if not newpin.isdigit():
               print("it must not contain letters")
               newpin=input("Enter the new pin: \n")
             elif len(newpin)<4:
               print("too short")
               newpin=input("Enter the new pin: \n")
             elif len(newpin)>4:
                print("too long")
                newpin=input("Enter the new pin: \n")
             elif newpin==pin:
                print("pin can't same as before")
                newpin=input("Enter the new pin: \n")
             else:
                print("pin changed successfully")
                pin=newpin
                break
       elif c1==5 :
          print("====== TRANSACTION SUMMARY ======")
          print("Deposits:")
          print(f"Numbers:{ndepo}")
          print(f"Total:{total_depo}")
          print(f"Largest:{high_depo}")
          print("\n")
          print("Withdrawals:")
          print(f"Number:{nwitdrw}")
          print(f"Total:{total_withdrw}")
          print(f"Largest:{high_withdrw}")
       elif c1==6 :
          print("Logging Out... ")
          end=time.time()
          print(f"session duration {end-start}seconds")
          break
       else:
          print("invalid choice")

