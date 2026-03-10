import streamlit as st

from multimodal.ocr import extract_text_from_image
from multimodal.speech_to_text import transcribe_audio

from agents.parser_agent import parse_problem
from agents.solver_agent import solve_problem
from agents.verifier_agent import verify_solution
from agents.explainer_agent import explain_solution

from rag.retriever import retrieve_context


st.title("Multimodal Math Mentor")

mode = st.radio("Choose Input Mode", ["Text", "Image", "Audio"])

# debug option (for developers)
debug = st.sidebar.checkbox("Show AI Debug Info")

question = ""



# TEXT INPUT

if mode == "Text":

    question = st.text_area("Enter your math question")



# IMAGE INPUT

elif mode == "Image":

    image = st.file_uploader("Upload image", type=["png", "jpg", "jpeg"])

    if image is not None:

        st.image(image, caption="Uploaded Image", width="stretch")

        extracted = extract_text_from_image(image)

        st.subheader("Extracted Text")

        # Human-in-the-loop correction
        question = st.text_area(
            "Edit the extracted question if OCR is incorrect",
            value=extracted
        )



# AUDIO INPUT

elif mode == "Audio":

    audio = st.file_uploader("Upload Audio", type=["wav", "mp3"])

    if audio is not None:

        transcript = transcribe_audio(audio)

        st.subheader("Transcript")

        question = st.text_area(
            "Edit the transcript if needed",
            value=transcript
        )



# SOLVE BUTTON

if st.button("Solve"):

    if question.strip() == "":
        st.warning("Please enter a question first")

    else:

        st.subheader("Question")
        st.write(question)

        
        # Parser Agent
        
        parsed_problem = parse_problem(question)

        if debug:
            st.subheader("Parsed Problem")
            st.write(parsed_problem)

        
        # Retrieve Context
        
        context = retrieve_context(question)

        if debug:
            st.subheader("Retrieved Context")

            for doc in context:
                st.write(doc.page_content)

        
        # Solver Agent
        
        solution = solve_problem(question, context)

        st.subheader("Final Answer")
        st.write(solution)

       
        # Verifier
        
        verification = verify_solution(question, solution)

        if debug:
            st.subheader("Confidence")
            st.write(verification)

        # Explanation
        
        explanation = explain_solution(question, solution)

        st.subheader("Step-by-Step Explanation")
        st.write(explanation)