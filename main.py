import streamlit as st
import base64
from utils.retreive_questions import retrieve_question
from utils.response_evaluation import get_evaluation_score

# Function to fetch questions from the API
def fetch_questions(stage):

    return retrieve_question(stage)

# Function to send responses to the API
def send_responses(stage, questions, answers):
    score=get_evaluation_score(questions,answers)
        
    st.write(score)
    return [True,score]

# Define stages
question_stages = [
    "Communication-Skills",
    "Adaptability-Skills",
    "Critical-Thinking-Skills",
    "Culture-Skills",
    "Learning-Mindset-Skills",
    "Time-Management-Skills",
    "Integrity-Skills",
]

response_stages = [
    "Communication-Response",
    "Adaptability-Response",
    "Critical-Thinking-Response",
    "Culture-Response",
    "Learning-Mindset-Response",
    "Time-Management-Response",
    "Integrity-Response",
]

# Function to convert the image to a base64 string
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Path to your logo
logo_path = "jinalyst.jpg"  # Replace with the actual path to your logo

# Convert the logo image to base64
try:
    logo_base64 = get_base64_image(logo_path)
except FileNotFoundError:
    st.error("Logo file not found. Please check the file path.")
    st.stop()

# Define HTML and CSS for the logo
logo_html = f"""
<div style="
    position: fixed;
    top: 60px;
    left: 10px;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    overflow: hidden;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    z-index: 1000;">
    <img src="data:image/png;base64,{logo_base64}" 
         alt="Logo" style="width: 100%; height: 100%; object-fit: cover;">
</div>
"""

# Render the logo at the top-left corner
st.markdown(logo_html, unsafe_allow_html=True)

# Streamlit app
st.title("AI-Based Recruitment System")

if "stage_index" not in st.session_state:
    st.session_state.stage_index = -1  # Start with the greeting message

if "questions" not in st.session_state:
    st.session_state.questions = {}

if "answers" not in st.session_state:
    st.session_state.answers = {}

if "scores" not in st.session_state:
    st.session_state.scores = []  # Initialize an empty list to store score

if st.session_state.stage_index == -1:
    st.subheader("Hi Sam, Welcome on board!")
    st.write("I am your recruitment system. I will guide you through your assessment.")
    st.write("Your abilities will be evaluated through the following stages:")
    st.write("1. Communication Skills")
    st.write("2. Problem Solving and Critical Thinking")
    st.write("3. Adaptability and Flexibility")
    st.write("4. Cultural Fit and Emotional Fit")
    st.write("5. Learning and Growth Mindset")
    st.write("6. Time Management")
    st.write("7. Integrity and Professionalism")
    st.write("Are you ready to begin?")
    if st.button("Start Assessment"):
        st.session_state.stage_index = 0
else:
    # Get the current stage
    stage_index = st.session_state.stage_index
    if stage_index < len(question_stages):
        current_stage_question = question_stages[stage_index]
        current_stage_response = response_stages[stage_index]
        st.subheader(f"Stage {stage_index + 1}: {current_stage_question.replace('-', ' ')}")

        # Fetch questions for the current stage only if not already fetched
        if current_stage_question not in st.session_state.questions:
            questions = fetch_questions(current_stage_question)
            st.session_state.questions[current_stage_question] = questions
        else:
            questions = st.session_state.questions[current_stage_question]

        if questions:
            answers = []
            for i, question in enumerate(questions):
                if f"answer_{i}" not in st.session_state.answers:
                    st.session_state.answers[f"answer_{i}"] = ""  # Initialize with an empty string
                
                st.write(f"Q{i + 1}: {question}")
                answer = st.text_input(
                    f"Your Answer for Q{i + 1}", 
                    value=st.session_state.answers[f"answer_{i}"], 
                    key=f"answer_{i}"
                )
                st.session_state.answers[f"answer_{i}"] = answer
                answers.append(answer)

            if st.button("Submit Answers"):
                evaluation_result = send_responses(current_stage_response, questions, answers)

                if evaluation_result[0]:
                    st.success("Congratulations! You have successfully completed the stage.")
                    
                    st.session_state.scores.append(evaluation_result[1])
                    
                    st.session_state.stage_index += 1  # Move to the next stage

                    # Clear the text input fields by resetting their keys
                    for i in range(len(questions)):
                        st.session_state.answers[f"answer_{i}"] = ""


                if st.button("Next Stage"):
                    # Re-enable the submit button for the next stage
                    st.session_state.submit_disabled = False  # Enable submit button again
                
                # Disable the submit button after completion
                st.session_state.submit_disabled = True

    else:
        st.subheader("Assessment Completed")
       
        # Calculate the average score
        total_score = sum(st.session_state.scores)
        average_score = total_score / len(st.session_state.scores)
        
        st.write(f"Thank you for completing the assessment. Your average score is: {average_score:.2f}/10. We will review your responses and get back to you.")
