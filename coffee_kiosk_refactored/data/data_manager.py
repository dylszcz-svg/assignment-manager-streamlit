import json
from pathlib import Path


# Define and export paths for other modules to use

DATA_DIR = Path(__file__).parent
INVENTORY_PATH = DATA_DIR / "inventory.json"
ORDERS_PATH = DATA_DIR / "orders.json"


# Note on ALL_CAPS: In Python, variables written in all capital letters are
# treated as "constants." This is a convention to signal to other developers
# that this value is not expected to change during the program's execution.


def load_data(json_path: Path):
# """Generic function to load a list of dictionaries from a JSON file."""
    if json_path.exists():
        with open(json_path, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return []
    
def save_data(data: list, json_path: Path):
# """Generic function to save a list of dictionaries to a JSON file."""
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)