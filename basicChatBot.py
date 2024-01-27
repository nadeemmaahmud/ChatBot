greetWords = ['hi', 'hello', 'hola']
badWords = ['dog', 'pocha', 'bal']

def listen():
    return input("Say something : ")

def decide(command):
    command = command.lower()
    brokenWords = command.split()

    for word in brokenWords:
        if word in greetWords:
            print(word.capitalize(), "Human! How can I serve you today?")
            break
        elif word in badWords:
            print("Your mom is a", word.capitalize())
            break

def talkback():
    pass

command = listen()
decide(command)