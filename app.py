import streamlit as st

from multimodal.ocr import extract_text_from_image
from multimodal.speech_to_text import transcribe_audio

from agents.parser_agent import parse_problem
from agents.solver_agent import solve_problem
from agents.verifier_agent import verify_solution
from agents.explainer_agent import explain_solution

from rag.retriever import retrieve_context


st.title("🧠 Multimodal Math Mentor")

mode = st.selectbox(
    "Choose Input Mode",
    ["Text", "Image", "Audio"]
)

question = ""


# TEXT INPUT
if mode == "Text":
    question = st.text_area("Enter your math question")


# IMAGE INPUT
if mode == "Image":

    image = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

    if image:
        question = extract_text_from_image(image)
        st.write("Extracted Text:", question)


# AUDIO INPUT
if mode == "Audio":

    audio = st.file_uploader("Upload Audio", type=["wav", "mp3"])

    if audio:
        question = transcribe_audio(audio)
        st.write("Transcript:", question)


# SOLVE BUTTON
if st.button("Solve"):

    if question == "":
        st.warning("Please enter a question first")
    else:

        st.subheader("Question")
        st.write(question)

        # --------------------
        # Parser Agent
        # --------------------
        parsed_problem = parse_problem(question)
        st.subheader("Parsed Problem")
        st.write(parsed_problem)

        # --------------------
        # Retrieve Context
        # --------------------
        context = retrieve_context(question)

        st.subheader("Retrieved Context")

        for doc in context:
            st.write(doc.page_content)

        # --------------------
        # Solver Agent
        # --------------------
        solution = solve_problem(question, context)

        st.subheader("Final Answer")
        st.write(solution)

        # --------------------
        # Verifier
        # --------------------
        verification = verify_solution(question, solution)

        st.subheader("Confidence")
        st.write(verification)

        # --------------------
        # Explanation
        # --------------------
        explanation = explain_solution(question, solution)

        st.subheader("Step-by-Step Explanation")
        st.write(explanation)