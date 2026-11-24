
import os
import sys
import time
import json

from dotenv import load_dotenv
from google import genai
from groq import Groq

# Load API keys and model names
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GEMINI_MODEL = os.getenv("GEMINI_MODEL")
GROQ_MODEL = os.getenv("GROQ_MODEL")


# Get prompt from terminal
if len(sys.argv) > 1:
    prompt = " ".join(sys.argv[1:])
else:
    prompt = input("Enter your prompt: ")


# ---------------- GEMINI ----------------

print("\n--- GEMINI RESPONSE ---")

gemini_client = genai.Client(api_key=GEMINI_API_KEY)

start = time.time()

gemini_response = gemini_client.models.generate_content(
    model=GEMINI_MODEL,
    contents=prompt
)

gemini_time = time.time() - start

print(gemini_response.text)

gemini_input = gemini_response.usage_metadata.prompt_token_count
gemini_output = gemini_response.usage_metadata.candidates_token_count

# Gemini prices per million tokens
gemini_input_price = 0.30
gemini_output_price = 2.50

gemini_cost = (
    gemini_input * gemini_input_price / 1000000
    + gemini_output * gemini_output_price / 1000000
)


# ---------------- GROQ ----------------

print("\n--- GROQ RESPONSE ---")

groq_client = Groq(api_key=GROQ_API_KEY)

start = time.time()

groq_response = groq_client.chat.completions.create(
    model=GROQ_MODEL,
    messages=[
        {"role": "user", "content": prompt}
    ]
)

groq_time = time.time() - start

print(groq_response.choices[0].message.content)

groq_input = groq_response.usage.prompt_tokens
groq_output = groq_response.usage.completion_tokens

# Groq prices per million tokens
groq_input_price = 0.075
groq_output_price = 0.30

groq_cost = (
    groq_input * groq_input_price / 1000000
    + groq_output * groq_output_price / 1000000
)


# ---------------- COMPARISON ----------------

print("\n--- COMPARISON TABLE ---")

print("Provider     Input Tokens     Output Tokens     Time     Cost USD")

print(
    "Gemini       ",
    gemini_input,
    "             ",
    gemini_output,
    "             ",
    round(gemini_time, 3),
    "   ",
    gemini_cost
)

print(
    "Groq         ",
    groq_input,
    "             ",
    groq_output,
    "             ",
    round(groq_time, 3),
    "   ",
    groq_cost
)


# ---------------- SAVE RESULTS ----------------

results = [
    {
        "provider": "Gemini",
        "model": GEMINI_MODEL,
        "reply": gemini_response.text,
        "input_tokens": gemini_input,
        "output_tokens": gemini_output,
        "response_time_seconds": round(gemini_time, 3),
        "input_price_per_m": gemini_input_price,
        "output_price_per_m": gemini_output_price,
        "cost_usd": gemini_cost
    },
    {
        "provider": "Groq",
        "model": GROQ_MODEL,
        "reply": groq_response.choices[0].message.content,
        "input_tokens": groq_input,
        "output_tokens": groq_output,
        "response_time_seconds": round(groq_time, 3),
        "input_price_per_m": groq_input_price,
        "output_price_per_m": groq_output_price,
        "cost_usd": groq_cost
    }
]

with open("results.json", "w") as file:
    json.dump(results, file, indent=4)

print("\nResults saved in results.json")
