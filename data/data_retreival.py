import json 

def get_questions(stage):
    
    with open("data\questions.json", "r") as file:
        data = json.load(file)

    return data[stage]