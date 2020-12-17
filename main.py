import pyttsx3

engine = pyttsx3.init()


print("hey! smart person ")
engine.say(" ready to go ")
engine.runAndWait()

def quiz():
        count = 0
        print("1. Which is the correct operator for power(xy) ? \n a) X^y b) X**y c) X^^y d) None of the mentioned ")
        engine.say(" 1. Which is the correct operator for power(xy) ? ")
        engine.runAndWait()
        ans = input()
        if ans == "b":
            count = count + 1
        else:
            count = count + 0
        print("2. Which one of these is floor division? \n a) / b) // c) % d) None of the mentioned ")
        engine.say("2. Which one of these is floor division? ")
        engine.runAndWait()
        ans = input()
        if ans == "b":
            count = count + 1
        else:
            count = count + 0
        print("3. What is the answer to this expression, 22 % 3 is? \n a) 7 b) 1 c) 0 d) 5")
        engine.say("3. What is the answer to this expression, 22 % 3 is? ")
        engine.runAndWait()
        ans = input()
        if ans == "b":
            count = count + 1
        else:
            count = count + 0

        print("result : " + str(count))

        print("wanna play? y or n")
        ans1 = input()
        if ans1 == "y":
            quiz()
        else:
            print("bbyee")
res = input("y or n : ")
if(res == "y"):
    quiz()
else:
    print("okayyyy")
    engine.say(" your loss ")
    engine.runAndWait()
