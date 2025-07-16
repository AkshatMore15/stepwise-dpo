# reward_model/llm_reward.py

import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def format_prompt(question: str, answer_a: str, answer_b: str) -> str:
    """Create a prompt to compare two answers."""
    return f"""
You are an expert AI tutor. Compare the following two answers and choose which one demonstrates better step-by-step reasoning.

Question: {question}

Answer A:
{answer_a}

Answer B:
{answer_b}

Which answer is better? Respond with only 'A' or 'B'.
"""

def get_preference_from_gpt(question: str, answer_a: str, answer_b: str) -> str:
    """Use OpenAI GPT to choose between answer A or B."""
    prompt = format_prompt(question, answer_a, answer_b)

    try:
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an impartial judge of logical reasoning quality."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.0
        )

        message = response.choices[0].message.content
        if message is not None:
            reply = message.strip().lower()
            if "a" in reply:
                return "a"
            elif "b" in reply:
                return "b"
            else:
                return "unknown"
        else:
            return "unknown"

    except Exception as e:
        print("❌ OpenAI API Error:", e)
        return "error"
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an impartial judge of logical reasoning quality."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.0
        )

        message = response.choices[0].message.content
        if message is not None:
            reply = message.strip().lower()
            if "a" in reply:
                return "a"
            elif "b" in reply:
                return "b"
        else:
            return "unknown"
