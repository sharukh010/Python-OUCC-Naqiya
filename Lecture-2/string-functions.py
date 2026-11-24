# name = "NAQIYA"

# # lower -> convert the string into lower case 
# print(name.lower())

# upper -> convert the string into upper case 
# print("naqiya".upper())

# title -> converts every word's starting character to upper case 
# ex: harry potter -> Harry Potter 
# print("harry potter".title())


#capitalize -> converts starting character of a string into upper case 
#ex: harry potter -> Harry potter 
# print("harry potter".capitalize())

# print("naqiya".casefold())

word1 = "Harry POTTER"
word2 = "HARRY POTTER"
# print(word1.casefold() == word2.casefold())

# word1 = word1.casefold()
# word2 = word2.casefold()

# print(word1,word2)

sentence = "sun rises in the west"
sentence = sentence.replace("west","east")
# print(sentence)


sentence = "       naqiya             "
sentence = sentence.strip()
# print(sentence)


# print("-".join(("a","b","c","d")))


# print("9".isdigit())
# print("9A".isalnum())
# print("naqiya".isalpha())
# print("naqiya last name".replace(" ",""))

print(len("naqiya"))