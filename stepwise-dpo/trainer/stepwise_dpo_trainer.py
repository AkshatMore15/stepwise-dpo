# trainer/stepwise_dpo_trainer.py

import json
from pathlib import Path

def load_data(file_path: str, limit: int = 3):
    print(f"📦 Loading data from: {file_path}")
    samples = []

    with open(file_path, 'r') as f:
        for i, line in enumerate(f):
            if i >= limit:
                break

            sample = json.loads(line)
            steps = sample.get("label", {}).get("steps", [])
            if not steps:
                continue

            samples.append(steps)
    return samples


def simulate_dpo_stepwise(samples):
    print("⚙️ Starting simulated DPO training...\n")
    for sample_idx, steps in enumerate(samples):
        print(f"🧩 Sample {sample_idx + 1}:")
        for step_idx, step in enumerate(steps):
            completions = step.get("completions", [])
            chosen_index = step.get("chosen_completion")

            if not completions or chosen_index is None or chosen_index >= len(completions):
                print(f"   ⚠️ Step {step_idx} skipped due to invalid structure.")
                continue

            chosen = completions[chosen_index]
            rating = chosen.get("rating", -1)

            print(f"   ✅ Step {step_idx}: Chosen index = {chosen_index}, Rating = {rating}")

            # Simulated loss (dummy value)
            loss = 1.0 - (rating / 5.0) if rating >= 0 else 1.0
            print(f"   🔧 Simulated loss: {loss:.4f}")

        print()


if __name__ == "__main__":
    data_file = "data/prm800k/data/phase2_train.jsonl"  # Replace if needed
    sample_steps = load_data(data_file, limit=3)
    simulate_dpo_stepwise(sample_steps)
