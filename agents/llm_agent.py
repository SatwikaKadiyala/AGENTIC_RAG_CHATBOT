from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in your .env file or environment variables.")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

class LLMResponseAgent:
    def __init__(self):
        pass

    def generate_response(self, query, context_chunks):
        prompt = (
            "You are an assistant answering questions based on documents.\n"
            f"Context:\n{chr(10).join(context_chunks[:5])}\n\n"
            f"Question: {query}\nAnswer:"
        )

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=300
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error during OpenAI API call: {e}")
            return "An error occurred while generating a response."
