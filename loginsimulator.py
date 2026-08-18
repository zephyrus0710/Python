name = "nasif"
pas = "Python123"
count =0
c=input("do you want to login (y/n)")

if c =="y":
  while count !=3:
    usnm=input(" enter your username :\n") 
    pas1=input("enter your password :\n")
    if name != usnm :
        print("wrong username")
        count+=1
    elif pas1 != pas:
        print("wrong password")
        count+=1
    elif name != usnm and pas1 != pas:
       print("wrong username and password")
       count += 1
    else:
       while True:
          print("1.View Profile\n")
          print("2.Change Password\n")
          print("3.Logout\n")
          c1=int(input("enter your choice: \n"))
          if c1==1:
             print("Username: nasif")
          elif c1==2:
             count1=0
             while True:
                pascng=input("enter your old password")
                if pascng==pas:
                   newpas=input("enter your new password")
                   while newpas == pas:
                      print("new password cant be the same as old")
                   pas=newpas
                   print("password changed successfully")
                else:
                   print("invalid password")
                   count+=1
                   if count==3:
                      print("maximum limit reached")
                      break
         
          elif c1==3:
             print("logged out")
             break
               
                                   

  print("account locked")  
       
       
elif c =="n":
  print("Goodbye")
else :
   print("invalid choice")