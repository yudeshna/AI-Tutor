# AI Tutor – Personal AI & ML Learning Assistant

AI Tutor is a Streamlit-based chatbot that teaches Artificial Intelligence concepts in a structured way.

## Features

- Beginner / Intermediate / Advanced mode
- Structured explanation format:
  - Simple Explanation
  - Real-world Example
  - Mathematical Explanation
  - Quiz Questions
  - Suggested Next Topic
- Conversation memory
- Powered by OpenRouter API
- Uses Claude Sonnet 4.6 model

## Tech Stack

- Python
- Streamlit
- OpenRouter API
- GitHub

## How to Run Locally

1. Clone the repository
2. Create virtual environment
3. Install dependencies:
   pip install -r requirements.txt
4. Set environment variable:
   setx OPENROUTER_API_KEY "your_key"
5. Run:
   streamlit run app.py

## Future Improvements

- RAG (PDF upload)
- Learning progress tracker
- Deployment on Streamlit Cloud