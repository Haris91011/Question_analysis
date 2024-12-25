# Define the JSON content as a Python dictionary
data = {
    "Communication Skills": [
        "How would you explain your current role to someone who has no technical knowledge of your field?",
        "Can you introduce yourself in a concise and engaging manner?",
        "Give an example of when you had to actively listen to understand a teammate's perspective.",
        "How do you handle misunderstandings in team discussions?",
        "What strategies do you use to communicate effectively during meetings?",
        "What steps do you take to ensure clear communication when working in a team?",
        "How do you make sure your ideas are understood in a brainstorming session?",
        "What steps do you take to avoid miscommunication in a team project?",
        "How would you convey a delay in a project deadline to your manager?",
        "If you had to explain a complex idea to someone with little background in the subject. How did you approach it",
        "How will you handle situations where language barriers exist in a multicultural team?",
        "If I asked you to describe your favorite hobby in just three sentences, how would you do it?",
        "How do you ensure your audience understands your presentation?",
        "Describe how you adapt your communication style for different audiences.",
        "What do you believe is the most important aspect of clear communication?",
        "What role does non-verbal communication play in your interactions?",
        "How do you manage communication when working under tight deadlines?",
        "What do you do when a teammate misunderstands your instructions?",
        "How do you handle situations where a coworker is not responsive?",
        "If you were tasked with writing an email to a client about a project delay, what key points would you include?",
        "Describe a time when you successfully persuaded a team to adopt your idea.",
        "How do you balance assertiveness and politeness in professional conversations?",
        "How you convinced someone to adopt your idea or suggestion?",
        "What strategies do you use to communicate effectively when trying to resolve a conflict?",
        "How do you provide constructive feedback to a team member without demotivating them?",
        "What’s your approach to receiving and responding to criticism about your work?",
        "Imagine a team member missed a deadline, causing delays. How would you address the situation through text communication?",
        "You notice that a team discussion in a group chat is becoming unproductive. How would you steer it back on track?"
    ],
    "Problem Solving and Critical Thinking": [
        "Can you describe a challenging problem you solved during a project?",
        "Can you describe your usual process for solving a complex problem?",
        "What steps do you take to break down complex problems into manageable tasks?",
        "When faced with an unfamiliar challenge, how do you begin tackling it?",
        "What do you do when you encounter a problem that doesn’t have an obvious solution?",
        "What methods do you use to evaluate multiple solutions to a problem?",
        "Can you give an example of when you solved a problem creatively?",
        "How do you prioritize tasks when faced with multiple issues simultaneously?",
        "What tools or frameworks do you rely on for problem-solving in software development?",
        "Describe a time when you had to solve a problem without complete information.",
        "How do you handle uncertainty or ambiguity in problem-solving?",
        "How do you ensure you validate the effectiveness of your solution?",
        "Tell us about a time you made a mistake while solving a problem and what you learned.",
        "What role does collaboration play in your problem-solving approach?",
        "How do you approach problems that require learning new skills or technologies?",
        "How do you decide when to escalate a problem to your manager?",
        "What techniques do you use to remain calm and focused during troubleshooting?",
        "How do you ensure that your solution aligns with business goals?",
        "Can you describe a time when you solved a problem under a tight deadline?",
        "What do you do when your initial solution doesn’t work?",
        "How do you balance analytical thinking and intuition in decision-making?",
        "Imagine you’re working on a project, and you’re suddenly assigned additional responsibilities that will delay your work. How would you handle this?",
        "Your team disagrees on the best approach to solve a critical issue. How would you mediate and arrive at a solution?",
        "If your project was running behind schedule, what steps would you take to get it back on track?",
        "How do you prioritize tasks when you’re faced with multiple deadlines?",
        "You’ve been given a limited budget to solve a significant problem. How would you ensure that you use resources efficiently?"
    ]
}

# Define the function to retrieve questions
def get_questions(stage):
    # Retrieve questions for the given stage
    return data.get(stage, [])

# # Example usage
# if __name__ == "__main__":
#     stage = "Communication Skills"
#     questions = get_questions(stage)
#     for question in questions:
#         print(question)




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


# import json 

# def get_questions(stage):
    
#     with open(r"data\questions.json", "r") as file:
#         data = json.load(file)

#     return data[stage]

