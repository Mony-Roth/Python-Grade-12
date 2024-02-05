# file name quiz_app.py
name = input("what is your name? ")
print("Hello", name )
question = input("2+2? ")

Total_point = 0
if question == "4":
    Total_point = Total_point + 1
    print('Correct') 
else:
    print('Incorrect')


question = input("5-2? ")

if question == "3":
    Total_point = Total_point + 1
    print('Correct')
else:
    print('Incorrect')


question = input("2*3? ")

if question == "6":
    Total_point = Total_point + 1
    print('Correct')
else:
    print('Incorrect')


question = input("8/2? ")


if question == "4":
    Total_point = Total_point + 1
    print('Correct')
else:
    print('Incorrect')


question = input("10+10? ")


if question == "20":
    Total_point = Total_point + 1
    print('Correct')
else:
    print('Incorrect')
    
print((Total_point/5*100))
print(int(Total_point/5*100))
print(f"Your total point is: {int(Total_point/5*100)}%")
question = input("what is this? ")
if question.lower() == "book":
    Total_point = Total_point + 1
    print('Correct')
else:
    print('Incorrect')