"""
config.py -- Configuration and environment validation.
This project requires no Azure credentials.
Run directly to confirm Python and pandas versions.
"""
import sys
import importlib


def check_dependencies():
    required = ["pandas", "rich"]
    missing = []
    for pkg in required:
        try:
            importlib.import_module(pkg)
        except ImportError:
            missing.append(pkg)
    return missing


if __name__ == "__main__":
    print(f"Python version : {sys.version.split()[0]}")
    missing = check_dependencies()
    if missing:
        print(f"[ERROR] Missing packages: {missing}")
        print("Run: pip install -r requirements.txt")
    else:
        print("[OK] All dependencies available.")
        import pandas as pd
        print(f"pandas version : {pd.__version__}")
