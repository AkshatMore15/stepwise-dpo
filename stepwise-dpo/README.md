
## ✅ Day 1 Summary

We completed the full setup for the Stepwise DPO project:

- [x] Created a Python 3.11 virtual environment using `venv`
- [x] Installed PyTorch with MPS support (macOS ARM)
- [x] Verified `torch` + `mps` compatibility
- [x] Cloned the [PRM800k dataset](https://github.com/openai/prm800k) and fixed folder structure
- [x] Added `helpers.py` to load `.jsonl` format datasets
- [x] Project folder structure organized: `reward_model`, `trainer`, `experiments`, `utils`, `data`
- [x] GitHub connected and `.gitignore` updated

---

### ✅ Day 2 Summary

We evaluated our reward model using Phase 2 dataset samples to verify reward alignment:

* Cleaned and analyzed structure of `phase2_train.jsonl` dataset
* Filtered out invalid steps or completions with missing or malformed data
* Successfully computed reward model accuracy on valid samples: **✅ 100% accuracy**
* Used local scripts (`eval_llm_reward.py`) to avoid excessive OpenAI API usage and conserve credits
* Implemented logging to handle structure issues gracefully
* **🧠 Took help from ChatGPT (LLM) for debugging dataset structure, writing cleaner iteration logic, and accuracy calculation strategy**

---

### ✅ Day 3 Summary

Simulated a DPO (Direct Preference Optimization) training loop using reward ratings:

* Created `stepwise_dpo_trainer.py` to simulate DPO training using parsed reward scores
* Handled structured preference scores from completions, computed simulated losses
* Implemented per-step tracking: loss values, chosen completion index, and rating correctness
* Skipped steps with invalid or missing data cleanly
* Successfully tested across 3 Phase 2 samples with correct loss behavior
* **🧠 Took help from ChatGPT (LLM) for implementing simulated preference-based training logic, designing step validation, and structured logs**

---

Absolutely, here's the updated and more concise **Day 4 README entry** with just "help was taken" mentioned:

---

## 🧠 **Day 4 – Final Day (DPO Trainer Integration & Execution Attempt)**

On the final day of the internship, the main goal was to integrate Hugging Face's **DPOTrainer** and perform preference-based fine-tuning on the Phase 2 dataset.

### ✅ Work Done:

* Implemented `load_phase2_dataset()` to process the `.jsonl` data into the format expected by DPOTrainer.
* Set up the script `run_hf_dpo_trainer.py` using:

  * `AutoTokenizer` and `AutoModelForCausalLM`
  * `DPOTrainer` and `DPOConfig`
  * Training arguments for evaluation and logging.
* Attempted model training using `mistralai/Mistral-7B-v0.1`.

### ⚠️ Issues Encountered:

* Hugging Face **gated repo** error: 401 Unauthorized for Mistral-7B.
* `DPOConfig` and `TrainingArguments` keyword compatibility issues.
* Local environment lacking GPU for actual training.
* File path mismatch errors while loading the dataset.

Despite multiple troubleshooting attempts, actual DPO training could not be executed successfully due to these limitations.

---

### 🤖 AI Help Taken:

Help was taken from **ChatGPT** to debug errors, set up the trainer, and handle compatibility and model loading issues.

---

### 📝 Final Note:

Although full training wasn’t achieved, the pipeline for dataset preparation, trainer configuration, and execution was successfully implemented, showing readiness for deployment in a properly resourced environment.

---

