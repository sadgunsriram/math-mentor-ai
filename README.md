# AI Math Mentor

## Overview

AI Math Mentor is an AI-powered application that helps students solve math problems and understand the solution step-by-step.
The system can take **text or image inputs** and generate clear explanations using AI.

This project demonstrates concepts like **Retrieval Augmented Generation (RAG), multimodal inputs, and AI agents**.

---

## Features

* Solve math problems step-by-step
* Accept **text or image-based questions**
* AI-generated explanations for better understanding
* Simple **Streamlit UI** for interaction

---

## Tech Stack

* **Python**
* **Streamlit**
* **Ollama (Local LLM)**
* **FAISS (Vector Database)**
* **OpenCV & OCR** for image processing

---

## Why I Used Ollama

I used **Ollama** instead of OpenAI because I did not have access to an OpenAI API key.

Ollama allows running large language models **locally on the system**, which means:

* No API key is required
* No API usage cost
* The model can run **offline on the local machine**

This made it easier to develop and test the project without relying on external APIs.

---

## Installation

Clone the repository:

```
git clone https://github.com/sadgunsriram/math-mentor-ai.git
cd math-mentor-ai
```

Create virtual environment:

```
python -m venv venv
```

Activate environment:

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
streamlit run app.py
```

---

## Author

**Sriram Sadgun**
B.Tech – Computer Science (AI & ML)
