import streamlit as st
from utils.pdf_reader import extract_text
from utils.gemini import generate_questions

# ---------------- Page Configuration ---------------- #

st.set_page_config(
    page_title="AI Interview Copilot",
    page_icon="🎯",
    layout="wide"
)

# ---------------- Session State ---------------- #

if "questions" not in st.session_state:
    st.session_state.questions = []

if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "answers" not in st.session_state:
    st.session_state.answers = []

if "scores" not in st.session_state:
    st.session_state.scores = []

if "feedback" not in st.session_state:
    st.session_state.feedback = []

# ---------------- Title ---------------- #

st.title("🎯 AI Interview Copilot")

st.write("Prepare for interviews with AI-powered personalized questions.")

st.divider()

# ---------------- Resume Upload ---------------- #

resume = st.file_uploader(
    "📄 Upload Your Resume (PDF)",
    type=["pdf"]
)

resume_text = ""

if resume is not None:

    resume_text = extract_text(resume)

    st.subheader("📄 Extracted Resume Text")

    st.text_area(
        "Resume Content",
        resume_text,
        height=300
    )

# ---------------- Job Role ---------------- #

job_role = st.selectbox(
    "💼 Select Job Role",
    [
        "AI Engineer",
        "Machine Learning Engineer",
        "Data Scientist",
        "Python Developer",
        "Software Engineer"
    ]
)

# ---------------- Experience ---------------- #

experience = st.slider(
    "📈 Years of Experience",
    0,
    10,
    0
)

# ---------------- Generate Questions ---------------- #

if st.button("🚀 Start Interview"):

    if resume is None:
        st.error("Please upload your resume first.")

    else:

        with st.spinner("Generating interview questions..."):

            questions = generate_questions(
                resume_text,
                job_role,
                experience
            )

        # Store questions in session state
        st.session_state.questions = [
            q.strip()
            for q in questions.split("\n")
            if q.strip()
        ]

        st.session_state.current_question = 0

        st.success("Interview Started!")

# ---------------- Show Current Question ---------------- #

if len(st.session_state.questions) > 0:

    st.divider()

    index = st.session_state.current_question

    if index < len(st.session_state.questions):

        st.subheader(f"Question {index + 1}")

        st.info(st.session_state.questions[index])

        answer = st.text_area(
            "✍️ Your Answer",
            key=f"answer_{index}"
        )