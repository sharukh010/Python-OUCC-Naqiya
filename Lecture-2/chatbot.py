question1 = "how do plants stay alive?"
answer1 = "they need several things, including water, soil and sunlight.they need sunlight because they need to create food for themselves. this process is called photosynthesis."

question2 = "question2"
question3 = "question3"
question4 = "question4"
question5 = "question5"

answer2 = "answer2"
answer3 = "answer3"
answer4 = "answer4"
answer5 = "answer5"

prompt = input("Prompt: ")

if prompt.casefold() == question1.casefold(): 
    print(f"Response: {answer1}")
elif prompt.casefold() == question2.casefold(): 
    print(f"Response: {answer2}")
elif prompt.casefold() == question3.casefold(): 
    print(f"Response: {answer3}")
elif prompt.casefold() == question4.casefold(): 
    print(f"Response: {answer4}")
elif prompt.casefold() == question5.casefold(): 
    print(f"Response: {answer5}")
else: 
    print("Sorry, couldn't answer this question.")