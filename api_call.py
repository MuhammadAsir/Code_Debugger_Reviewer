from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

my_api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=my_api_key)


def code_debugger(code, language):
    prompt = f"""You are an expert debugger and beginner-friendly teacher. Analyze the {language} code below.

Rules:
- Check if code compiles/runs correctly
- Detect ALL errors: syntax, missing libraries, wrong usage, logical issues
- Flag mixed-language concepts (e.g. C mixed with C++)
- Explain everything simply — no complex jargon

Respond in this exact markdown format:

### 🐞 Detected Errors
- Each error with a simple explanation of why it's wrong

### 🛠️ Fixed Code
````{language}
(full corrected code)
````

### 💡 Explanation
Step-by-step: what was changed and why

### ✅ Final Output
What the program outputs after fixing (if runnable)

{language} code:
````{language}
{code}
```"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )
    return response.text



def code_reviewer(code, language):
    prompt = f"""You are a friendly but smart Programming Teacher. Review the {language} code below.

Rules:
- Check if code has errors or won't compile
- Point out ALL mistakes (missing headers, wrong syntax, logic issues) and explain WHY simply
- Never ignore serious mistakes

Respond in this exact markdown format:

### 🌟 Encouragement & Score
Score /10 (reduce for errors, stay encouraging)

### ❌ Mistakes Found
- List each error with a simple explanation of why it's wrong

### 🚀 Easy Ways to Improve
2–3 simple improvements for readability or logic

### ✨ Polished Code
``````{language}
(fully corrected code)
``````

{language} code:
``````{language}
{code}
`````"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )
    return response.text

