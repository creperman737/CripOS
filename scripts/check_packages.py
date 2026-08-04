"""CripOS papkalarida __init__.py mavjudligini tekshirish."""
import os

missing = []
for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in ['__pycache__', '.git', 'build', 'node_modules', '.venv', 'assets', 'locales', 'sounds', 'wallpapers', 'themes', 'branding', 'docs', 'config', 'installer', 'packages', 'store', 'system', 'tests']]
    for d in dirs:
        init_path = os.path.join(root, d, '__init__.py')
        if not os.path.exists(init_path):
            # Check if directory contains Python files
            has_py = any(f.endswith('.py') for f in os.listdir(os.path.join(root, d)))
            if has_py:
                missing.append(os.path.join(root, d))

if missing:
    print("Python fayllari bor lekin __init__.py yo'q papkalar:")
    for m in missing:
        print(f"  - {m}")
else:
    print("Barcha papkalarda __init__.py mavjud yoki Python fayllari yo'q.")