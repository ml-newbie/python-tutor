# Python Tutor Chatbot

This is a simple chatbot app that will teach you Python concepts with examples. Will be hosted on Streamlit Cloud.

## Description

This chatbot uses the Python Tutor API to answer your Python programming questions.  It maintains a chat history to provide context for follow-up questions.

## Features

*   **Interactive Chat:** Ask Python questions and receive explanations.
*   **Chat History:**  The chatbot remembers previous questions and answers.
*   **Code Highlighting:**  Code blocks in the responses are displayed with syntax highlighting.
*   **User-Friendly Interface:** Built with Streamlit for a clean and easy-to-use experience.

## Getting Started

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/ml-newbie/python-tutor.git
    cd python-tutor
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the app:**

    ```bash
    streamlit run app.py
    ```

## Usage

1.  Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).
2.  Enter your Python question in the text area.
3.  Click the "💬 Ask Tutor" button.
4.  The chatbot will respond with an answer, potentially including code examples.

## GitHub Commands to Push Changes:

```bash
git init
git add .
git commit -m "Initial commit of resume analyzer app"
git remote add origin https://github.com/ml-newbie/python-tutor.git

Technologies Used
Python: Programming language.
Streamlit: Framework for building interactive web apps.
Python Tutor API: Provides access to the Python Tutor service for code execution and explanation.
Regular Expressions: Used for code block detection and rendering.
git branch -M main
git push -u origin main
# All future pushes can be done with: git push
