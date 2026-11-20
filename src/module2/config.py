import json
from pathlib import Path

# Get project root directory
project_root = Path(__file__).resolve().parents[2]

# Build path to config file
config_file = project_root / "config" / "config.json"

# Read JSON file
with open(config_file, "r") as f:
    config = json.load(f)

print("Application:", config["application"])
print("Environment:", config["environment"])
print("Timeout:", config["timeout"])