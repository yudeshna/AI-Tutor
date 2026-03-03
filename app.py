import streamlit as st
from openai import OpenAI
import os

# -----------------------
# Page Config
# -----------------------
st.set_page_config(
    page_title="AI Tutor",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Tutor – Personal AI & ML Learning Assistant")

# -----------------------
# API Setup
# -----------------------
api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    st.error("OPENROUTER_API_KEY not found. Please set it in your environment.")
    st.stop()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

# -----------------------
# Sidebar Settings
# -----------------------
with st.sidebar:
    st.header("⚙️ Settings")

    level = st.selectbox(
        "Select Learning Level",
        ["Beginner", "Intermediate", "Advanced"]
    )

    temperature = st.slider(
        "Creativity Level",
        min_value=0.0,
        max_value=1.0,
        value=0.6,
        step=0.1
    )

    max_tokens = st.slider(
        "Max Response Length",
        min_value=300,
        max_value=1200,
        value=700,
        step=100
    )

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []

    st.markdown("---")
    st.caption("Model: Claude Sonnet 4.6")
    st.caption("Powered by OpenRouter")

# -----------------------
# Memory Initialization
# -----------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------
# Display Chat History
# -----------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -----------------------
# User Input
# -----------------------
user_input = st.chat_input("Enter AI topic...")

if user_input:

    system_prompt = f"""
You are a structured AI Professor teaching Artificial Intelligence.

Adapt explanation depth based on level:
- Beginner → Simple language, intuitive explanations, minimal math.
- Intermediate → Balanced explanation with formulas.
- Advanced → Deep technical reasoning with equations and detailed derivations.

Every response must strictly follow this format:

1. Simple Explanation
2. Real-world Example
3. Mathematical Explanation
4. 2 Quiz Questions
5. Suggested Next Topic

Maintain clarity, logical structure, and professional tone.
"""

    messages = [
        {"role": "system", "content": system_prompt}
    ] + st.session_state.messages + [
        {"role": "user", "content": user_input}
    ]

    # Show user message instantly
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate AI response
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="anthropic/claude-sonnet-4.6",
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
        )

        answer = response.choices[0].message.content

    # Show assistant message
    with st.chat_message("assistant"):
        st.markdown(answer)

    # Save to memory
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.messages.append({"role": "assistant", "content": answer})