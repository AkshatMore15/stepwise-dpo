# experiments/test_device.py

import torch

if torch.backends.mps.is_available():
    print("✅ MPS backend is available.")
else:
    print("⚠️ MPS not available. Falling back to CPU.")
