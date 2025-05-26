questions=[
    {
        "prompt":"What is 2+2?",
        "Options":["A. 3","B. 4","C. 5","D. 6"],
        "Answer":"B"
    },
    {
        "prompt":"What is 2+3?",
        "Options":["A. 3","B. 4","C. 5","D. 6"],
        "Answer":"C"
    },
    {
        "prompt":"What is 2+4?",
        "Options":["A. 3","B. 4","C. 5","D. 6"],
        "Answer":"D"
    },
    {
        "prompt":"What is 2+1?",
        "Options":["A. 3","B. 4","C. 5","D. 6"],
        "Answer":"A"
    }
]
def game(questions):
    score=0
    for question in questions:
        print(question["prompt"])
        for option in question["Options"]:
            print(option)
        answer=input("Enter your answer(A,B,C, or D): ").upper()
        if(answer==question["Answer"]):
            score=score+1
            print("Correct Answer!!")
        else:
            print("Wrong Answer..The correct answer was ",question["Answer"])
    print("GAME OVER")
    print("You got ",score," out of ", len(questions)," questions correct.")
game(questions)

