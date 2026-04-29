import streamlit as st
from api_call import code_debugger, code_reviewer

# App title
st.title(":green[🧠 AI Developer Assistant]", anchor=False)

# Instruction message for users
st.markdown(":violet-background[Select your language, paste your code to detect bugs, get fixes, and receive a professional code review!]")
st.divider()

with st.sidebar:
    st.header(":blue[Input Your Code]")
    
    # NEW: Dropdown for Programming Language
    language = st.selectbox("Select Programming Language",
                 ("Python", "JavaScript", "Java", "C++", "C#", "HTML/CSS", "SQL", "Other"), index=None)
    
    # Text area for pasting code
    user_code = st.text_area("Paste your code here:", height=300)

    # Mode selection
    selected = st.selectbox("Select Action",
                 ("Debug Code", "Review Code", "Both"), index=None)     
    
    press = st.button("Analyze Code", type="primary")

# Action after button is pressed
if press:
    # Error handling (Now includes a check for language)
    if not language:
        st.error("Please select a programming language.")
    if not user_code:
        st.error("Please paste some code to analyze.")
    if not selected:
        st.error("Please select an action (Debug, Review, or Both).")
    
    # If all inputs are provided, run the AI
    if language and user_code and selected:
        
        # Debug Mode
        if selected in ["Debug Code", "Both"]:
            with st.container(border=True):
                st.subheader(f"🔧 Debugger Report ({language})", anchor=False)
                
                with st.spinner("AI is hunting for bugs..."):
                    # We now pass BOTH user_code and language to the function!
                    debug_result = code_debugger(user_code, language)
                    st.markdown(debug_result)
        
        # Review Mode
        if selected in ["Review Code", "Both"]:
            with st.container(border=True):
                st.subheader(f"🚀 Code Review Report ({language})", anchor=False)
                
                with st.spinner("AI is reviewing your code quality..."):
                    review_result = code_reviewer(user_code, language)
                    st.markdown(review_result)