# Two Provider Cost Tracker

## Project Overview

This project compares two Large Language Model (LLM) providers: Google Gemini and Groq.

It sends the same user prompt to both providers and compares their responses, token usage, response time, and estimated API costs.

## Technologies Used

- Python
- Google Gemini API
- Groq API
- python-dotenv
- uv
- JSON

## Features

- Send the same prompt to Gemini and Groq.
- Get actual responses from both providers.
- Retrieve input and output token counts from API usage data.
- Measure response time in seconds.
- Calculate estimated API costs.
- Display a comparison table.
- Save results in `results.json`.
- Store API keys securely in `.env`.

## Project Structure

```text
Assignment_01_Two_Provider_Cost_Tracker/
│
├── tracker.py
├── results.json
├── README.md
├── .env
├── .env.example
├── .gitignore
├── pyproject.toml
└── uv.lock
```

## Installation

Make sure Python and uv are installed.

Install the project dependencies:

```bash
uv sync
```

## Environment Setup

Create a `.env` file in the project root.

Add your own API keys and model names:

```env
GEMINI_API_KEY=your_gemini_api_key
GROQ_API_KEY=your_groq_api_key

GEMINI_MODEL=your_gemini_model
GROQ_MODEL=your_groq_model

GEMINI_INPUT_PRICE_PER_M=0.30
GEMINI_OUTPUT_PRICE_PER_M=2.50

GROQ_INPUT_PRICE_PER_M=your_input_price
GROQ_OUTPUT_PRICE_PER_M=your_output_price
```

Never upload your real `.env` file or API keys to GitHub.

## How to Run

Run the tracker with a prompt:

```bash
uv run tracker.py "Explain Agentic AI with an example"
```

You can also run it without a prompt and enter one when requested:

```bash
uv run tracker.py
```

## Output

The program displays:

- Gemini response
- Groq response
- Input tokens
- Output tokens
- Response time
- Estimated cost in USD

The results are also saved to `results.json`.

## Cost Calculation

The project uses this formula:

```text
Input Cost =
(input_tokens × input_price_per_m) / 1,000,000

Output Cost =
(output_tokens × output_price_per_m) / 1,000,000

Total Cost = Input Cost + Output Cost
```

## What I Learned

Through this assignment, I learned how to integrate two LLM providers into one Python application, securely manage API keys using environment variables, retrieve real token usage, measure API response time, calculate estimated costs, and save structured results in JSON.
