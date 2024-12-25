from data.data_retreival import get_questions
import random

def retrieve_question(stage):

    if stage=="Adaptability-Skills":
        questions=get_questions("Adaptability and Flexibility")
    elif stage=="Communication-Skills":
        questions=get_questions("Communication Skills")
    elif stage=="Critical-Thinking-Skills":
        questions=get_questions("Problem Solving and Critical Thinking")
    elif stage=="Culture-Skills":
        questions=get_questions("Cultural Fit and Emotional Fit")
    elif stage=="Integrity-Skills":
        questions=get_questions("Integrity and Professionalism")
    elif stage=="Learning-Mindset-Skills":
        questions=get_questions("Learning and Growth Mindset")
    else:
        questions=get_questions("Time Management")

    random_questions = random.sample(range(len(questions)), 5)
        
    for index,value in enumerate(random_questions):
        random_questions[index]=questions[value]

    return random_questions