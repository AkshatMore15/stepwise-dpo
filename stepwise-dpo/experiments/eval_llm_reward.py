def evaluate_batch(filepath, limit=3):
    import json

    correct = 0
    total = 0

    with open(filepath, "r") as f:
        for i, line in enumerate(f):
            if i >= limit:
                break

            sample = json.loads(line)

            question = sample.get("question", {}).get("problem", "")
            steps = sample.get("label", {}).get("steps", [])

            for step_index, step in enumerate(steps):
                completions = step.get("completions", [])
                chosen = step.get("chosen_completion")

                if not completions or chosen is None or chosen >= len(completions):
                    print(f"⚠️ Step {step_index+1}: skipping due to invalid structure")
                    continue

                # Get rating of chosen one
                chosen_rating = completions[chosen].get("rating", -1)
                best_rating = max([c.get("rating", -1) for c in completions])

                if chosen_rating == best_rating:
                    correct += 1
                total += 1

    print(f"\n✅ Accuracy: {correct}/{total} = {(correct / total):.2%}" if total else "\n⚠️ No valid steps found.")

if __name__ == "__main__":
    evaluate_batch("data/prm800k/data/phase2_train.jsonl", limit=3)
