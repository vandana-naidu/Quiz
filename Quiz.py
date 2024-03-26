def a(i, ans, count=0):
    if i == "1)Who is the father of computer" and ans == "b":
        print("correct.., :)")
        count = count + 1
    elif i == "2)What does CPU stands for" and ans == "a":
        print("correct.., :)")
        count = count + 1
    elif i == "3)heart of computer" and ans == "c":
        print("correct.., :)")
        count = count + 1
    elif i == "4)How many stripes are there on US flag" and ans == "c":
        print("correct.., :)")
        count = count + 1
    elif i == "5)What is the national animal of Australia" and ans == "c":
        print("correct.., :)")
        count = count + 1
    elif i == "6)What country has the most islands in the world" and ans == "b":
        print("correct.., :)")
        count = count + 1
    elif i == "7)Where is Bellie Eilish from?" and ans == "a":
        print("correct.., :)")
        count = count + 1
    elif i == "8)When was Netflix found" and ans == "a":
        print("correct.., :)")
        count = count + 1
    elif i == "9)What was the name of the coffee shop in the sitcom friends" and ans == "d":
        print("correct.., :)")
        count = count + 1
    elif i == "10)Name the Disney's first film" and ans == "a":
        print("correct.., :)")
        count = count + 1
    else:
        print("oops.., wrong :(")
    return count


def quiz(questions):
    d = 0
    for i in questions:
        print(i)
        print(questions[i])
        ans = input().lower()
        if ans in ["a", "b", "c", "d"]:
            c = a(i, ans)
            d += c

        else:
            print("please enter either a/b/c/d")
            print(i)
            print(questions[i])
            ans = input().lower()
            c = a(i, ans)
            d += c
    return d


if __name__ == "__main__":
    questions = {"1)Who is the father of computer": "a)Euclid b)Charles c)Einstein d)Nelson",
                 "2)What does CPU stands for": "a)control processing unit b)central program unit c)control perform output d)cup",
                 "3)heart of computer": "a)monitor b)keyboard c)cpu d)mouse",
                 "4)How many stripes are there on US flag": "a)11 b)12 c)13 d)14",
                 "5)What is the national animal of Australia": "a)horse b)giraffe c)kangaroo d)rhinoceros",
                 "6)What country has the most islands in the world": "a)canada b)sweden c)rome d)egypt",
                 "7)Where is Bellie Eilish from?": "a)los angelas b)athens c)manchster d)USA",
                 "8)When was Netflix found": "a)1997 b)2001 c)2009 d)2015",
                 "9)What was the name of the coffee shop in the sitcom friends": "a)friends corner b)barista c)coffe shop d)central park",
                 "10)Name the Disney's first film": "a)snow white b)rapenzel c)miami d)umbrella"}
    instructions="""-->This game consists of 10 questions
-->you have to enter your option by either a/b/c/d for each question
-->for each correct question you will get 1 point
-->your final score will be displayed at the end"""
    print("Welcome to my Quiz game!")
    print(instructions)
    play = (input("""Do you want to play?
       a) YES b) NO
       Enter a/b
       """)).lower()
    while True:
        if play == "a":
            a = quiz(questions)
            print("************************************************")
            print("Game Ended!!")
            print("your total score is: ", a, "out of ", len(questions))
            break
        elif play == "b":
            print("Quiting..,")
            break
        else:
            play = input("please enter either a/b")




