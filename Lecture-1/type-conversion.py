"""
Type conversion / casting: 
It is the process of converting data from one data type to the 
other data time 
Note: the data should be compatable with the destination data time 
ex: "alex" -> int ? it is not possible 
    "10" -> int ? it is possible 
    "1.4" -> float ? it is possible 
"""
num1 = int("100")
num2 = float("1.34")
data = bool("True")
text = str(134)
print(type(num1))
print(type(num2))
print(type(data))
print(type(text))