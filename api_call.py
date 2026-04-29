from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

my_api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=my_api_key)

def code_debugger(code, language):
    prompt = f"""You are an expert Programming Debugger and a beginner-friendly teacher.

Your job is to carefully analyze the following {language} code.

IMPORTANT RULES:
- First, check if the code will compile or run correctly.
- Detect ALL errors (syntax, missing libraries, wrong usage, logical issues).
- Do NOT ignore any mistakes.
- Be clear and simple in explanations (no complex jargon).
- If the code mixes concepts incorrectly (like C and C++), point it out.

Provide the output in this strict markdown format:

### 🐞 Detected Errors
- (List each error clearly)
- (Explain WHY it is wrong in simple words)

### 🛠️ Fixed Code
(Provide the FULL corrected {language} code in a proper code block)

### 💡 Explanation
(Explain what you changed and why, step by step in simple terms)

### ✅ Final Output (if applicable)
(What the program will output after fixing, if it can run)

Here is the {language} code:
{code}
"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )
    return response.text


def code_reviewer(code, language):
    
    prompt = f"""You are a friendly but smart Programming Teacher.

Carefully review the following {language} code.

IMPORTANT:
- First, check if the code has any errors or will not compile.
- Clearly point out ALL mistakes (missing headers, wrong syntax, etc.)
- Then explain them in a simple way (no complex jargon).
- Do NOT ignore serious mistakes.

Provide the output in this strict markdown format:

### 🌟 Encouragement & Score
(Give a score out of 10, but reduce score if there are errors. Still be encouraging.)

### ❌ Mistakes Found
(List all errors clearly and simply. Explain WHY they are wrong.)

### 🚀 Easy Ways to Improve
(Give 2-3 simple improvements for readability or logic.)

### ✨ Polished Code
(Fix the code properly and provide correct {language} code.)

Here is the {language} code:
{code}
"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )
    return response.text
