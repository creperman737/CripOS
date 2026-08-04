"""CripOS JSON fayllarini tekshirish skripti."""
import json
import os
import sys

errors = []
json_files = []

for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in ['__pycache__', '.git', 'build', 'node_modules', '.venv']]
    for f in files:
        if f.endswith('.json'):
            json_files.append(os.path.join(root, f))

print(f"Jami JSON fayllar: {len(json_files)}")

for filepath in json_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            json.load(f)
    except json.JSONDecodeError as e:
        errors.append(f"JSON ERROR: {filepath}: {e}")
    except Exception as e:
        errors.append(f"READ ERROR: {filepath}: {e}")

if errors:
    print(f"\n=== {len(errors)} XATO TOPILDI ===")
    for err in errors:
        print(err)
else:
    print("\n=== JSON XATOLAR YO'Q ===")

sys.exit(1 if errors else 0)