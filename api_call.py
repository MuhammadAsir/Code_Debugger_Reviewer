from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

my_api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=my_api_key)

def code_debugger(code, language):
    # Notice we added {language} to the prompt so the AI knows the exact syntax!
    prompt = f"""You are a helpful AI Developer Assistant. Analyze the following {language} code and debug it.
    Provide the output in this strict markdown format:
    ### 🐞 Detected Errors
    (Explain what is wrong in simple, beginner-friendly terms)
    ### 🛠️ Fixed Code
    (Provide the corrected {language} code in a code block)
    ### 💡 Explanation
    (Explain why you made these fixes)

    Here is the {language} code:
    {code}
    """

    response = client.models.generate_content(
        model="gemini-3-flash-preview", 
        contents=prompt
    )
    return response.text

def code_reviewer(code, language):
    
    prompt = f"""You are a friendly, encouraging Programming Teacher. Review the following {language} code to help a beginner learn and improve. 
    Do NOT use confusing jargon. Explain things simply, as if you are talking to a student.
    
    Provide the output in this strict markdown format:
    ### 🌟 Encouragement & Score
    (Give a friendly score out of 10 and say something nice about what they did well)
    
    ### 🚀 Easy Ways to Improve
    (Give 2 or 3 simple suggestions. Focus on making the code easier to read, like better variable names or simpler logic. Explain WHY the change helps in simple words.)
    
    ### ✨ Polished Code
    (Provide the improved {language} code in a code block. Keep it simple and don't make it overly advanced.)

    Here is the {language} code:
    {code}
    """

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )
    return response.text