import random


def insert_phrase(input_phrase):
    phrase = input_phrase
    ball_list.append(phrase)


def append_question(input_question):
    Q = input_question
    questions.append(Q)


ball_list = ['Outlook is good', 'ask again later', 'yes', 'no', 'most likely no', 'most likely yes',
             'outlook is not good']
questions = []
repeat = 'yes'
while repeat == 'yes':
    input_question = input("What would you like to ask the 8 ball: ")
    print(random.choice(ball_list))
    repeat = input('do you want to ask another question?: ')
    add_questions = input('Do you want to add phrase to the magic 8 ball: ')
    if repeat == 'no':
        continue
    if repeat == 'yes':
        input_question = input("What would you like to ask the 8 ball: ")
        append_question(input_question)
        print(random.choice(ball_list))
    if add_questions == 'yes':
        phrase = input("Input a phrase: ")
        insert_phrase(phrase)


