import time

tym= int(input("enter the amouont of time in seconds \n "))

for tym in range(tym,0,-1):
    seconds= tym%60
    minutes=int(tym/60)%60
    hours=int(tym/3600)

    print(f"{hours:02}:{minutes:02}:{seconds:02}",end="\r")

    time.sleep(1)
 