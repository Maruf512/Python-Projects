import datetime
def gettime():
    return datetime.datetime.now()
import time
x = int(input("Press 1 for lock the value and 2 for retrieve "))

if x==1:
    a = int(input("Press 1 for exercise and 2 for food "))
    if (a==1):
        b = int(input("Press 1 for(Anik) 2 for(Maruf) 3 for(Sami) "))
        if (b==1):
            value = input("Type Hear \n")
            with open("Anik--Exercise.txt", "a") as f:
                f.write(str([str(gettime())])+" : " +value+"\n")
                print("Successfully written.")
                time.sleep(10)
        elif (b==2):
            value = input("Type Hear \n")
            with open("Maruf--Exercise.txt", "a") as f:
                f.write(str([str(gettime())])+" : " +value+"\n")
                print("Successfully written.")
                time.sleep(10)
        elif (b==3):
            value = input("Type Hear \n")
            with open("Sami--Exercise.txt", "a") as f:
                f.write(str([str(gettime())])+" : " +value+"\n")
                print("Successfully written.")
                time.sleep(10)
        else:
            print("plz enter valid input (1(Anik),2(Maruf),3(Sami)")
            time.sleep(10)
    elif (a==2):
        b = int(input("Press 1 for Anik 2 for Maruf 3 for Sami "))
        if (b==1):
            value = input("Type Hear \n")
            with open("Anik--Food.txt", "a") as f:
                f.write(str([str(gettime())])+" : " +value+"\n")
                print("Successfully written.")
                time.sleep(10)
        elif (b==2):
            value = input("Type Hear \n")
            with open("Maruf--Food.txt", "a") as f:
                f.write(str([str(gettime())])+" : " +value+"\n")
                print("Successfully written.")
                time.sleep(10)
        elif (b==3):
            value = input("Type Hear \n")
            with open("Sami--Food.txt", "a") as f:
                f.write(str([str(gettime())])+" : " +value+"\n")
                print("Successfully written.")
                time.sleep(10)
        else:
            print("plz enter valid input (1(Anik),2(Maruf),3(Sami)")
            time.sleep(10)
elif x==2:
    d = int(input("Enter 1 for exercise and 2 for food "))
    if d==1:
        e = int(input("Whitch one do you want to see?\n Enter 1 for Anik 2 for Maruf 3 for Sami "))

        if e==1:
            with open("Anik--Exercise.txt") as f:
                for i in f:
                    print(i, end="")
                    time.sleep(10)

        elif e==2:
            with open("Maruf--Exercise.txt") as f:
                for i in f:
                    print(i, end="")
                    time.sleep(10)

        elif e==3:
            with open("Sami--Exercise.txt") as f:
                for i in f:
                    print(i, end="")
                    time.sleep(10)

        else:
            print("plz enter valid input (1(Anik),2(Maruf),3(Sami)")
            time.sleep(10)
    elif d==2:
        g = int(input("Whitch one do you want to see?\n Enter 1 for Anik 2 for Maruf 3 for Sami "))
        if g==1:
            with open("Anik--Food.txt") as  h:
                for j in  h:
                    print(j, end="")
                    time.sleep(10)

        elif g==2:
            with open("Maruf--Food.txt") as  h:
                for j in  h:
                    print(j, end="")
                    time.sleep(10)

        elif g==3:
            with open("Sami--Food.txt") as  h:
                for j in  h:
                    print(j, end="")
                    time.sleep(10)


        else:
            print("plz enter valid input (1(Anik),2(Maruf),3(Sami)")
            time.sleep(10)

