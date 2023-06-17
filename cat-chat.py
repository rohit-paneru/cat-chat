required="ok meow"
import random

print("WELCOME TO MEOWW MEOWW CHAT🐱\n")
print("YOU CAN ASK ANYTHING 🐾")
print("TO EXIT FROM CHAT JUST TYPE 'ok meow'")
print("MEOW CAN I HELP YOU ^..^")
while True:
   
    i=str(input("\n🐱🫴"))
   
    

    if i==required:
        break
    elif i=="hi":
        print("meow meow")
    elif i=="woof" or i== "i dont like you" or i== "you are stinky" or i=="thats rude":
        print("ANGRILY MEOWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
    elif i=="sorry":
        print("meow😻")
    else:
        #a=len(i)
    
        print(random.randint(1,50)* " meowww")
