# experiments/test_llm_reward.py

from reward_model.llm_reward import get_preference_from_gpt

sample = {
    "question": "What is 12 + 23?",
    "answer_a": "Step 1: Add 10 + 20 = 30. Step 2: Add 2 + 3 = 5. Step 3: Final answer = 35.",
    "answer_b": "Add 10 + 3 = 13. Then 2 + 20 = 22. Final answer: 35."
}

print("LLM preference:", get_preference_from_gpt(
    sample["question"],
    sample["answer_a"],
    sample["answer_b"]
))
