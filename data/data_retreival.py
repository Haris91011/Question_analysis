# import json
# import os

# def get_questions(stage):
#     # Get the absolute path to ensure compatibility
#     base_path = os.path.dirname(os.path.abspath(__file__))
#     file_path = os.path.join(base_path, "data", "questions.json")

#     # Read the JSON file
#     with open(file_path, "r", encoding="utf-8") as file:
#         print("File path:", file_path)
#         data = json.load(file)

#     return data[stage]


import json 

def get_questions(stage):
    
    with open(r"data\questions.json", "r") as file:
        data = json.load(file)

    return data[stage]
