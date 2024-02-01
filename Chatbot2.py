import datetime

bores = ['bored', 'boring', 'feeling bad', 'feeling not good']
times = ['time']

def listen():
    print("Type 'Exit' to terminate : ")
    i = input(">>")
    if(i == "exit" or i == "Exit"):
        print("Program Terminated!")
        return 0
    else:
        decide(i)

def decide(commands):
    commands = commands.split()
    for index,word in enumerate(commands):
        word = word.strip(",.!?").lower()
        if word in bores:
            talkback("bor")
        elif word in times:
            talkback("time")

def talkback(getdata):
    if(getdata == "bor"):
        print("Bot:  You can learn Javascript.")
        listen()
    elif(getdata == "time"):
        print("Bot: ", datetime.datetime.now())
        listen()
    else:
        print("Bot: Sorry! I didn't get it at all!")
        listen()

listen()