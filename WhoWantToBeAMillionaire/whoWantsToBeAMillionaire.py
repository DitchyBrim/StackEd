import random
input("Who wants to be a Millionaire?")
input("The topic for today is.")
input("All about Software Engineering.")
input("For the first level. We will be choosing fun facts relating to software Engineering.")
choice_lifeline =[]
use_lifeline = False
correct_answer = 0
# choice_lifeline =[]
# user_input= 9
# def lifeline(input_list):
#     # random()
#     answer = input_list[-1]
#     for i in range(2):
#         to_remove = random.choice(input_list)
#         if to_remove != answer:
#             input_list.remove(to_remove)
#     choice_lifeline = input_list
#     use_lifeline = True
# def show_questions(quest, choicesList):
#     print(quest)
#     for i in range(len(choicesList)-1):
#         print(f"{i+1}:) {choicesList[i]}")
#     user_input = input()
fun_facts = {"Who is the first computer programmer?":["Ada Lovelace", "Alan Turing","Charles Babbage","Bill Gates",1], "What year was the first game created?":[1960, 1958, 1990, 1991, 2], "It was found out that a huge percentage of programmers are non degree holders in computer related courses\n Choose what range are the non degree holders part of":["65-75%","55-64%","76-85%","86-95%", 1],"What is the first HIGH-level programming language used?":["python","Java","FORTRAN","ALGOL", 3],"What year was the first virus created?":[1980, 1983, 2004, 2000, 2]}

second_level = {"What operator is used to result True, if two statements are True?":["or","not","both","and", 4],"What operator is used to result True, if at least one of the statements is True?":["or","not","both","and",1],"What loop is used to repeatedly execute over a block of code as long as the condition is True?":["do while loop","while loop","for loop","for while loop", 2],"What control statements in python will skip the statements which are present after this statement and proceed with the next iterations?":["continue","break","pass","skip", 1],"What loops can be used to access items of lists which are inside other lists?":["for loop","all loop","nested loop","while loop", 3]}

third_level= {"What variable is used for numbers with decimal places?":["Integer","Float","String","Decimal",2],"The value '1+2j' is what type of variable?":["Number", "Complex Number","List","Float", 2],"What data type are an ordered sequence of items that are immutable?":["List","Array","Tuple","Dictionary", 3],"This type of variable is a sequence of Unicode characters.":["Characters","Sequence","String","List", 3],"This is an unordered collecton of key-value pairs.":["List", "Tuples", "Array", "Dictionary",4]}

wrong_input = ["Incorrect","Sadly","You got it wrong"]
correct_input =["You got it right!","CORRECT!","Amazing!"]
sample_dict = {"first list":["0","1","2"],"second":["3","5","4"]}
question = ""
prices = {0:"Zero Dollars, NOTHING.",1:"$1000",2:"$10,000",3:"$25,000",4:"$40,000",5:"50,000",6:"80,000",7:"100,000",8:"250,000",9:"350,000",10:"500,000",11:"650,000",12:"700,000",13:"750,000",14:"900,000",15:"1,000,000"}
price_key = 0
choices = []
quest_list = [fun_facts,second_level,third_level]
incorrect = False
for a in quest_list:
    for x,y in a.items():
        question = x
        choices = y
        correct_answer = choices[-1]
        user_input=""
        while user_input=="":
            print(x)
            for i in range(len(choices)-1):
                print(f"{i+1}:) {choices[i]}")
            user_input = input()

        user_input=int(user_input)

        if user_input == correct_answer:
            input(random.choice(correct_input))
            input("Next Question!")
            price_key+=1
        # elif user_input == 5:
        #     lifeline(choices)
        else:
            input(random.choice(wrong_input))
            input(f"The correct answer is {choices[choices[4]-1]}")
            incorrect = True
            break
    input()
    if incorrect==True:
        break

print(f"You got {price_key} question/s answered correctly.\nYou won a total of {prices[price_key]}")
