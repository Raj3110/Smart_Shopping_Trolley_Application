import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

PRODUCT_FILE = os.path.join(DATA_DIR, "products.json")
ORDER_FILE = os.path.join(DATA_DIR, "orders.json")
LOG_FILE = os.path.join(DATA_DIR, "audit.log")


def init_storage():
    """
    Initialize storage safely.
    - Creates data folder if missing
    - Creates files only if missing or empty
    - NEVER deletes or overwrites existing data
    """
    os.makedirs(DATA_DIR, exist_ok=True)

    _ensure_json_file(PRODUCT_FILE)
    _ensure_json_file(ORDER_FILE)

    if not os.path.exists(LOG_FILE):
        open(LOG_FILE, "a").close()


def _ensure_json_file(path):
    """
    Ensure file exists and contains valid JSON list.
    Prevents JSONDecodeError on new or corrupted files.
    """
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        with open(path, "w") as f:
            json.dump([], f)


def load_products():
    try:
        with open(PRODUCT_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_products(products):
    with open(PRODUCT_FILE, "w") as f:
        json.dump(products, f, indent=4)


def load_orders():
    try:
        with open(ORDER_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_orders(orders):
    with open(ORDER_FILE, "w") as f:
        json.dump(orders, f, indent=4)


def log_event(message):
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")
