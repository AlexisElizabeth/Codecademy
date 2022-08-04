#!/usr/bin/env python3
"""
Answers any question you need answered.
"""

import random


def main():
    name = "Alexis"
    question = "Will I learn Python?"
    answer = ""
    random_number = random.randint(1, 9)
    print(random_number)
    all_answers = {1: "Yes - definitely.",
                   2: "It is decidedly so.",
                   3: "Without a doubt.",
                   4: "Reply hazy, try again.",
                   5: "Ask again later.",
                   6: "Better not tell you now.",
                   7: "My sources say no.",
                   8: "Outlook not so good.",
                   9: "Very doubtful."}

    if random_number in all_answers:
        answer = all_answers[random_number]
    else:
        raise ValueError(f"Random number {random_number} wasn't anticipated "
                         "in the code. This is a bug.")

    if name == "":
        print("Question: " + question)
    else:
        print(name + " asks: " + question)
    
    if question == "":
        print("Please ask a question")
    else:
        print("Magic 8-Ball's answer: " + answer)

if __name__ == '__main__':
    main()
