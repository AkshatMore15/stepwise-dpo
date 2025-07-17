
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
