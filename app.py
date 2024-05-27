from langchain_community.llms import Ollama
import streamlit as st

# Initialize the LLAMA3 model
llm = Ollama(model="llama3")

# Set page configuration
st.set_page_config(
    page_title="Chatbot Landing Page",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Streamlit app title
st.title("Chatbot Built Using LLAMA3")

# Text area for user input prompt
prompt = st.text_area("Enter your prompt:")

# Button to generate response
if st.button("Generate"):
    if prompt.strip():  # Check if prompt is not empty or contains only spaces
        with st.spinner("Generating..."):
            response = llm.invoke(prompt, stop=['<|eot_id|>'])
            st.write(response)

# Clear button to reset input
if st.button("Clear"):
    prompt = ""

# Help section
st.sidebar.title("Help")
st.sidebar.write(
    "1. Enter a prompt in the text area above.\n"
    "2. Click the 'Generate' button to get a response from the chatbot.\n"
    "3. Use the 'Clear' button to reset the input."
)

# Footer with information
st.sidebar.markdown("---")
st.sidebar.write("Built with Streamlit & LLAMA3 by [Nabin Khair](https://github.com/nabinkhair42)")

# Footer with privacy and feedback links
st.sidebar.markdown(
    """
    **Privacy Policy** | [Feedback](mailto:nabinkhair12@gmail.com)
    """
)
