import random
x=0
amount=0
heads=0
tails=0
flip_result=[]
def flip():
    global x
    global amount
    global flip_result
    while x<amount:
        flips=random.randint(1,2)
        if flips== 1:
            flip_result.append("heads")
        else:
            flip_result.append("tails")
        x+=1
def coin_flip():
    global amount
    temp=input("how many times would you like to flip\n")
    amount=int(temp)
    print("you flip a coin\n")
    flip()
    print(flip_result)
def sort():
    global heads
    global tails
    flip_result.sort()
    for x in flip_result:
        if x == "heads":
            heads+=1
        elif x == "tails":
            tails+=1
    print(heads, "heads\n")
    print(tails, "tails\n")
coin_flip()
sort()
