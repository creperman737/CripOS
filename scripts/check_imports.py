"""CripOS import xatolarini tekshirish skripti."""
import os
import importlib.util
import sys

errors = []
py_files = []

for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in ['__pycache__', '.git', 'build', 'node_modules', '.venv']]
    for f in files:
        if f.endswith('.py'):
            py_files.append(os.path.join(root, f))

print(f"Jami Python fayllar: {len(py_files)}")

for filepath in py_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        if 'tkinter' in content:
            continue
        module_name = os.path.splitext(os.path.basename(filepath))[0]
        module_dir = os.path.dirname(os.path.abspath(filepath))
        spec = importlib.util.spec_from_file_location(module_name, filepath)
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            # Add the module's directory to sys.path so relative imports work
            old_path = sys.path.copy()
            sys.path.insert(0, module_dir)
            try:
                spec.loader.exec_module(module)
            except Exception as e:
                errors.append(f"IMPORT ERROR: {filepath}: {type(e).__name__}: {e}")
            finally:
                sys.path = old_path
    except Exception:
        pass

if errors:
    print(f"\n=== {len(errors)} XATO TOPILDI ===")
    for err in errors:
        print(err)
else:
    print("\n=== IMPORT XATOLAR YO'Q ===")

sys.exit(1 if errors else 0)