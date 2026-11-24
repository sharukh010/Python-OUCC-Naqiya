question1 = "how do plants stay alive?"
answer1 = "they need several things, including water, soil and sunlight.they need sunlight because they need to create food for themselves. this process is called photosynthesis."

question2 = "where was time discovered?"
question3 = "who discovered the laws of motion?"
question4 = "who were the 4 people who wanted the english thone after edward the confesser died?"
question5 = "what is 7x2?"

answer2 = "time was discovered in greenwhich, london"
answer3 = "Sir isaac newton. he also discovered that white light can be split into many different colours "
answer4 = "the 4 people were William, duke of normandy, Harald hadraga, king of the vikings, Harold godwinson< the late kings chancellor, and edgar athling, the late kings great nephew."
answer5 = "the answer is 14"

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