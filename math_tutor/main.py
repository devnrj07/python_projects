from random import randrange
from time import time as t 
question_count = int(input('Enter the number of questions'))
max_number = int(input('Enter the max range'))
score = 0
answer_list = []
start = t()
for n in range(question_count):
    rand_a, rand_b = int(randrange(2,max_number+1)), int(randrange(2,max_number+1))
    answer = rand_a * rand_b
    
    user_answer = int(input(f'What is {rand_a} * {rand_b} = '))
    answer_list.append(f'{n}. for {rand_a} * {rand_b} you answered {user_answer}, the correct answer {answer}')
    if user_answer == answer:
        score+=1
end = t()
correct_ans = score/question_count
correct_perc = correct_ans * 100
print(f'Thank you for playing Math tutor')
print(f'You got {score} answers correct out of {question_count} questions with {round(correct_perc,1)} % accuracy')
print(f'you took {round(end-start,1)} sec to answer all the questions') 

for item in answer_list:
    print(item)
