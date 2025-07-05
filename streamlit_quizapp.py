import streamlit as st

# Social Eagle + AI Quiz Data
questions = [
    {
        "question": "What type of services does Social Eagle primarily offer?",
        "options": [
            "Digital Marketing and AI Tools",
            "Real Estate Sales",
            "Food Delivery",
            "Construction Materials"
        ],
        "answer": "Digital Marketing and AI Tools"
    },
    {
        "question": "Which platform does Social Eagle often use to run digital ad campaigns?",
        "options": [
            "Meta (Facebook/Instagram)",
            "Snapchat",
            "TikTok",
            "Reddit"
        ],
        "answer": "Meta (Facebook/Instagram)"
    },
    {
        "question": "What is a key goal for clients working with Social Eagle?",
        "options": [
            "Generating more leads and sales",
            "Buying office furniture",
            "Hosting cooking shows",
            "Opening physical retail stores"
        ],
        "answer": "Generating more leads and sales"
    },
    {
        "question": "Which of these is an example of Artificial Intelligence?",
        "options": [
            "A spreadsheet calculating sums",
            "A microwave heating food",
            "A chatbot answering questions",
            "A bicycle moving forward"
        ],
        "answer": "A chatbot answering questions"
    },
    {
        "question": "What technology is commonly used to train AI models to understand language?",
        "options": [
            "Blockchain",
            "Natural Language Processing (NLP)",
            "GPS Navigation",
            "3D Printing"
        ],
        "answer": "Natural Language Processing (NLP)"
    }
]

st.title("🦅 Social Eagle + AI Quiz")

# Store user answers
user_answers = []

# Display each question
for idx, q in enumerate(questions):
    st.write(f"**Q{idx+1}. {q['question']}**")
    choice = st.radio(
        "Select an answer:",
        q["options"],
        key=f"question_{idx}"
    )
    user_answers.append(choice)
    st.write("---")

# Submit button
if st.button("Submit Quiz"):
    score = 0
    for i in range(len(questions)):
        if user_answers[i] == questions[i]["answer"]:
            score += 1
    st.success(f"✅ You scored {score} out of {len(questions)}!")

    # Optionally, show correct answers
    st.subheader("Correct Answers:")
    for i, q in enumerate(questions):
        st.write(f"**Q{i+1}: {q['answer']}**")
